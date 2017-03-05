
from urllib2 import urlopen
import json

def get_group_location(d, group_name):
    group = d.loc[d['gname'] == group_name]
    lat = group['latitude'].median()
    lon = group['longitude'].median()
    return (lat, lon)

def get_country_from_location(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
    return country

