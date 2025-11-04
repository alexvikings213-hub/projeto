import streamlit as st
import pandas as pd
import plotly.express as px

# --- Leitura dos dados ---
car_data = pd.read_csv('vehicles.csv') 

# --- Cabeçalho do aplicativo ---
st.header('Dashboard de Anúncios de Vendas de Carros')

# --- Texto descritivo ---
st.write('Explore os dados de veículos usados e visualize diferentes distribuições.')

# --- Botão para criar histograma ---
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a coluna "odometer" (quilometragem).')
    fig = px.histogram(car_data, x='odometer', nbins=30, title='Distribuição da Quilometragem dos Carros')
    st.plotly_chart(fig, use_container_width=True)

# --- Botão para criar gráfico de dispersão ---
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: preço x quilometragem.')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relação entre Preço e Quilometragem')
    st.plotly_chart(fig, use_container_width=True)
