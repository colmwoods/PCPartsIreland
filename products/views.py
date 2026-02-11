from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

# Create your views here.
def all_products(request):
    """
    A view to show all products, including sorting and category filtering.
    """
    products = Product.objects.all()
    current_categories = None
    current_sorting = 'None_None'
    search_term = None

    # Category filter: /products/?category=ddr4,ddr5
    if 'category' in request.GET:
        categories = request.GET['category'].split(',')

        query = Q()
        for cat in categories:
            cat = cat.strip()
            query |= Q(category__name=cat)
            query |= Q(category__name__startswith=f"{cat}-")
            query |= Q(category__name__contains=f"-{cat}-")

        products = products.filter(query).distinct()
        current_categories = Category.objects.filter(name__in=categories)
    else:
        categories = []
        # current_categories stays None

    # Sorting: /products/?sort=price&direction=asc
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        direction = request.GET.get('direction', 'asc')

        if sortkey == 'name':
            sortkey = 'name'
        elif sortkey == 'price':
            sortkey = 'price'
        elif sortkey == 'rating':
            sortkey = 'rating'
        elif sortkey == 'category':
            sortkey = 'category__name'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)
        current_sorting = f"{request.GET['sort']}_{direction}"

    context = {
        'products': products,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
        'search_term': search_term,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
    A view to show individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

from django.shortcuts import render
from django.db.models import Q
from .models import Product


def product_search(request):
    query = request.GET.get('q')

    if not query:
        return render(request, 'search/search_results.html')

    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(sku__icontains=query)
    )

    # 🔥 IF RESULTS EXIST → USE PRODUCTS PAGE
    if products.exists():
        return render(request, 'products/products.html', {
            'products': products,
            'search_term': query,
            'current_categories': None,
            'current_sorting': 'None_None',
        })

    # ❌ IF NO RESULTS → USE HERO EMPTY PAGE
    return render(request, 'search/search_results.html', {
        'query': query
    })


from django.http import JsonResponse

def search_suggestions(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)[:5]

    data = [
        {
            'name': product.name,
            'url': product.get_absolute_url()
        }
        for product in products
    ]

    return JsonResponse(data, safe=False)
