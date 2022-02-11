import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data

#import cities in US and their Lat/Long
cities = pd.read_excel('uscities.xlsx')
#import recorded visited cities
visited = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTDYgt8M7tHR2wJdSet4RwPgy7ZCoV_BRw4FzTc9Oylp-AYolOUITaG21YOFpTefSyib3lPgKuCD0h9/pub?gid=1065799884&single=true&output=csv')

#clean visited cities data
visited['city'] = visited['What City did you visit?']
visited['state_id'] = visited['What State is it in?']

#clean cities information data
citiesfiltered = cities[["city","state_id", "lat", "lng"]]

#combine useful data
final = pd.merge(visited, citiesfiltered)

states = alt.topo_feature(data.us_10m.url, feature='states')
points = alt.Chart(final).mark_circle().encode(
    longitude='lng',
    latitude='lat',
    size=alt.value(25),
    tooltip='city'
)
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa').properties(
    width=1000,
    height=600
)

st.header("The Map:")
st.write(background + points)

st.header("The list of Cities:")
st.write(visited)
