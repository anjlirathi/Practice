python -m pip install {BeautifulSoup}
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
Soup = BeautifulSoup(page.text, 'html')
print(Soup)
