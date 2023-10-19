"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.snow()
    st.title('Data Mining Project')
    st.markdown('''### SLIIT CODERS''')
    st.markdown('''Passionate Engineer and Rational Thinker. Data Scientist, Web Developer''')
    image = Image.open('./images/icon.jpg')
    st.image(image)
    
    st.markdown('''### GitHub: [Group 24](https://github.com/IT21365232/Traffic-Prediction-project.git)''')
    
