
from geopy.geocoders import Nominatim
from iso3166 import countries

def get_group_location(d, group_name):
    group = d.loc[d['gname'] == group_name]
    lat = group['latitude'].median()
    lon = group['longitude'].median()
    return (lat, lon)

def get_country_from_location(lat, lon):
    geolocator = Nominatim()
    location = geolocator.reverse(str(lat)+', '+str(lon))
    code = location.raw[u'address'][u'country_code'].encode('utf-8')
    if code == 'xk':
        return 'Kosovo'
    country = countries.get(code)
    return country.name

