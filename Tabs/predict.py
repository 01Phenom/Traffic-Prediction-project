"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st


# Import necessary functions from web_functions
from web_functions import predict




# <style>
# body {
#   background-image: url('img_girl.jpg');
#   background-repeat: no-repeat;
#   background-attachment: fixed; 
#   background-size: 100% 100%;
# }
# </style>


def app(df, X, y,data1):
    """This function create the prediction page"""


    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for Predict the traffic
            </p>
        """, unsafe_allow_html=True)
    
    

    option = st.selectbox(
    "How would you like to be enter data ? ",
    ("Slider", "Text Box"),
    index=None,
    placeholder="Select contact method...",
    )

    if (option == "Slider"):

        st.write('You selected:', option)
        
        # Take feature input from the user
        # Add a subheader
        st.subheader("Select Values:")

        # Take input of features from the user.
        ag = st.slider("temperature", float(df["temperature"].min()), float(df["temperature"].max()))
        bp = st.slider("weekday", int(df["weekday"].min()), int(df["weekday"].max()))
        sth = st.slider("hour", int(df["hour"].min()), int(df["hour"].max()))
        insulin = st.slider("month_day 	", int(df["month_day"].min()), int(df["month_day"].max()))
        bmi = st.slider("year", int(df["year"].min()), 2023)
        gc = st.slider("month", int(df["month"].min()), int(df["month"].max()))

        fg = st.selectbox("Holiday",("Yes", "No"),index=None,placeholder="Is today is holiday ? ")

        def holiday_to_number(status):
            # Define a dictionary to map day names to numbers
            H_status = {
                "No":0,
                "Yes":1
            }

            # Check if the input day name is in the dictionary
            if status in H_status:
                return H_status[status]
            else:
                return None

        # Example usage:
        hd = holiday_to_number(fg)
        

        age = st.selectbox("Weather type",("Rain", "Clouds", "Clear", "Snow", "Mist","Drizzle", "Haze", "Thunderstorm", "Fog", "Smoke", "Squall"),index=None,placeholder=" How is the weather ? ")
        def Weather_type_to_number(weather_type):
            # Define a dictionary to map day names to numbers
            w_type = {
                "Rain":1, "Clouds":2, "Clear":3, "Snow":4, "Mist":5,"Drizzle":6, "Haze":7, "Thunderstorm":8, "Fog":9, "Smoke":10, "Squall":11
                
            }

            # Check if the input day name is in the dictionary
            if weather_type in w_type:
                return w_type[weather_type]
            else:
                return None

        # Example usage:
        w_type_number = Weather_type_to_number(age)
        

        wd_dec = st.selectbox("Weather Description",("light rain", "few clouds", "Sky is Clear", "light snow", "sky is clear", "mist", "broken clouds", "moderate rain", "drizzle", "overcast clouds", "scattered clouds", "haze", "proximity thunderstorm", "light intensity drizzle", "heavy snow", "heavy intensity rain", "fog", "heavy intensity drizzle", "shower snow", "snow", "thunderstorm with rain",
              "thunderstorm with heavy rain", "thunderstorm with light rain", "proximity thunderstorm with rain", "thunderstorm with drizzle", "smoke", "thunderstorm", "proximity shower rain", "very heavy rain", "proximity thunderstorm with drizzle", "light rain and snow", "light intensity shower rain", "SQUALLS", "shower drizzle", "thunderstorm with light drizzle"),index=None,placeholder="What is the weather description ? ")
        def Weather_des_to_number(weatherD_type):
            # Define a dictionary to map day names to numbers
            wD_type = {
                "light rain":1, "few clouds":2, "Sky is Clear":3, "light snow":4, "sky is clear":5, "mist":6, "broken clouds":7, "moderate rain":8,
                "drizzle":9, "overcast clouds":10, "scattered clouds":11, "haze":12, "proximity thunderstorm":13, "light intensity drizzle":14, "heavy snow":15, 
                "heavy intensity rain":16, "fog":17, "heavy intensity drizzle":18, "shower snow":19, "snow":20, "thunderstorm with rain":21,
              "thunderstorm with heavy rain":22, "thunderstorm with light rain":23, "proximity thunderstorm with rain":24, 
              "thunderstorm with drizzle":25, "smoke":26, "thunderstorm":27, "proximity shower rain":28, "very heavy rain":29, "proximity thunderstorm with drizzle":30, 
              "light rain and snow":31, "light intensity shower rain":32, "SQUALLS":33, "shower drizzle":34, "thunderstorm with light drizzle":35
                
            }

            # Check if the input day name is in the dictionary
            if weatherD_type in wD_type:
                return wD_type[weatherD_type]
            else:
                return None

        # Example usage:
        wD_type_number = Weather_des_to_number(wd_dec)
        
        

        # Create a list to store all the features
        features = [hd, ag, bp, sth, insulin, bmi, gc, w_type_number, wD_type_number]

    if (option == "Text Box"):

        fg = st.selectbox("Holiday",("Yes", "No"),index=None,placeholder="Is today is holiday ? ")

        def holiday_to_number(status):
            # Define a dictionary to map day names to numbers
            H_status = {
                "No":0,
                "Yes":1
            }

            # Check if the input day name is in the dictionary
            if status in H_status:
                return H_status[status]
            else:
                return None

        # Example usage:
        hd = holiday_to_number(fg)
        


        ag = st.text_input("Temperature",placeholder="Todays temperature ? ",max_chars=6,key=int)
        try:
            # Try to convert the user input to an integer
            integer_input = float(ag)

        except ValueError:
            # If not successful, display an error message
            st.error("Please enter a valid temperature.")


        bp = st.selectbox("Day",("Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"),index=None,placeholder="What is the day ? ")
        def day_name_to_number(day_name):
            # Define a dictionary to map day names to numbers
            days = {
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5,
                "Saturday": 6,
                "Sunday": 7
            }

            # Check if the input day name is in the dictionary
            if day_name in days:
                return days[day_name]
            else:
                return None

        # Example usage:
        day_number = day_name_to_number(bp)
        

        sth = st.text_input("Hour",placeholder="What is the Hour ? ")
        
        try:
            # Try to convert the user input to an integer
            integer_input = int(sth)
            if int(sth) > 24 or int(sth) <1:
                st.error("Please enter a valid hour between 1-24.")
            
        except ValueError:
            # If not successful, display an error message
            st.error("Please enter a valid integer.")

        insulin = st.text_input("Month day",placeholder="What is the month day ? ")

        try:
            # Try to convert the user input to an integer
            integer_input = int(insulin)
            if int(insulin) > 31 or int(insulin) <1:
                st.error("Please enter a valid day between 1-31.")
            
        except ValueError:
            # If not successful, display an error message
            st.error("Please enter a valid integer.")

        gc = st.text_input("Month",placeholder="What is the month ? ")
        try:
            # Try to convert the user input to an integer
            integer_input = int(gc)
            if int(gc) > 12 or int(gc) <1:
                st.error("Please enter a valid month between 1-12.")
            
        except ValueError:
            # If not successful, display an error message
            st.error("Please enter a valid integer.")

        
        bmi = st.text_input("Year",placeholder="What is Year ? ",max_chars=4)
        try:
            # Try to convert the user input to an integer
            integer_input = int(bmi)
            if int(bmi) > 2026 or int(bmi) <2010:
                st.error("Please enter a valid year between 2010-2026.")
            
        except ValueError:
            # If not successful, display an error message
            st.error("Please enter a valid integer.")



        age = st.selectbox("Weather type",("Rain", "Clouds", "Clear", "Snow", "Mist","Drizzle", "Haze", "Thunderstorm", "Fog", "Smoke", "Squall"),index=None,placeholder=" How is the weather ? ")
        def Weather_type_to_number(weather_type):
            # Define a dictionary to map day names to numbers
            w_type = {
                "Rain":1, "Clouds":2, "Clear":3, "Snow":4, "Mist":5,"Drizzle":6, "Haze":7, "Thunderstorm":8, "Fog":9, "Smoke":10, "Squall":11
                
            }

            # Check if the input day name is in the dictionary
            if weather_type in w_type:
                return w_type[weather_type]
            else:
                return None

        # Example usage:
        w_type_number = Weather_type_to_number(age)
        

        wd_dec = st.selectbox("Weather Description",("light rain", "few clouds", "Sky is Clear", "light snow", "sky is clear", "mist", "broken clouds", "moderate rain", "drizzle", "overcast clouds", "scattered clouds", "haze", "proximity thunderstorm", "light intensity drizzle", "heavy snow", "heavy intensity rain", "fog", "heavy intensity drizzle", "shower snow", "snow", "thunderstorm with rain",
              "thunderstorm with heavy rain", "thunderstorm with light rain", "proximity thunderstorm with rain", "thunderstorm with drizzle", "smoke", "thunderstorm", "proximity shower rain", "very heavy rain", "proximity thunderstorm with drizzle", "light rain and snow", "light intensity shower rain", "SQUALLS", "shower drizzle", "thunderstorm with light drizzle"),index=None,placeholder="What is the weather description ? ")
        def Weather_des_to_number(weatherD_type):
            # Define a dictionary to map day names to numbers
            wD_type = {
                "light rain":1, "few clouds":2, "Sky is Clear":3, "light snow":4, "sky is clear":5, "mist":6, "broken clouds":7, "moderate rain":8,
                "drizzle":9, "overcast clouds":10, "scattered clouds":11, "haze":12, "proximity thunderstorm":13, "light intensity drizzle":14, "heavy snow":15, 
                "heavy intensity rain":16, "fog":17, "heavy intensity drizzle":18, "shower snow":19, "snow":20, "thunderstorm with rain":21,
              "thunderstorm with heavy rain":22, "thunderstorm with light rain":23, "proximity thunderstorm with rain":24, 
              "thunderstorm with drizzle":25, "smoke":26, "thunderstorm":27, "proximity shower rain":28, "very heavy rain":29, "proximity thunderstorm with drizzle":30, 
              "light rain and snow":31, "light intensity shower rain":32, "SQUALLS":33, "shower drizzle":34, "thunderstorm with light drizzle":35
                
            }

            # Check if the input day name is in the dictionary
            if weatherD_type in wD_type:
                return wD_type[weatherD_type]
            else:
                return None

        # Example usage:
        wD_type_number = Weather_des_to_number(wd_dec)
        

        features = [hd, ag, day_number, sth, insulin, bmi, gc, w_type_number, wD_type_number]
        
        

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        # score = score + 0.20 #correction factor
        # st.info("Predicted Sucessfully")

        
        if(prediction<=1000):
            st.success("No Traffic on this day",icon="✅")
        if(prediction>1000 and prediction<=3000):
            st.error("Busy or Normal Traffic",icon="🚨")
        if(prediction>3000 and prediction<=5000):
            st.error("heavy Traffic",icon="🚨")
        if(prediction>5000):
            st.warning("Do not go! Extreme Traffic",icon="🚨")
        

        # Print teh score of the model 
        # st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
        st.write(prediction)
