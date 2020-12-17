import requests
from bs4 import BeautifulSoup
from re import sub
import pandas as pd

# lists we want
titles = []
years = []
times = []
imdb_ratings = []
votes = []
metascores = []
reviews = []
critics = []
#popularitys = [] <- too many bugs
countrys = []
worldwide_grosses = []
movie_classes = []

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
    title = soup.find('h1').text.split('(')[0]
    titles.append(title)

    # store year
    year = soup.find('h1').text.split('(')[1].strip(' )')
    years.append(year)

    # store runtime
    time = soup.find_all('time')[1].text.split()[0]
    times.append(time)

    # store imdb ratings
    imdb_rating = soup.find('span', itemprop="ratingValue").text
    imdb_ratings.append(imdb_rating)

    # store votes
    vote = soup.find('span', itemprop="ratingCount").text
    votes.append(vote)

    # store metascores
    if soup.find('div', class_="metacriticScore") is not None:
        metascore = soup.find('div', class_="metacriticScore").contents
        metascore = sub(r"\D", "", str(metascore))
    else:
        metascore = None
    metascores.append(metascore)

    # store review number
    review = soup.find('a', href="reviews")
    review = sub(r"\D", "", str(review))
    reviews.append(review)

    # store critic number
    critic = soup.find('a', href="externalreviews")
    critic = sub(r"\D", "", str(critic))
    critics.append(critic)

    # store popularity
    #if len(soup.find_all('div', class_="titleReviewBarSubItem")) > 1:
    #    popularity = soup.find_all('div', class_="titleReviewBarSubItem")[2].span.text.split()[0]
    #elif soup.find('div', class_="titleReviewBarSubItem") is None:
    #    popularity = None
    #else:
    #    popularity = soup.find('div', class_="titleReviewBarSubItem").span.text.split()[0]
    #popularitys.append(popularity)

    # store country
    country = soup.find('h4', class_="inline", text="Country:").next_element.next_element.next_element.text
    countrys.append(country)

    # store worldwide gross
    if soup.find('h4', class_="inline", text="Cumulative Worldwide Gross:") is not None:
        wwg = soup.find('h4', class_="inline", text="Cumulative Worldwide Gross:").next_element.next_element.strip()
    else:
        wwg = None
    worldwide_grosses.append(wwg)

    # store movie ratings
    movie_class = soup.find('h4', class_="inline", text="Certificate:").next_element.next_element.next_element.text
    if len(movie_class) > 5:
        movie_class = None
    movie_classes.append(movie_class)

# create the dataset
movies = pd.DataFrame({'movie': titles,
                       'year': years,
                       'time_minute': times,
                       'imdb_rating': imdb_ratings,
                       'imdb_voters': votes,
                       'metascore': metascores,
                       'reviews': reviews,
                       'critics': critics,
                       #'popularity': popularitys,
                       'country':countrys,
                       'worldwide_gross': worldwide_grosses,
                       'movie_class': movie_classes})

movies.to_csv('imdb_top250')
