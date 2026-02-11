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
            'description',
            'price',
            'category',
            'rating',
            'stock',
            'image_url',
        )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock',
        'stock_status',
        'rating',
    )

    list_filter = ('category',)
    search_fields = ('name', 'description', 'sku')

    list_editable = ('price', 'stock')

    ordering = ('name',)

    # ---- Stock Indicator ----
    def stock_status(self, obj):
        if obj.stock == 0:
            return "❌ Out of Stock"
        elif obj.stock < 5:
            return "⚠️ Low Stock"
        return "✅ In Stock"

    stock_status.short_description = "Stock Status"