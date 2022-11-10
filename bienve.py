import streamlit as st

def bienvenida(nombre):
    mensa = 'Bienvenid@ ' + str(nombre)
    return mensa

myname = st.text_input('Nombre: ')
if myname:
    mensaje = bienvenida(myname)
    st.write(': {mensaje}')