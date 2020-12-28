#Web Scraping ODI Cricket Player Names from Wikipedia.

import requests
from bs4 import BeautifulSoup
import pandas as pd
page=requests.get("https://en.wikipedia.org/wiki/List_of_India_ODI_cricketers").text
#page
soup=BeautifulSoup(page,"lxml")
print(soup.prettify())
table=soup.find("table",{"class":"wikitable"})
data_rows = table.findAll('tr')[2:]
#type(data_rows)
player_names=[]
for i in data_rows:
    names=i.findAll("a")
    for x in names:
        player_names.append(x.get("title"))
print(player_names)
dataframe=pd.DataFrame()
dataframe['player_names']= Players
#dataframe.head()
dataframe.to_csv("Cricket_players.csv")
