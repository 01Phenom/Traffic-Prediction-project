# Import pages
from Tabs import home, data, predict, visualise, oscia3, about

# Configure the app
st.set_page_config(
    page_title='Traffic Prediction',
    page_icon='random',
    layout='wide',
    initial_sidebar_state='auto'
)

# Dictionary for pages
Tabs = {
    "***Home***": home,
    "***Data Info***": data,
    "***Visualisation***": visualise,
    "***Prediction***": predict,
    "***Traffic signal Simulation***": oscia3,
    "***About***": about,
}

# Create a sidebar
st.sidebar.header("Menu")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset
df, X, y, data1 = load_data()

# Call the app function of the selected page
if page in ["***Prediction***", "***Visualisation***"]:
    Tabs[page].app(df, X, y, data1)
elif page == "***Data Info***":
    Tabs[page].app(df)
else:
    Tabs[page].app()
