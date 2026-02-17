from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from django.conf import settings
from decimal import Decimal



@login_required
def profile(request):
    """ Display the user's profile. """
    profile, created = UserProfile.objects.get_or_create(user=request.user)


    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    selected_currency = request.session.get("currency", "EUR").upper()

    if selected_currency not in settings.CURRENCIES:
        selected_currency = "EUR"

    currency_symbol = settings.CURRENCIES[selected_currency]["symbol"]
    rate = settings.CURRENCIES[selected_currency]["rate"]

    for order in orders:
        order.converted_grand_total = (
            order.grand_total * rate
        ).quantize(Decimal("0.01"))

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

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
    'from_profile': True,
    'currency_symbol': currency_symbol,
    'order_total_converted': order_total_converted,
    'delivery_converted': delivery_converted,
    'grand_total_converted': grand_total_converted,
}
    return render(request, template, context)