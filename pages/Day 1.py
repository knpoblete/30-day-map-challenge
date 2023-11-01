import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import sys
import json
from pathlib import Path
import pandas as pd
import numpy as np

from utils import read_data, set_font, show_map

st.set_page_config(layout="wide")
# st.write(set_font(), unsafe_allow_html=True)

filepath = 'philippines.geojson'

data = read_data(filepath)

st.markdown(set_font('30-day Map Challenge: Day 1','h1'),unsafe_allow_html=True)
st.write('The first day of the challenge is all about points.')
st.write('I used a dataset from: [https://data.humdata.org/dataset/philippines-healthsites](https://data.humdata.org/dataset/philippines-healthsites). This dataset has all health related facilities but I only got the hospitals for this exercise.')
st.write('Key learnings include: loading a geojson file, extracting centroids, visualizing using Folium library, loading my own mapbox style, and adding some icon customizations.')

st.markdown(set_font('Hospitals in the Philippines','h3'),unsafe_allow_html=True)
map = show_map(data)
folium_static(map, height=800, width=1200)