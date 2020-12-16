import requests
import datetime
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import numpy as np

# lists we want
titles = []
years = []
time = []
imdb_ratings = []
audience_rating = []
metascores = []
votes = []
reviews = []
popularity = []
countrys = []
worldwide_gross = []

# store urls of each movie
page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(page.text, 'html.parser')
urls = []

for link in soup.find_all('a'):
    if link.get('href') is not None and '/title/tt' in link.get('href') and link.get('href') not in urls:
        urls.append(link.get('href'))

# store data from each link
for url in urls:
    page = requests.get('https://www.imdb.com/' + url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # store title
    titles.append()

#sleep(randint(2,10))
print(titles)
print(years)