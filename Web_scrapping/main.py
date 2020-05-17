##for web scrapping we need install request,beautifulsoup and pandas library
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XsGXbRZE1uQ') ##link to web page
soup =BeautifulSoup(page.content,'html.parser') ##whole source code of page
##print(soup)
week= soup.find(id='seven-day-forecast-body') ##finding the posistion of data which we should aquire
print(week)
