from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.context import bag_contents
import stripe
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY
if not settings.STRIPE_SECRET_KEY:
    raise ValueError("STRIPE_SECRET_KEY is missing. Check env.py / environment variables.")



@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            current_bag = bag_contents(request)
            order.order_total = current_bag['total']
            order.delivery_cost = current_bag['delivery']
            order.grand_total = current_bag['grand_total']
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag "
                        "wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total_eur = current_bag['grand_total']

        # Get selected currency from session
        selected_currency = request.session.get("currency", "EUR").upper()

        # Validate currency
        if selected_currency not in settings.CURRENCIES:
            selected_currency = "EUR"

        # Get exchange rate
        rate = settings.CURRENCIES[selected_currency]["rate"]

        # Convert total
        converted_total = round(total_eur * rate, 2)

        # Stripe requires smallest unit
        stripe_total = int(converted_total * 100)

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=selected_currency.lower(),
        )



        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        # in the video, the below code is not indented properly
        # this is the correct indentation
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'converted_total': converted_total,
            'selected_currency': selected_currency,
        }


        return render(request, template, context)
        # end of the corrected indentation


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # ---- DEDUCT STOCK AFTER SUCCESSFUL ORDER ----
    for line_item in order.lineitems.all():
        product = line_item.product
        product.stock -= line_item.quantity
        product.save()


    # Attach user profile if authenticated
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        # Save the user's default delivery info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # --- SEND CONFIRMATION EMAIL ---
    subject = render_to_string(
        'checkout/email/order_confirmation_subject.txt',
        {'order': order}
    )

    body = render_to_string(
        'checkout/email/order_confirmation_body.txt',
        {'order': order}
    )

    send_mail(
        subject.strip(),
        body,
        settings.EMAIL_HOST_USER,
        [order.email],
        fail_silently=False,
    )
    # --- END EMAIL ---

    messages.success(request, f'Order successfully processed! '
        f'Your order number is {order_number}. '
        f'A confirmation email was sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    selected_currency = request.session.get("currency", "EUR").upper()

    if selected_currency not in settings.CURRENCIES:
        selected_currency = "EUR"

    currency_symbol = settings.CURRENCIES[selected_currency]["symbol"]
    rate = settings.CURRENCIES[selected_currency]["rate"]

    order_total_converted = (order.order_total * rate).quantize(Decimal("0.01"))
    delivery_converted = (order.delivery_cost * rate).quantize(Decimal("0.01"))
    grand_total_converted = (order.grand_total * rate).quantize(Decimal("0.01"))
    
    context = {
    'order': order,
    'currency_symbol': currency_symbol,
    'order_total_converted': order_total_converted,
    'delivery_converted': delivery_converted,
    'grand_total_converted': grand_total_converted,
}
    return render(request, template, context)

