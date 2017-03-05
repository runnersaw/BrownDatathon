
import pandas as pd
from database import data, polity_data

def get_polity(df):
    try:
        vals = polity_data.loc[(polity_data['scode']==df['country_code']) & (polity_data['year']==df['iyear'])]['polity'].values
    except Exception as e:
        print(str(e))
        print(df)
        vals = [-88]
    global count
    count += 1
    if count % 1000 == 0:
        print(count)
    if len(vals) > 0:
        return vals[0]
    else:
        return -88

if __name__=="__main__":
	count = 0
	data['polity'] = data.apply(get_polity, axis=1)


