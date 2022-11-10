import streamlit as st
import pandas as pd
import numpy as np


nrow = 10000
nameL = 'https://raw.githubusercontent.com/NeusAiriGit/streamlit_lab/2ce36a1deaaa3962cb3b79f89b8c4553d69ab1dc/dataset.csv?token=GHSAT0AAAAAAB2XY6OHRP6XGESNPLKCMCKMY3NHVDA'



'''Funciones'''
@st.cache
def load_data(nameL,nrow,name_input):
    df = pd.read_csv(nameL,nrows=nrow)
    filtereddata = df.where(df['name'] == name_input)
    return filtereddata




st.title('Buscar nombres')
name_input = st.text_input('Nombre a buscar: ')
if name_input:
    loadinms = st.text('Cargando datos...')
    df = load_data(nameL,nrow,name_input)
    nameF = df.shape[0]
    loadinms.text(str(nrow) + ' Datos cargados')
    st.write(f'Se encontró {name_input} un total de: {nameF}')



