
import pandas as pd

data = pd.read_csv('gtd98_now.csv', dtype={'approxdate':str,'gsubname2':str,'gname3':str,'gsubname3':str,'divert':str,'kidhijcountry':str,'ransomnote':str})
polity_data = pd.read_csv('p4v2015.csv')
