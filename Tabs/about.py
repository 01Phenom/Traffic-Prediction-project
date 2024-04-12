"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.snow()
    st.title('Design Thinking and Innovation')
    
    st.markdown('''Project: iTraffic Harmony''')
    image = Image.open('./images/icon.jpg')
    st.image(image)
    
    
    
