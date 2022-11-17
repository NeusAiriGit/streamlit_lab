import streamlit as st
import pandas as pd
import numpy as np


st.title('Streamlit con Sidebar')
st.header('Header de la app')




sidebar = st.sidebar
sidebar.title('Titulo de barra lateral')
sidebar.write('Info del sidebar')

if sidebar.checkbox('Show df'):
    chart_data= pd.DataFrame(np.random.randn(20,3)
    ,columns=['a','b','c'])

    st.dataframe(chart_data)

