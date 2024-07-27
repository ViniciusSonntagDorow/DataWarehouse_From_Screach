#Imports
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#Env Variables
load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

#Code itself

def get_commodities_data(symbol,period='5y',interval='1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period,interval=interval)[['Close']]
    data['Symbol'] = symbol
    return data

def get_all_commodities_data(commodities):
    all_data = []
    for symbol in commodities:
        data = get_commodities_data(symbol=symbol)
        all_data.append(data)
    return pd.concat(all_data)

def to_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

if __name__ == '__main__':
    concat_data = get_all_commodities_data(commodities=commodities)
    to_postgres(concat_data)