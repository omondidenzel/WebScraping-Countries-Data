# Import dependencies 
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import config
import sys
import logging 

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


data_list = []

def get_data():
    for country in config.list_of_countries['countries']:
        # Define the URL
        url = f'{config.url}{country}'
        log.info("Extracting -> {}".format(url))

        # Call the Api
        try:
            fetch_page = requests.get(url)
        except Exception as e:
            log.info('Error --> {}'.format(e))
            
        if fetch_page.status_code == 200:
            soup = BeautifulSoup(fetch_page.content, 'html.parser')

            data_dict = {}

            data_dict['Country'] = soup.css.select('.fn.org.country-name')[0].get_text()
            data_dict['Latitude'] = soup.css.select('.latitude')[0].get_text()
            data_dict['Longitude'] = soup.css.select('.longitude')[0].get_text()

            find_td_element = soup.find('td', class_='infobox-data')
            data_dict['Capital'] = find_td_element.find('a').text

            rows = soup.find_all('tr')
            populatiom_estimate = rows[32].find_all('td', class_='infobox-data')
            # gdp_estimate = rows[36].find_all('td', class_='infobox-data')

            for x in populatiom_estimate:
                data_dict['populatiom_estimate'] = x.text

            data_list.append(data_dict)
            
            # create empty DataFrame 
            df = pd.DataFrame(data_list)

            # Transformation
            def removeSymbolsNumber(data_symbol):
                data_symbol = re.sub(r'\[\d+\]', '', data_symbol)
                return data_symbol 
            
            def removeNumericalValue(data_numerical):
                data_numerical = re.sub('[^A-Za-z]+', ' ', data_numerical)
                return data_numerical 
            
            df.columns = df.columns.str.lower()
            df['country'] = df['country'].apply(removeSymbolsNumber)
            df['capital'] = df['capital'].apply(removeNumericalValue)

    # print(df.head(20))

    # Load to DB
    log.info(f'Load data to database')
    try:
        with config.engine.connect() as conn:
            df.to_sql('country_record', con=conn, if_exists='replace', index=False)
            log.info(f'Data loaded to database ->> ({df.shape[0]} rows and {df.shape[1]} columns; {list(df.columns)}).')
            
            log.info('Attempting to close DB connection')
            conn.close()
            log.info('DB connection closed')
    except Exception as e:
        log.info(f'Error -> '.format(e))
            
get_data()