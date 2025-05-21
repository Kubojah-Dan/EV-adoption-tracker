import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from Google Cloud Storage
@st.cache
def load_data():
    ev_sales = pd.read_csv('https://storage.googleapis.com/ev-adoption-data/ev_sales.csv')
    charging_stations = pd.read_csv('https://storage.googleapis.com/ev-adoption-data/charging_stations.csv')
    regional_registrations = pd.read_csv('https://storage.googleapis.com/ev-adoption-data/regional_registrations.csv')
    return ev_sales, charging_stations, regional_registrations

ev_sales, charging_stations, regional_registrations = load_data()

st.title("Electric Vehicle Adoption Tracker")

# Line Plot: EV Growth Trend
st.subheader("EV Registrations Over Years")
fig1 = px.line(ev_sales, x='Year', y='Total_Registrations', title='Yearly EV Registrations')
st.plotly_chart(fig1)

# Bar Plot: Charging Stations by City
st.subheader("Charging Stations by City")
fig2 = px.bar(charging_stations, x='City', y='Number_of_Stations', title='Charging Stations per City')
st.plotly_chart(fig2)

# Heatmap: Registrations by Region
st.subheader("Registrations by Region")
fig3 = px.density_heatmap(regional_registrations, x='Region', y='Registrations', title='Regional EV Registrations')
st.plotly_chart(fig3)
