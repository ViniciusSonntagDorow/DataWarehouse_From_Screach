import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import streamlit as st

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

def get_data():
    query = """
        SELECT *
        FROM public.dm_commodities
    """

    df = pd.read_sql(query, engine)
    return df

st.set_page_config(page_title='Transactions Dashboard', layout='wide')

st.title('Transactions Dashboard')

st.write("""
This dashboard shows the transaction data from CL=F, GC=F and Sl=F commodities
""")

df = get_data()

st.dataframe(df)

st.bar_chart(df, x='symbol', y='value', x_label='symbol', y_label='value', color='profit', )