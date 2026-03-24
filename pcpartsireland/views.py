from django.shortcuts import redirect
from django.conf import settings


def set_currency(request):
    if request.method == "POST":
        currency = request.POST.get("currency")

        if currency in settings.CURRENCIES:
            request.session['currency'] = currency

    return redirect(request.META.get('HTTP_REFERER', '/'))