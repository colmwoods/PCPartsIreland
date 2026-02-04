from django.conf import settings

def currency_context(request):
    currency = request.session.get('currency', 'EUR')
    currency_data = settings.CURRENCIES.get(currency, settings.CURRENCIES['EUR'])

    return {
        'current_currency': currency,
        'currency_symbol': currency_data['symbol'],
        'currency_rate': currency_data['rate'],
        'currencies': settings.CURRENCIES,
    }
