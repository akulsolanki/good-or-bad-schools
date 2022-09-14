import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from pandas.io.html import read_html

#url = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey'

#data = pd.read_html(url, attrs= {'class': 'wikitable sortable'})

#nj_cities_table = data[0]
#nj_cities = nj_cities_table['Municipality']

path = '/Users/rishabsolanki09@gmail.com/Downloads/Sale_Prices_City.csv'
all_cities = pd.read_csv(path)
nj_data = pd.DataFrame()
nj_cities = pd.Series()
medianPriceList = pd.Series()

i = 0
while i < len(all_cities['RegionID']):
    if all_cities['StateName'][i] != 'New Jersey':
        nj_cities.append(([all_cities['RegionName'][i]]))
        medianPriceList.append([all_cities['2019-07'][i]])

    i += 1

#nj_cities.insert(0, 'Median Home Price (07-2019)', medianPriceList, True)
#nj_data.append(nj_cities, ignore_index= True)

print(nj_cities)
#print(all_cities)
#print(all_cities['StateName'][0])


#for city in nj_cities:
 #   APIurl = 'https://api.greatschools.org/search/schools?key=[yourAPIKey]&state=NJ&q=' + city
