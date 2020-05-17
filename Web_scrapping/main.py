##for web scrapping we need install request,beautifulsoup and pandas library
##for web scrapping we need install request,beautifulsoup and pandas library
import pandas as pd ##for making csv file
import requests 
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XsGXbRZE1uQ') ##link to web page
soup =BeautifulSoup(page.content,'html.parser') ##whole source code of page
##print(soup)
week= soup.find(id='seven-day-forecast-body') ##finding the posistion of data which we should aquire
##print(week)

items=week.find_all(class_='tombstone-container') ##will show the fukll list of items(in our case weather from mon-sund)
#print(items[0]) #print 0th posisiton data

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names =[item.find(class_='period-name').get_text()  for item in items] ##looping through item to find only the period name
short_descriptions=[item.find(class_='short-desc').get_text()  for item in items]##looping through item to find only the  short-descri.
temperatures=[item.find(class_='temp').get_text()  for item in items]##looping through item to find only the tempersture

#print(period_names)
#print(short_descriptions)
#print(temperatures)

weather_stuff =pd.DataFrame({'period':period_names, 'short_descriptions': short_descriptions, 'temperatures':temperatures,}) #making the purticular order with rows and cols

print(weather_stuff)
weather_stuff.to_csv('weather.csv') ##making the csv file(after making csv dowload the folder from repl to view as spreadsheet)
)
