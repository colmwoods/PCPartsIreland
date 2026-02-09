from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('sku',)
        fields = (
            'sku',
            'name',
            'price',
            'category',
            'rating',
            'image_url',
        )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'category', 'price', 'rating')
    list_filter = ('category',)
    search_fields = ('name', 'description')