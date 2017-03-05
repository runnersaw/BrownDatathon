
import pandas as pd
from database import data
from geopy.geocoders import Nominatim
from iso3166 import countries

def get_country_code(country):
    return countries.get(country).alpha3

def get_group_location(group_name):
    group = data.loc[data['gname'] == group_name]
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

def get_deadliness():
	countries = data.groupby('country_txt').groups
	l = []
	for (k,v) in countries.iteritems():
	    av_kills = data.loc[v]['nkill'].mean()
	    l.append((k,av_kills,len(v)))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	return l

def get_targets():
	countries = data.groupby('country_txt').groups
	groups = {k:len(v) for (k,v) in countries.iteritems()}
	l = []
	for (k,v) in groups.iteritems():
		l.append((k,v))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	return l

def get_groups():
	groups = data.groupby('gname').groups
	groups = {k:len(v) for (k,v) in groups.iteritems()}
	l = []
	for (k,v) in groups.iteritems():
		l.append((k,v))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	return l

if __name__=="__main__":
	print(get_groups()[:100])
	print(get_targets())
	print(get_deadliness())
