from django.shortcuts import redirect
from django.conf import settings

def set_currency(request, currency_code):
    if currency_code in settings.CURRENCIES:
        request.session['currency'] = currency_code
    return redirect(request.META.get('HTTP_REFERER', '/'))