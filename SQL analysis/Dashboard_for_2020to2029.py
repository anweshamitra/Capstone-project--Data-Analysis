import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(page_title="World Population Analysis 2020-2029", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: World Population Analysis 2020-2029")
st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)

# API URL
API_URL = "http://127.0.0.1:5000/query/"

# Function to fetch data from API
def fetch_data(query_name):
    response = requests.get(API_URL + query_name)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error(f"Failed to fetch data for query: {query_name}")
        return pd.DataFrame()

# Sidebar for query selection
st.sidebar.header("Select a query")
queries = [
    "highest_population_at_each_location",
    "average_male_and_female_population_at_each_location",
    "highest_male_and_female_population_at_each_location",
    "highest_male_population_at_each_location",
    "highest_female_population_at_each_location",
    "total_population_by_location",
    "highest_population_in_each_year",
    "average_male_and_female_population_for_each_year",
    "highest_population_of_each_age_group",
    "highest_male_population_of_each_age_group",
    "highest_female_population_of_each_age_group",
    "average_male_population_of_each_age_group",
    "average_female_population_of_each_age_group"
]
query_name = st.sidebar.selectbox("Choose a query to visualize", queries)

# Fetch data
data = fetch_data(query_name)

# Display data
st.title(f"Results for query: {query_name}")
st.write(data)

# Visualizations
if not data.empty:
    if query_name == "LOCATION":
        st.subheader("Population by Location")
        fig = px.bar(data, x='Location', y=['Male_population', 'Female_population', 'Total_population'], barmode='group', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_population_at_each_location":
        st.subheader("Highest Population at Each Location")
        fig = px.bar(data, x='Location', y='Maximum_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "average_male_and_female_population_at_each_location":
        st.subheader("Average Male and Female Population at Each Location")
        fig = px.bar(data, x='Location', y=['AvgMalePopulation', 'AvgFemalePopulation'], barmode='group', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_male_and_female_population_at_each_location":
        st.subheader("Highest Male and Female Population at Each Location")
        fig = px.bar(data, x='Location', y=['HighestMalePopulation', 'HighestFemalePopulation'], barmode='group', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_male_population_at_each_location":
        st.subheader("Highest Male Population at Each Location")
        fig = px.bar(data, x='Location', y='Maximum_Male_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_female_population_at_each_location":
        st.subheader("Highest Female Population at Each Location")
        fig = px.bar(data, x='Location', y='Maximum_Female_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "Total_Population_by_Location":
        st.subheader("Total Population by Location for 2020")
        fig = px.bar(data, x='Location', y='TotalPopulation', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_population_in_each_year":
        st.subheader("Highest Population in Each Year")
        fig = px.line(data, x='Time', y='Maximum_Population', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "average_male_and_female_population_for_each_year":
        st.subheader("Average Male and Female Population for Each Year")
        fig = px.line(data, x='Time', y=['AvgMalePopulation', 'AvgFemalePopulation'], template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_population_of_each_age_group":
        st.subheader("Highest Population of Each Age Group")
        fig = px.bar(data, x='AgeGrp', y='Maximum_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_male_population_of_each_age_group":
        st.subheader("Highest Male Population of Each Age Group")
        fig = px.bar(data, x='AgeGrp', y='Maximum_Male_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "highest_female_population_of_each_age_group":
        st.subheader("Highest Female Population of Each Age Group")
        fig = px.bar(data, x='AgeGrp', y='Maximum_Female_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "average_male_population_of_each_age_group":
        st.subheader("Average Male Population of Each Age Group")
        fig = px.bar(data, x='AgeGrp', y='Average_Male_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    
    elif query_name == "average_female_population_of_each_age_group":
        st.subheader("Average Female Population of Each Age Group")
        fig = px.bar(data, x='AgeGrp', y='Average_Female_Population', color='Time', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
