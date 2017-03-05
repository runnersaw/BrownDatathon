
import pandas as pd

data = pd.read_csv('globalterrorismdb_0616dist.csv', dtype={'approxdate':str,'gsubname2':str,'gname3':str,'gsubname3':str,'divert':str,'kidhijcountry':str,'ransomnote':str})
data = data.loc[data['iyear'] >= 1996]
