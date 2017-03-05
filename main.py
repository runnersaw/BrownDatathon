
from database import data
from utils import *

if __name__=="__main__":
	print(get_country_code('united states'))
	lat, lon = get_group_location(data, 'Abkhazian Separatists')
	print(lat, lon)
	print(get_country_from_location(lat, lon))

