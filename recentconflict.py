import numpy as np
import pandas as pd
import re
from iso3166 import countries

def get_country_code(country):
    try:
        return countries.get(country).alpha3
    except:
        return None

def clean_and_save_data(fname=None):
    onesided = pd.read_csv('./files/ucdp-onesided-14-2016.csv')
    armedconflict = pd.read_csv('./files/ucdp-prio-acd-4-2016.csv')
    nonstate = pd.read_csv('./files/ucdp-nonstate-25-2016.csv')

    df = pd.concat([onesided[['Location', 'Year']], armedconflict[['Location', 'Year']], nonstate[['Location', 'Year']]])

    print(len(df.index))

    df_expanded = df.copy()
    # Separate out multiple countries in one location
    for country, subdf in df.groupby('Location'):
        if len(country.split(',')) > 1: # has multiple countries in this field
            for indivcountry in country.split(','):
                cpdf = subdf.copy()
                cpdf["Location"] = indivcountry
                df_expanded = pd.concat([df_expanded, cpdf])

    print(len(df_expanded.index))

    print(df_expanded[df_expanded['Location'] == 'Vietnam']['Year'].unique())

    df = df_expanded.copy()
    # Turn country (old country) into just country
    for country, subdf in df.groupby('Location'):
        wout_paren = re.sub(r'\([^)]*\)', '', country).strip()

        if len(country) > len(wout_paren): # has (old country)
            cpdf = subdf.copy()
            cpdf["Location"] = wout_paren
            df_expanded = pd.concat([df_expanded, cpdf])

    print(len(df_expanded.index))

    print(df_expanded[df_expanded['Location'] == 'Vietnam']['Year'].unique())

    # add country code
    df_expanded['Location ISO'] = df_expanded['Location'].apply(get_country_code)

    if fname is not None:
        df_expanded.to_csv(fname)

    return df_expanded

def recent_conflict(df, country_code, year):
    """Will calculate how many of the past 5 years had conflict
    country_code: i.e. ZWE
    year: year that you want to predict on
    """
    qby_country = df[df['Location ISO'] == country_code]
    years_of_conflict = qby_country['Year'].unique()

    # conflict history over past 5 years
    measure = 0
    for prev_year in range(year - 5, year):
        measure += sum(years_of_conflict == prev_year)
    return measure

mydf = clean_and_save_data()
print(len(mydf.index))
mydf = mydf.dropna()
print(len(mydf.index))

def byumho(x):
    return recent_conflict(mydf, x['Location ISO'], x['Year'])

mydf['Recent Conflict'] = mydf.apply(byumho, axis=1)

mydf.to_csv('recent-conflict.csv')
