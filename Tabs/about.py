"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.snow()
    st.title('Data Mining Project')
    
    st.markdown(''' Data Scientist Project''')
    image = Image.open('./images/icon.jpg')
    st.image(image)
    
    
    
