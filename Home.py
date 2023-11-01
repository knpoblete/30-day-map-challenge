import streamlit as st
from utils import set_font, set_text
from PIL import Image


st.set_page_config(layout="wide")
st.markdown(set_text('30-day Map Challenge','h1'),unsafe_allow_html=True)

st.markdown(set_text('Hello, I\'m Kath!','h2'),unsafe_allow_html=True)
st.write('I will be participating in the 30-day Map Challenge. Join me as I learn to make maps!')

st.write("Check out the challenge here: [https://30daymapchallenge.com/](https://30daymapchallenge.com/)")

image = Image.open('challenge.png')
st.image(image)
