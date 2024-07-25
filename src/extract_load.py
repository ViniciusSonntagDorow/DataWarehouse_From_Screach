import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

commodities = ['CL=F', 'GC=F', 'SI=F']

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

if __name__ == '__main__':
    concat_data = get_all_commodities_data(commodities=commodities)
    concat_data