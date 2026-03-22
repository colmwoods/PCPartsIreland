from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product', 'quantity', 'lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'email',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
