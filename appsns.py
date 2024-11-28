import streamlit as st
import pandas as pd
from datetime import date
from datetime import time
import seaborn as sns
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Manipulation de données et création graphiques")

dataset = sns.get_dataset_names()
selection = st.selectbox("Choisissez votre dataset :", dataset)
dataset = sns.load_dataset(selection)
st.write(f"Affichage des premières lignes du dataset {selection}:")
st.write(dataset.head())
colonnes = dataset.select_dtypes(include=np.number).columns
if len(colonnes) >= 2:
    x = st.selectbox("Choisissez la colonne pour l'axe X :", colonnes)
    y = st.selectbox("Choisissez la colonne pour l'axe Y :", colonnes)
else:
    st.write("Visualisation impossible car pas assez de colonnes numériques")
selectgraph = st.selectbox("Choisissez votre dataset :", ["scatter_chart", "line_chart","bar_chart"])
if selectgraph:
    if "scatter_chart" in selectgraph:
        fig2 = px.scatter(dataset,x=x,y=y)
        st.plotly_chart(fig2)
    elif "line_chart" in selectgraph:
        fig2=px.line(dataset, x=x, y=y)
        st.plotly_chart(fig2)
    elif "bar_chart" in selectgraph:
        fig2=px.bar(dataset,x=x, y=y,)
        st.plotly_chart(fig2)

afficheok=st.checkbox("afficher la matrice de corrélation")
if afficheok:
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(dataset[dataset.select_dtypes(["number"]).columns].corr(), annot=True, cmap='magma')
    st.write('Matrice de corrélation')
    st.pyplot(fig)
