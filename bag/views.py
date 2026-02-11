from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)

    # ---- STOCK PROTECTION ----
    if product.stock == 0:
        messages.error(request, "Sorry, this product is out of stock.")
        return redirect(redirect_url)

    bag = request.session.get('bag', {})

    current_quantity = 0

    # Get current quantity already in bag
    if item_id in bag:
        if size:
            if size in bag[item_id]['items_by_size']:
                current_quantity = bag[item_id]['items_by_size'][size]
        else:
            current_quantity = bag[item_id]

    # Prevent exceeding stock
    if current_quantity + quantity > product.stock:
        messages.error(
            request,
            f"Only {product.stock} available in stock."
        )
        return redirect(redirect_url)
    if size:
        if item_id in bag:
            if size in bag[item_id]['items_by_size']:
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to '
                    f'{bag[item_id]["items_by_size"][size]}',
                    extra_tags='bag'
                )
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag',
                    extra_tags='bag'
                )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag',
                extra_tags='bag'
            )
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}',
                extra_tags='bag'
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Added {product.name} to your bag',
                extra_tags='bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size', None)

    bag = request.session.get('bag', {})

    # ---- STOCK VALIDATION ----
    if quantity > product.stock:
        messages.error(
            request,
            f"You cannot set quantity higher than available stock ({product.stock})."
        )
        return redirect(reverse('view_bag'))

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to '
                f'{quantity}'
            )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {quantity}',
                extra_tags='bag'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} from your bag',
                extra_tags='bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)