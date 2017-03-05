
import pandas as pd
from database import data
from geopy.geocoders import Nominatim
from iso3166 import countries
import json

def get_country_code(country):
    if country.lower() == 'xk' or country.lower() == 'kosovo':
        return 'unk'
    elif country.lower() == 'russia':
        return 'RUS'
    elif country.lower() == 'syria':
        return 'SYR'
    elif country.lower() == 'united kingdom':
        return 'GBR'
    try:
        return countries.get(country).alpha3
    except:
        print(country)
        return '??'

def get_country_code_alpha2(country):
    d = {
        'unk': 'xk',
        'kosovo': 'xk',
        'russia': 'RU',
        'syria': 'SY',
        'united kingdom': 'GB',
        'iran': 'IR',
        'yugoslavia': 'YU',
        'west bank and the gaza strip': 'PS',
        'west bank and gaza strip': 'PS',
        'tanzania': 'TZ',
        'south korea': 'KR',
        'republic of the congo': 'CD',
        'democratic republic of the congo': 'CD',
        'laos': 'LA',
        'serbia-montenegro': 'CS',
        'macedonia': 'MK',
        'bolivia': 'BO',
        'bosnia-herzegovina': 'BA',
        'ivory coast': 'CI',
        'venezuela': 'VE',
        'czech republic': 'CZ',
        'east timor': 'TL',
        'macau': 'MO',
        'moldova': 'MD',
        'slovak republic': 'SK',
        'vietnam': 'VN'
    }
    if country.lower() in d:
        return d[country.lower()]
    try:
        return countries.get(country).alpha2
    except:
        print(country)
        return '??'

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

def get_target_origin_data():
    combos = data.groupby(['country_txt','country_code']).size().reset_index().rename(columns={0:'count'})
    subset = combos[['country_txt', 'country_code', 'count']]
    tuples = [tuple(x) for x in subset.values]
    tuples = sorted(tuples, key=lambda x: x[2], reverse=True)
    print(tuples)

    d = {}
    for t in tuples:
        target = get_country_code_alpha2(t[0])
        origin = get_country_code_alpha2(t[1])
        if target in d:
            d[target][origin] = t[2]
        else:
            d[target] = {origin:t[2]}

    return d

def save_data(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

if __name__=="__main__":
    print(get_groups()[:100])
    print(get_targets())
    print(get_deadliness())
    d = get_target_origin_data()
    print(d)
    save_data('js/attacks.json', d)
