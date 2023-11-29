from babel.numbers import get_currency_symbol, get_territory_currencies, format_currency
from babel import Locale


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