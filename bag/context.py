from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        item_total = quantity * product.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'item_total': item_total,
        })

    delivery = settings.STANDARD_DELIVERY_COST
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': total + delivery,
    }

    return context
