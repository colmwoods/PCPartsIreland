from django.contrib import admin
from .models import ContactMessage, ReturnRequest

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')

@admin.register(ReturnRequest)
class ReturnRequestAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "email",
        "reason",
        "created_at",
    )
    list_filter = ("reason",)
    search_fields = ("order_number", "email")