from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.email}"
    

class ReturnRequest(models.Model):

    RETURN_REASONS = [
        ("faulty", "Faulty item"),
        ("wrong_item", "Wrong item received"),
        ("not_needed", "No longer needed"),
        ("other", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    order_number = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)

    reason = models.CharField(max_length=20, choices=RETURN_REASONS)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Return {self.order_number} - {self.email}"