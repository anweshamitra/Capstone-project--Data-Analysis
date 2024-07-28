import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="World Population Analysis 2030-2040", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: World Population Analysis 2030-2040")
st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)

# API URL
API_URL = "http://127.0.0.1:5001/query/"

# Function to fetch data from API
def fetch_data(query_name):
    response = requests.get(API_URL + query_name)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        # Ensure the 'Time' column is correctly formatted as a string and drop rows where 'Time' is 'nan'
        if 'Time' in df.columns:
            df['Time'] = df['Time'].astype(str)
            df = df[df['Time'] != 'nan']  # Drop rows where 'Time' is 'nan'
        return df
    else:
        st.error(f"Failed to fetch data for query: {query_name}")
        return pd.DataFrame()

# Sidebar for query selection
st.sidebar.header("Select a query")
queries = [
    "LOCATION",
    "Population by location",
    "Highest population at each location",
    "Average male and female population at each location",
    "Highest male and female population at each location",
    "Highest male population at each location",
    "Highest female population at each location",
    "Total Population by Location",
    "Highest population in each year",
    "Average male and female population for each year",
    "Highest population of each age group",
    "Highest male population of each age group",
    "Highest female population of each age group",
    "Average male population of each age group",
    "Average female population of each age group"
]
query_name = st.sidebar.selectbox("Choose a query to visualize", queries)

# Fetch data
data = fetch_data(query_name)

# Display data
st.title(f"Results for query: {query_name}")
st.write(data)

# Visualizations
if not data.empty:
    # Print data to debug
    st.write("Data Snapshot:", data.head())
    
    if query_name == "Population by location":
        st.subheader("Population by Location")
        fig = px.bar(data, x='Location', y=['Male_population', 'Female_population', 'Total_population'], barmode='group', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

    
    elif query_name == "Highest population at each location":
        st.subheader("Highest population at each location")
        if 'Location' in data.columns and 'Maximum_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='Location', y='Maximum_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Average male and female population at each location":
        st.subheader("Average Male and Female Population at Each Location")
        if 'Location' in data.columns and 'AvgMalePopulation' in data.columns and 'AvgFemalePopulation' in data.columns:
            fig = px.bar(data, x='Location', y=['AvgMalePopulation', 'AvgFemalePopulation'], barmode='group', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest male and female population at each location":
        st.subheader("Highest Male and Female Population at Each Location")
        if 'Location' in data.columns and 'HighestMalePopulation' in data.columns and 'HighestFemalePopulation' in data.columns:
            fig = px.bar(data, x='Location', y=['HighestMalePopulation', 'HighestFemalePopulation'], barmode='group', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest male population at each location":
        st.subheader("Highest Male Population at Each Location")
        if 'Location' in data.columns and 'Maximum_Male_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='Location', y='Maximum_Male_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest female population at each location":
        st.subheader("Highest Female Population at Each Location")
        if 'Location' in data.columns and 'Maximum_Female_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='Location', y='Maximum_Female_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Total_Population_by_Location_for_2020":
        st.subheader("Total Population by Location for 2020")
        if 'Location' in data.columns and 'TotalPopulation' in data.columns:
            fig = px.bar(data, x='Location', y='TotalPopulation', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest population in each year":
        st.subheader("Highest Population in Each Year")
        if 'Time' in data.columns and 'Maximum_Population' in data.columns:
            fig = px.line(data, x='Time', y='Maximum_Population', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Average male and female population for each year":
        st.subheader("Average Male and Female Population for Each Year")
        if 'Time' in data.columns and 'AvgMalePopulation' in data.columns and 'AvgFemalePopulation' in data.columns:
            fig = px.line(data, x='Time', y=['AvgMalePopulation', 'AvgFemalePopulation'], template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest population of each age group":
        st.subheader("Highest Population of Each Age Group")
        if 'AgeGrp' in data.columns and 'Maximum_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='AgeGrp', y='Maximum_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest male population of each age group":
        st.subheader("Highest Male Population of Each Age Group")
        if 'AgeGrp' in data.columns and 'Maximum_Male_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='AgeGrp', y='Maximum_Male_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Highest female population of each age group":
        st.subheader("Highest Female Population of Each Age Group")
        if 'AgeGrp' in data.columns and 'Maximum_Female_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='AgeGrp', y='Maximum_Female_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Average male population of each age group":
        st.subheader("Average Male Population of Each Age Group")
        if 'AgeGrp' in data.columns and 'Average_Male_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='AgeGrp', y='Average_Male_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
    
    elif query_name == "Average female population of each age group":
        st.subheader("Average Female Population of Each Age Group")
        if 'AgeGrp' in data.columns and 'Average_Female_Population' in data.columns and 'Time' in data.columns:
            fig = px.bar(data, x='AgeGrp', y='Average_Female_Population', color='Time', template='plotly_dark')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Columns missing for this query. Please check the data.")
