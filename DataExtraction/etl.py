# Import dependencies 
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import config

data_list = []

def get_data():
    for country in config.list_of_countries['countries']:
        # Define the URL
        url = f'{config.url}{country}'

        # Call the Apo
        fetch_page = requests.get(url)

        soup = BeautifulSoup(fetch_page.content, 'html.parser')

        data_dict = {}

        data_dict['Country'] = soup.css.select('.fn.org.country-name')[0].get_text()
        data_dict['Latitude'] = soup.css.select('.latitude')[0].get_text()
        data_dict['Longitude'] = soup.css.select('.longitude')[0].get_text()
        # data_dict['National_Language'] = soup.css.select('.infobox-data')[0].get_text()

        data_list.append(data_dict)
        
        # create empty DataFrame 
        df = pd.DataFrame(data_list)

        df.columns = df.columns.str.lower()


    print(df.head())

get_data()