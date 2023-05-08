import numpy as np
import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Fonction de Syracuse", layout="wide")

collatz_number = st.number_input('Collatz', step=1)

n = int(collatz_number)

liste = []
if n!=0:
    while n!=1:
        if n%2 == 0:
            n = n//2
            liste.append(n)
        else:
            n=3*n+1
            liste.append(n)

a = len(liste)

liste_2 = []
for i in range (1, a+1): 
    liste_2.append(i)

list(zip(liste_2, liste))

df = pd.DataFrame(list(zip(liste_2, liste)), columns=['Pas de Syracuse', 'collatz'])

fig = px.line(df, x= 'Pas de Syracuse', y='collatz')

st.plotly_chart(fig)