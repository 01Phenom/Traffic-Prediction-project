"""This module contains data about prediction page"""

# Import necessary modules
import streamlit as st
from web_functions import predict  # Import necessary functions from web_functions

def app(df, X, y, data1):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> to predict traffic.
            </p>
        """, unsafe_allow_html=True)
    
    option = st.selectbox(
        "How would you like to enter data?",
        ("Slider", "Text Box"),
        index=None,
        placeholder="Select contact method..."
    )

    if option == "Slider":
        st.write('You selected:', option)
        
        # Take feature input from the user
        # Add a subheader
        st.subheader("Select Values:")

        # Take input of features from the user.
        ag = st.slider("temperature", float(df["temperature"].min()), float(df["temperature"].max()))
        bp = st.slider("weekday", int(df["weekday"].min()), int(df["weekday"].max()))
        sth = st.slider("hour", int(df["hour"].min()), int(df["hour"].max()))
        insulin = st.slider("month_day", int(df["month_day"].min()), int(df["month_day"].max()))
        bmi = st.slider("year", int(df["year"].min()), 2023)
        gc = st.slider("month", int(df["month"].min()), int(df["month"].max()))

        fg = st.selectbox("Holiday",("Yes", "No"), index=None, placeholder="Is today a holiday? ")

        hd = holiday_to_number(fg)
        
        age = st.selectbox("Weather type",("Rain", "Clouds", "Clear", "Snow", "Mist","Drizzle", "Haze", "Thunderstorm", "Fog", "Smoke", "Squall"), index=None, placeholder="What is the weather like?")
        w_type_number = Weather_type_to_number(age)
        
        wd_dec = st.selectbox("Weather Description",("light rain", "few clouds", "Sky is Clear", "light snow", "sky is clear", "mist", "broken clouds", "moderate rain", "drizzle", "overcast clouds", "scattered clouds", "haze", "proximity thunderstorm", "light intensity drizzle", "heavy snow", "heavy intensity rain", "fog", "heavy intensity drizzle", "shower snow", "snow", "thunderstorm with rain",
              "thunderstorm with heavy rain", "thunderstorm with light rain", "proximity thunderstorm with rain", "thunderstorm with drizzle", "smoke", "thunderstorm", "proximity shower rain", "very heavy rain", "proximity thunderstorm with drizzle", "light rain and snow", "light intensity shower rain", "SQUALLS", "shower drizzle", "thunderstorm with light drizzle"), index=None, placeholder="What is the weather description?")
        wD_type_number = Weather_des_to_number(wd_dec)
        
        features = [hd, ag, bp, sth, insulin, bmi, gc, w_type_number, wD_type_number]

    if option == "Text Box":
        fg = st.selectbox("Holiday",("Yes", "No"), index=None, placeholder="Is today a holiday? ")
        hd = holiday_to_number(fg)

        ag = st.text_input("Temperature", placeholder="Today's temperature?", max_chars=6, key=int)
        bp = st.selectbox("Day",("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"), index=None, placeholder="What day is it?")
        day_number = day_name_to_number(bp)
        
        sth = st.text_input("Hour", placeholder="What is the hour?")
        insulin = st.text_input("Month day", placeholder="What is the month day?")
        gc = st.text_input("Month", placeholder="What is the month?")
        bmi = st.text_input("Year", placeholder="What is the year?", max_chars=4)
        
        age = st.selectbox("Weather type",("Rain", "Clouds", "Clear", "Snow", "Mist","Drizzle", "Haze", "Thunderstorm", "Fog", "Smoke", "Squall"), index=None, placeholder="What is the weather like?")
        w_type_number = Weather_type_to_number(age)
        
        wd_dec = st.selectbox("Weather Description",("light rain", "few clouds", "Sky is Clear", "light snow", "sky is clear", "mist", "broken clouds", "moderate rain", "drizzle", "overcast clouds", "scattered clouds", "haze", "proximity thunderstorm", "light intensity drizzle", "heavy snow", "heavy intensity rain", "fog", "heavy intensity drizzle", "shower snow", "snow", "thunderstorm with rain",
              "thunderstorm with heavy rain", "thunderstorm with light rain", "proximity thunderstorm with rain", "thunderstorm with drizzle", "smoke", "thunderstorm", "proximity shower rain", "very heavy rain", "proximity thunderstorm with drizzle", "light rain and snow", "light intensity shower rain", "SQUALLS", "shower drizzle", "thunderstorm with light drizzle"), index=None, placeholder="What is the weather description?")
        wD_type_number = Weather_des_to_number(wd_dec)
        
        features = [hd, ag, day_number, sth, insulin, bmi, gc, w_type_number, wD_type_number]
        
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.write(prediction)
