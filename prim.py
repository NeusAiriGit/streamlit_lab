import streamlit as st
import pandas as pd


nrow = 100

nameL = 'dataset.csv'
st.title('Read csv')



loadinms = st.text('Loading data...')

@st.cache
def load_data(nameL,nrow):
    df = pd.read_csv(nameL,nrows=nrow)
    return df


df = load_data(nameL,nrow)

loadinms.text('Done reading ' + str(nrow) + ' rows')
st.dataframe(df)
