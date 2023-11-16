from django.contrib.gis.geoip2 import GeoIP2
from babel.numbers import get_currency_symbol, get_territory_currencies, format_currency
from babel import Locale

# get country code using ip address
def currency(request):
    g = GeoIP2()
    remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        address = remote_addr.split(',')[-1].strip()
    else:
        address = request.META.get('REMOTE_ADDR')
    
    return g.country_code(address)  # returns a 2-letter country code


# get country currency symbol using country code
def currency_symbol(country_code):
    try:
        currency_code = get_territory_currencies(country_code)[0]
        symbol = get_currency_symbol(currency_code)
    except IndexError:
        symbol = ''
    return symbol


# get country currency name from country code
def currency_name(country_code):
    try:
        currency_code = get_territory_currencies(country_code)[0]
    except IndexError:
        currency_code = ''
    return currency_code