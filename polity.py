
import pandas as pd

def get_polity(df):
    try:
        vals = polity.loc[(polity['scode']==df['country_code']) & (polity['year']==df['iyear'])]['polity'].values
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
	d = pd.read_csv('gtd98_now.csv')
	polity = pd.read_csv('p4v2015.csv')
	d['polity'] = d.apply(get_polity, axis=1)


