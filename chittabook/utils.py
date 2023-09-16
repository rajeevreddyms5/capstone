from django.contrib.gis.geoip2 import GeoIP2
import json

# get country code using ip address
def currency(request):
    g = GeoIP2()
    remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        address = remote_addr.split(',')[-1].strip()
    else:
        address = request.META.get('REMOTE_ADDR')
    
    return g.country_code(address)  # returns a 2-letter country code