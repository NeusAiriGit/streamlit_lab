import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


titdat = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
dat_tit = pd.read_csv(titdat)

fig, ax = plt.subplots()
ax.hist(dat_tit.fare)
st.header('Histiograma')
st.pyplot(fig)
st.markdown('___')

fig3, ax3 = plt.subplots()
ax3.scatter(dat_tit.age,dat_tit.fare)
ax3.set_xlabel('Edad')
ax3.set_ylabel('Fare')
st.pyplot(fig3)
st.markdown('___')

map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[25.67507, -100.31847],
    columns=['lat','lon']

)
st.dataframe(map_data)
st.map(map_data)