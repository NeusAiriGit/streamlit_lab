import streamlit as st
import pandas as pd

DataUrl = 'uber-raw-data-sep14.csv'
dateColum = 'Date/Time'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DataUrl,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[dateColum] = pd.to_datetime(data[dateColum])
    data.rename(lowercase,axis='columns',inplace=True)
    return data
    

data = load_data(100)
st.dataframe(data)
st.map(data)
