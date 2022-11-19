#'''
#A01610903 José Rodrigo Hernández
#'''
#INSTRUCCIONES
#'''
#Construir la estructura  básica de una aplicación web que
#contenga una sección principal y además un apartado denominado barra
#lateral, el cual contendrá algunos controles para que se pueda manipular
#los datos sobre el proyecto de visualización de analítica de datos para
#WalMart USA.
#En el siguiente enlace podrás encontrar el enlace al conjunto de datos
#que pertencen a WaltMart USA.

#'''

#CODIGO ------------------------------------
#'''Librerias'''
import streamlit as st
import pandas as pd

#'''DataSet WalMart'''
dset_rute = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data_WalM = pd.read_csv(dset_rute)
data_vis = data_WalM.copy()

#Basicos
apptitle = 'Visualización de datos WalMart USA'
descrip = 'En esta WebApp se podrá visualizar datos sobre WalMart USA. Con el objetivo de visualizar y controlar los datos motrados de forma dinámica utilizando Streamlit.'
sidebar = st.sidebar

@st.cache
def showDataset(data):
    return st.dataframe(data)

#'''Web'''
st.title(apptitle)
st.header(descrip)
st.markdown('___')

#'''Sidebar'''
sidebar.title('Controles')
sidebar.write('En esta sección se encuentran los controles para visualizar el dataset')

sidebar.header('Controles Select box')
slec_Us= sidebar.selectbox('Modo de envio:', data_vis['Ship Mode'].unique())
data_vis = data_WalM[(data_WalM['Ship Mode']==slec_Us)]
sidebar.markdown('___')

sidebar.header('Controles checkbox')
if sidebar.checkbox('Visualizar Dataset?'):
    showDataset(data_vis)

sidebar.markdown('___')

#'''ShowDataset'''


