import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import sys
import json
from pathlib import Path
import pandas as pd
import numpy as np

from utils import read_data, set_font, set_text, show_map_circle, show_map_marker

st.set_page_config(layout="wide")
# st.write(set_font(), unsafe_allow_html=True)

filepath = 'philippines.geojson'

data = read_data(filepath)

st.markdown(set_text('30-day Map Challenge: Day 1','h1'),unsafe_allow_html=True)

intro_text = '''The first day of the challenge is all about points.
The dataset I am working with is a geojson file from [https://data.humdata.org/dataset/philippines-healthsites](https://data.humdata.org/dataset/philippines-healthsites).
It contains different health realted facilities in the Philippines. For the purpose of this exercise, I only took the hospitals.
'''
geopandas_text = '''[GeoPandas](https://geopandas.org/en/stable/) is a python library that can read geojson files and output it in a dataframe - a format that most data scientists and data analysts are familiar with.
As written in the documentation, the library extends the data types used by pandas to allow spatial operations on geometric types. A geojson file will contain a geometry which contains features like points, lines, and polygons.
Since we are interested in points for this exercise, we'll be using this library to extract the points from the geometry.
'''
folium_text = '''[Folium](https://python-visualization.github.io/folium/latest/) is a library that builds on top of leaflet.js library and can be used for geospatial data manipulated in python to create interactive web maps.

For this exercise, I've used the function folium.Marker() to map the hospitals using icons. The icons are customizable - you can change the icons itself and the color. I've also used another function, folium.Circle(), that uses circles to map the points in the map.
'''
st.markdown(intro_text)
st.markdown(set_text('Using geopandas to read a geojson file','h3'),unsafe_allow_html=True)
st.markdown(geopandas_text)
st.markdown(set_text('Using folium for the map','h3'),unsafe_allow_html=True)
st.markdown(folium_text)

st.markdown(set_text('Hospitals in the Philippines','h3'),unsafe_allow_html=True)
map_marker = show_map_marker(data)
map_circle = show_map_circle(data)

col1, col2= st.columns(2)
with col1:
    folium_static(map_marker, height=500, width=600)

with col2:
    folium_static(map_circle, height=500, width=600)