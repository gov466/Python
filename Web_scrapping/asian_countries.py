##for web scrapping we need install request,beautifulsoup and pandas library
##for web scrapping we need install request,import pandas as pd ##for making csv file
import requests 
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area') ##link to web page
soup =BeautifulSoup(page.content,'html.parser') ##whole source code of page
#print(soup.prettify())

#week= soup.find(id='wikitable sortable jquery-tablesorter') ##finding the posistion of data which we should aquire
all_link=soup.find_all("a")
for link in all_link:
  print(link.get('href'))
all_tables= soup.find_all('table')
#print(all_tables)
all_link=soup.find_all("a")
#for link in all_link:
#  print(link.get('href'))
#print(soup.title.string) ##ge
right_table=soup.find('table',class_='wikitable sortable')
print(right_table)

table_links= right_table.find_all('a')
print(table_links)

country=[]
for links in table_links:
  country.append(links.get('title'))
print(country)

df=pd.DataFrame()
df['country']=country
print(df)

df.to_csv('df.csv')
