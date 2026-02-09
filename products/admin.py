from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.core.files.base import ContentFile
import requests

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


class ProductResource(resources.ModelResource):
    image_url = fields.Field(column_name='image_url')

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

    def dehydrate_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return ''

    def before_import_row(self, row, **kwargs):
        image_url = row.get('image_url')

        if image_url:
            try:
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()

                filename = image_url.split('/')[-1]
                row['image'] = ContentFile(response.content, name=filename)

            except Exception as e:
                print(f"Image download failed: {image_url} ({e})")


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'category', 'price', 'rating')
    list_filter = ('category',)
    search_fields = ('name', 'description')
