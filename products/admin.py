from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating')
    list_filter = ('category',)
    search_fields = ('name', 'description')