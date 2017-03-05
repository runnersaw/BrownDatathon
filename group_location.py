
from geopy.geocoders import Nominatim
from iso3166 import countries

def country_number_to_code(number):
    return countries.get(number).alpha3

def get_group_location(d, group_name):
    group = d.loc[d['gname'] == group_name]
    lat = group['latitude'].median()
    lon = group['longitude'].median()
    return (lat, lon)

def get_country_from_location(lat, lon):
    geolocator = Nominatim()
    location = geolocator.reverse(str(lat)+', '+str(lon))
    try:
        code = location.raw[u'address'][u'country_code'].encode('utf-8')
    except:
        print('Failed to get address for '+str(lat)+','+str(lon)+' with dict: '+location.raw)
        return None
    if code == 'xk':
        return 'UNK'
    country = countries.get(code)
    return country.name

