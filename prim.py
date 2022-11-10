import streamlit as st
import pandas as pd


nrow = 100

nameL = 'https://raw.githubusercontent.com/NeusAiriGit/streamlit_lab/2ce36a1deaaa3962cb3b79f89b8c4553d69ab1dc/dataset.csv?token=GHSAT0AAAAAAB2XY6OHRP6XGESNPLKCMCKMY3NHVDA'
st.title('Read csv')



loadinms = st.text('Loading data...')

@st.cache
def load_data(nameL,nrow):
    df = pd.read_csv(nameL,nrows=nrow)
    return df


df = load_data(nameL,nrow)

loadinms.text('Done reading ' + str(nrow) + ' rows')
st.dataframe(df)
