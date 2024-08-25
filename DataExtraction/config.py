from sqlalchemy import create_engine
import logging, sys, os
from dotenv import load_dotenv, find_dotenv # to load and reload env incase of cred change

load_dotenv(find_dotenv())

db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

url = 'https://en.wikipedia.org/wiki/'

list_of_countries =  {
    'countries': ['Kenya', 'Rwanda', 'Uganda', 'Ethiopia', 'Ghana', 'Malawi', 'Israel', 'Japan', 'France', 'India', 'USA']                
}

def save_toDB():
    URL_DATABASE = 'postgresql://denzel_admin:{}@futurekwany.cbeyew4isf50.us-east-1.rds.amazonaws.com:5432/{}'.format(db_password, db_name)
    return create_engine(URL_DATABASE)

engine = save_toDB() 