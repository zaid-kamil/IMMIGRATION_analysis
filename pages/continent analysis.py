import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


years = list(range(1980, 2014))

@st.cache_data()
def load_data():
    df = pd.read_excel('data/Canada.xlsx', sheet_name=1, skiprows=20, skipfooter=2) 
    # add a column
    df['Total'] = df[years].sum(axis=1)
    # remove unnecessary columns
    cols_to_drop = ['AREA', 'REG', 'DEV', 'Type', 'Coverage',]
    df.drop(columns=cols_to_drop, inplace=True)
    # rename columns
    df.rename(columns={
        'OdName': 'Country',
        'AreaName': 'Continent',
        'RegName': 'Region',
        'DevName':'Status',
    }, inplace=True)
    # sort values by total
    df.sort_values(by='Total', ascending=False, inplace=True)
    # set index to country
    df.set_index('Country', inplace=True)
    cdf = df.groupby('Continent')[years].sum()
    return cdf

with st.spinner('Loading data...'):
    df = load_data()

st.dataframe(df)