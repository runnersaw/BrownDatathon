
import pandas as pd
from database import data

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