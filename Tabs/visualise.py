import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import tree
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y, data1):
    """This function creates the visualization page"""

    # Remove the warnings
    warnings.filterwarnings('ignore')

    # Set the page title
    st.title("Visualise the :blue[Traffic Dataset]")

    # Create a checkbox to show the correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize=(20, 20))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot=True, cmap='Blues')
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig)

    if st.checkbox("Show the histogram of temperature"):
        st.subheader("Correlation Temperature")
        df["temperature"].hist(bins=20)
        st.pyplot()

    if st.checkbox("Show the Trend of traffic according to Time"):
        st.subheader("Correlation Time")
        metrics = ['month', 'month_day', 'weekday', 'hour']
        fig = plt.figure(figsize=(10, 4 * len(metrics)))
        for i, metric in enumerate(metrics):
            ax = fig.add_subplot(len(metrics), 1, i + 1)
            ax.plot(df.groupby(metric)['traffic_volume'].mean(), '-o')
            ax.set_xlabel(metric)
            ax.set_ylabel("Mean Traffic")
            ax.set_title(f"Traffic Trend by {metric}")
        plt.tight_layout()
        st.pyplot(fig)

    if st.checkbox("months against traffic by Scatter plot"):
        st.subheader("Scatter plot")
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.scatterplot(x="month", y="traffic_volume", data=df)
        st.pyplot()

    if st.checkbox("monthly average traffic"):
        st.subheader("Monthly Average Traffic")
        df["month"].plot(kind='hist')
        st.pyplot()

    if st.checkbox("traffic volume according to Weather type using line graph"):
        st.subheader("Line graph")
        new_features = ["year", "month", "hour", "month_day"]

        for i in new_features:
            fig = plt.figure(figsize=(10, 2), facecolor="#99ccff")
            ax = sns.lineplot(x=data1[i], y="traffic_volume", data=data1, hue="weather_type")
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            st.pyplot(fig)

    if st.checkbox("Show Histogram"):
        st.subheader("Traffic Volume Histogram")
        data1["traffic_volume"].plot(kind='hist')
        st.pyplot()
