
import pandas as pd
from database import data

def get_deadliness():
	countries = data.groupby('country_txt').groups
	l = []
	for (k,v) in countries.iteritems():
	    av_kills = d.loc[v]['nkill'].mean()
	    l.append((k,av_kills,len(v)))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	return l

if __name__=="__main__":
	print(get_deadliness())