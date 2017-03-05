
import pandas as pd
from database import data

def get_targets():
	countries = data.groupby('country_txt').groups
	groups = {k:len(v) for (k,v) in countries.iteritems()}
	l = []
	for (k,v) in groups.iteritems():
		l.append((k,v))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	return l

if __name__=="__main__":
	print(get_targets())