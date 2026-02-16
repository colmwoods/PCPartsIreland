from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.product_search, name='product_search'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
]