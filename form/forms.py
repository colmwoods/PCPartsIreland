from django import forms
from .models import ContactMessage, ReturnRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                # Requires Full Domain (.com, .net, etc.)
                'pattern': r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$',
                'title': (
                    'Please include a full email domain, '
                    'like example.com or example.net'
                ),
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Optional phone number'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...'
            }),
        }

class ReturnRequestForm(forms.ModelForm):
    class Meta:
        model = ReturnRequest
        fields = [
            "first_name",
            "last_name",
            "email",
            "order_number",
            "product_name",
            "reason",
            "message",
        ]