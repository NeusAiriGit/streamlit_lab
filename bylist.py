import streamlit as st
import pandas as pd

nameL = 'dataset.csv'
df = pd.read_csv(nameL)

st.title('Buscar por indices')


@st.cache
def load_data(nameL,gender):
    df = nameL
    filtereddata =df[df['sex']  == gender]

    return filtereddata


selected_sex = st.selectbox('Genero a filtrar: ', df['sex'].unique())

if st.button('Filtrar por Genero'):

    loadinms = st.text('Cargando datos...')
    df = load_data(df ,selected_sex)
    nameF = df.shape[0]
    loadinms.text('Datos cargados')
    st.dataframe(df)
    st.write(f'Se registran : {nameF}  de personas con el genero {selected_sex}')