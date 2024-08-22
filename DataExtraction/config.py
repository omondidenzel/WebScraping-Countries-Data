from sqlalchemy import create_engine
import logging, sys

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

url = 'https://en.wikipedia.org/wiki/'

list_of_countries =  {
    'countries': ['Kenya', 'Rwanda', 'Uganda', 'Ethiopia', 'Ghana', 'Malawi', 'Israel', 'Japan', 'France', 'India', 'USA']                
}

def save_toDB():
    URL_DATABASE = 'postgresql://postgres:ya!e3ekafE@localhost:5450/denzel'
    return create_engine(URL_DATABASE)

engine = save_toDB() 