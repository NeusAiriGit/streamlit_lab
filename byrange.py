import streamlit as st
import pandas as pd

nameL = 'dataset.csv'

'''Funciones'''
@st.cache
def load_data(nameL,id_ini,id_fin):
    df = pd.read_csv(nameL)
    filtereddata =df[(df['index'] >= id_ini) & (df['index'] <= id_fin) ]

    return filtereddata

st.title('Buscar por indices')
id_ini = st.text_input('Indice inicial: ')
id_fin = st.text_input('Indice fianl: ')

if st.button('Buscar'):

    loadinms = st.text('Cargando datos...')
    df = load_data(nameL,int(id_ini),int(id_fin))
    nameF = df.shape[0]
    loadinms.text('Datos cargados')
    st.dataframe(df)
    st.write(f'Se muestran : {nameF} entradas')
