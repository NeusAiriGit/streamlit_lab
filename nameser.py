import streamlit as st
import pandas as pd
import numpy as np


nrow = 10000
nameL = 'dataset.csv'



'''Funciones'''
@st.cache
def load_data(nameL,nrow,name_input):
    df = pd.read_csv(nameL,nrows=nrow)
    filtereddata =df[df['name'].str.contains(name_input)]

    return filtereddata




st.title('Buscar nombres')
name_input = st.text_input('Nombre a buscar: ')
if st.button('Buscar'):
    loadinms = st.text('Cargando datos...')
    df = load_data(nameL,nrow,name_input)
    nameF = df.shape[0]
    loadinms.text(str(nrow) + ' Datos cargados')
    st.dataframe(df)
    st.write(f'Se encontró {name_input} un total de: {nameF} veces')



