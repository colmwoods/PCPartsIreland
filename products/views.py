from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Category
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from urllib.parse import urlencode

# Create your views here.
def all_products(request):
    """
    A view to show all products, including sorting,
    category filtering, and pagination.
    """

    products = Product.objects.all()
    current_categories = None
    current_sorting = 'None_None'
    search_term = None

    # -------------------
    # CATEGORY FILTERING
    # -------------------
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

    # -------------------
    # SORTING
    # -------------------
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
        elif sortkey == 'stock':
            sortkey = 'stock'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)
        current_sorting = f"{request.GET['sort']}_{direction}"

    # -------------------
    # PAGINATION
    # -------------------
    per_page = request.GET.get('per_page', 16)

    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 16

    # Cap at 72 (so nobody can request 5000)
    if per_page > 72:
        per_page = 72

    paginator = Paginator(products, per_page)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    querydict = request.GET.copy()
    querydict.pop('page', None)  # remove existing page param
    query_string = urlencode(querydict)

    context = {
        'products': products,
        'per_page': per_page,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
        'search_term': search_term,
        'query_string': query_string,
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


def search_suggestions(request):
    query = request.GET.get('q', '')

    products = Product.objects.filter(
        name__icontains=query
    )[:5]

    data = []

    for product in products:

        if product.image:
            image_url = product.image.url
        elif product.image_url:
            image_url = product.image_url
        else:
            image_url = ""

        data.append({
            'name': product.name,
            'url': f"/products/{product.id}/",
            'image_url': image_url,
        })

    return JsonResponse(data, safe=False)

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, "Failed to add product. Please check the form.")
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, "Failed to update product.")
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {
        'form': form,
        'product': product,
    })

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    return redirect(reverse('products'))

