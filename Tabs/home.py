"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st
from PIL import Image

def app():
    """This function create the home page"""
    
    # Add title to the home page
    image = Image.open('./images/home.jpeg')
    st.title(":blue[Traffic Prediction] System")

    # Add image to the home page
    st.image(image)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Today, the city is facing a pressing traffic problem. Our roads are swamped with vehicles, causing frustrating delays for commuters and a surge in road rage incidents. Traffic jams have become an everyday ordeal, extending rush hours and making daily travel a daunting task. This gridlock not only wastes time but also contributes to increased pollution and fuel consumption. Local authorities are actively seeking solutions, such as expanding public transportation, optimizing traffic signals, and promoting carpooling and cycling. Resolving this traffic crisis is paramount for the city's well-being, the environment, and the sanity of its residents.
        </p>
        <br>
        <p style="font-size:20px;">
            To avoid the time consuming on road we create a traffic prediction using <b style="color:blue">Random Forest Classifier</b> predict the traffic is high or not a particular day.
        </p>

    """, unsafe_allow_html=True)
