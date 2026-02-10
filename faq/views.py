from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq_list(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, "faq/faq.html", {"faqs": faqs})