# Import dependencies 
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import config

url = f'{config.url}{config.list_of_countries['countries'][0]}'

fetch_page = requests.get(url)

soup = BeautifulSoup(fetch_page.content, 'html.parser')

print(soup.prettify())