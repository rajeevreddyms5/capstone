from django import template
from django.utils.translation import to_locale, get_language
from babel.numbers import format_currency
from chittabook.models.userprofile import UserProfile
from babel import Locale

register = template.Library()


# function for formating decimal values into currency
def formatter(context, decimal, currency_name, country):
    locale_string = "und_" + country
    locale = Locale.parse(locale_string)
    return format_currency(decimal, currency_name, locale=locale)

register.simple_tag(takes_context=True)(formatter)
