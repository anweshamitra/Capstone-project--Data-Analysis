# import streamlit as st
# import plotly.express as px
# import pandas as pd
# import os
# import warnings
# import numpy as np
# import matplotlib.pyplot as plt

# warnings.filterwarnings('ignore')

# st.set_page_config(page_title="World Population Analysis", page_icon=":bar_chart:", layout="wide")

# st.title(" :bar_chart: World Population Analysis")
# st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)

# # Function to load default dataset
# def load_default_data():
#     default_path = "C:/Users/anwes/Downloads/population_2020-2029.csv"
#     if os.path.exists(default_path):
#         df = pd.read_csv(default_path)
#         return df
#     else:
#         st.error("Default data file not found. Please upload a file.")
#         st.stop()

# # File uploader
# fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
# if fl is not None:
#     filename = fl.name
#     st.write(filename)
    
#     if filename.endswith('.csv') or filename.endswith('.txt'):
#         df = pd.read_csv(fl)
#     elif filename.endswith('.xlsx') or filename.endswith('.xls'):
#         df = pd.read_excel(fl)
#     else:
#         st.error("Unsupported file type. Please upload a CSV or Excel file.")
#         st.stop()
# else:
#     df = load_default_data()

# # Ensure necessary columns are present
# required_columns = ['AgeGrp', 'PopMale', 'PopFemale', 'Time']
# if not all(column in df.columns for column in required_columns):
#     st.error("The uploaded file does not contain the necessary columns. Using default dataset.")
#     df = load_default_data()

# # Rename columns
# df.rename(columns={'PopMale': 'Male_population', 'PopFemale': 'Female_population'}, inplace=True)

# # Convert datatypes to numeric and then to float64
# df['Male_population'] = pd.to_numeric(df['Male_population'], errors='coerce').astype('float64')
# df['Female_population'] = pd.to_numeric(df['Female_population'], errors='coerce').astype('float64')
# df['PopTotal'] = pd.to_numeric(df['PopTotal'], errors='coerce').astype('float64')

# # Remove rows with NaN values in 'Male_population' and 'Female_population'
# df.dropna(subset=['Male_population', 'Female_population'], inplace=True)

# # Group data by AgeGrp and calculate the total male and female population for each age group
# grouped_data = df.groupby('AgeGrp').agg({'Male_population': 'sum', 'Female_population': 'sum'}).reset_index()

# # Sort the data by AgeGrp
# grouped_data = grouped_data.sort_values(by='AgeGrp')

# # Set the positions and width for the bars
# bar_width = 0.35
# r1 = np.arange(len(grouped_data['AgeGrp']))
# r2 = [x + bar_width for x in r1]

# # Plotting the bar chart
# plt.figure(figsize=(14, 8))
# plt.bar(r1, grouped_data['Male_population'], color='grey', width=bar_width, edgecolor='grey', label='Male')
# plt.bar(r2, grouped_data['Female_population'], color='brown', width=bar_width, edgecolor='grey', label='Female')

# # Adding titles and labels
# plt.title('Male and Female Population for Each Age Group')
# plt.xlabel('Age Group', fontweight='bold')
# plt.ylabel('Population', fontweight='bold')
# plt.xticks([r + bar_width / 2 for r in range(len(grouped_data['AgeGrp']))], grouped_data['AgeGrp'])
# plt.legend()

# # Show the plot
# plt.show()

# # Continue with the rest of the Streamlit dashboard
# col1, col2 = st.columns((2))
# df["Time"] = pd.to_datetime(df["Time"], format='%Y')

# # Getting the min and max date 
# startDate = pd.to_datetime(df["Time"]).min()
# endDate = pd.to_datetime(df["Time"]).max()

# with col1:
#     date1 = pd.to_datetime(st.date_input("Start Date", startDate))

# with col2:
#     date2 = pd.to_datetime(st.date_input("End Date", endDate))

# df = df[(df["Time"] >= date1) & (df["Time"] <= date2)].copy()

# st.sidebar.header("Choose your filter: ")
# # Create for Age Group
# age_group = st.sidebar.multiselect("Pick your Age Group", df["AgeGrp"].unique())
# if not age_group:
#     df2 = df.copy()
# else:
#     df2 = df[df["AgeGrp"].isin(age_group)]

# # Filter the data based on Age Group
# filtered_df = df2

# # Analysis based on Age Group
# age_group_df = filtered_df.groupby(by=["AgeGrp"], as_index=False).agg({'Male_population': 'sum', 'Female_population': 'sum'})

# with col1:
#     st.subheader("Age Group wise Population")
#     fig = px.bar(age_group_df, x="AgeGrp", y=["Male_population", "Female_population"], barmode='group', template="seaborn")
#     st.plotly_chart(fig, use_container_width=True, height=200)

# with col2:
#     st.subheader("Time wise Population")
#     time_df = filtered_df.groupby(by=["Time"], as_index=False).agg({'Male_population': 'sum', 'Female_population': 'sum'})
#     fig = px.line(time_df, x="Time", y=["Male_population", "Female_population"], template="seaborn")
#     st.plotly_chart(fig, use_container_width=True)

# cl1, cl2 = st.columns((2))
# with cl1:
#     with st.expander("Age Group Population Data"):
#         st.write(age_group_df.style.background_gradient(cmap="Blues"))
#         csv = age_group_df.to_csv(index=False).encode('utf-8')
#         st.download_button("Download Data", data=csv, file_name="Age_Group_Population.csv", mime="text/csv",
#                             help='Click here to download the data as a CSV file')

# with cl2:
#     with st.expander("Time wise Population Data"):
#         st.write(time_df.style.background_gradient(cmap="Oranges"))
#         csv = time_df.to_csv(index=False).encode('utf-8')
#         st.download_button("Download Data", data=csv, file_name="Time_Population.csv", mime="text/csv",
#                         help='Click here to download the data as a CSV file')

# filtered_df["month_year"] = filtered_df["Time"].dt.to_period("M")
# st.subheader('Time Series Analysis')

# linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b")).agg({'Male_population': 'sum', 'Female_population': 'sum'})).reset_index()
# fig2 = px.line(linechart, x="month_year", y=["Male_population", "Female_population"], labels={"value": "Population"}, height=500, width=1000, template="gridon")
# st.plotly_chart(fig2, use_container_width=True)

# with st.expander("View Data of TimeSeries:"):
#     st.write(linechart.T.style.background_gradient(cmap="Blues"))
#     csv = linechart.to_csv(index=False).encode("utf-8")
#     st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')

# # Create a treemap based on Time and Age Group
# st.subheader("Hierarchical view of Population using TreeMap")
# fig3 = px.treemap(filtered_df, path=["Time", "AgeGrp"], values="Male_population", hover_data=["Female_population"],
#                   color="AgeGrp")
# fig3.update_layout(width=800, height=650)
# st.plotly_chart(fig3, use_container_width=True)

# chart1, chart2 = st.columns((2))
# with chart1:
#     st.subheader('Age Group wise Male Population')
#     fig = px.pie(filtered_df, values="Male_population", names="AgeGrp", template="plotly_dark")
#     fig.update_traces(text=filtered_df["AgeGrp"], textposition="inside")
#     st.plotly_chart(fig, use_container_width=True)

# with chart2:
#     st.subheader('Age Group wise Female Population')
#     fig = px.pie(filtered_df, values="Female_population", names="AgeGrp", template="gridon")
#     fig.update_traces(text=filtered_df["AgeGrp"], textposition="inside")
#     st.plotly_chart(fig, use_container_width=True)

# import plotly.figure_factory as ff
# st.subheader(":point_right: Time wise Population Summary")
# with st.expander("Summary_Table"):
#     df_sample = df[0:5][["AgeGrp", "Time", "Male_population", "Female_population"]]
#     fig = ff.create_table(df_sample, colorscale="Cividis")
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("Time wise Population Table")
#     filtered_df["month"] = filtered_df["Time"].dt.month_name()
#     population_time = pd.pivot_table(data=filtered_df, values="Male_population", index=["AgeGrp"], columns="month")
#     st.write(population_time.style.background_gradient(cmap="Blues"))

# # Create a scatter plot
# filtered_df = filtered_df.dropna(subset=['Male_population', 'Female_population'])
# data1 = px.scatter(filtered_df, x="Male_population", y="Female_population", size="Male_population", color="AgeGrp")
# st.plotly_chart(data1, use_container_width=True)

# st.sidebar.markdown('<div style="position: fixed; bottom: 10px; width: 100%;">Developed by **Anwesha Mitra**</div>',
#                     unsafe_allow_html=True)

# # Download original DataSet
# csv = df.to_csv(index=False).encode('utf-8')
# st.download_button('Download Data', data=csv, file_name="Population_Data.csv", mime="text/csv")

import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

st.set_page_config(page_title="World Population Analysis", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: World Population Analysis")
st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)

# Function to load default dataset
def load_default_data():
    default_path = "C:/Users/anwes/Downloads/population_2020-2029.csv"
    if os.path.exists(default_path):
        df = pd.read_csv(default_path)
        return df
    else:
        st.error("Default data file not found. Please upload a file.")
        st.stop()

# File uploader
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    
    if filename.endswith('.csv') or filename.endswith('.txt'):
        df = pd.read_csv(fl)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        df = pd.read_excel(fl)
    else:
        st.error("Unsupported file type. Please upload a CSV or Excel file.")
        st.stop()
else:
    df = load_default_data()

# Ensure necessary columns are present
required_columns = ['AgeGrp', 'PopMale', 'PopFemale', 'Time', 'Location']
if not all(column in df.columns for column in required_columns):
    st.error("The uploaded file does not contain the necessary columns. Using default dataset.")
    df = load_default_data()

# Rename columns
df.rename(columns={'PopMale': 'Male_population', 'PopFemale': 'Female_population'}, inplace=True)

# Convert datatypes to numeric and then to float64
df['Male_population'] = pd.to_numeric(df['Male_population'], errors='coerce').astype('float64')
df['Female_population'] = pd.to_numeric(df['Female_population'], errors='coerce').astype('float64')
df['PopTotal'] = pd.to_numeric(df['PopTotal'], errors='coerce').astype('float64')

# Convert 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

# Remove rows with NaN values in 'Male_population', 'Female_population', or 'Time'
df.dropna(subset=['Male_population', 'Female_population', 'Time'], inplace=True)

# Group data by AgeGrp and calculate the total male and female population for each age group
grouped_data = df.groupby('AgeGrp').agg({'Male_population': 'sum', 'Female_population': 'sum'}).reset_index()

# Sort the data by AgeGrp
grouped_data = grouped_data.sort_values(by='AgeGrp')

# Set the positions and width for the bars
bar_width = 0.35
r1 = np.arange(len(grouped_data['AgeGrp']))
r2 = [x + bar_width for x in r1]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.bar(r1, grouped_data['Male_population'], color='grey', width=bar_width, edgecolor='grey', label='Male')
plt.bar(r2, grouped_data['Female_population'], color='brown', width=bar_width, edgecolor='grey', label='Female')

# Adding titles and labels
plt.title('Male and Female Population for Each Age Group')
plt.xlabel('Age Group', fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.xticks([r + bar_width / 2 for r in range(len(grouped_data['AgeGrp']))], grouped_data['AgeGrp'])
plt.legend()

# Show the plot
plt.show()

# Continue with the rest of the Streamlit dashboard
st.sidebar.header("Choose your filter: ")

# Create filters for Age Group, Location, and Time
age_group = st.sidebar.multiselect("Pick your Age Group", df["AgeGrp"].unique())
location = st.sidebar.multiselect("Pick your Location", df["Location"].unique())
# times = st.sidebar.multiselect("Pick your Time", df["Time"].dt.year.unique())

# Apply filters
if age_group:
    df = df[df["AgeGrp"].isin(age_group)]

if location:
    df = df[df["Location"].isin(location)]

# if times:
#     df = df[df["Time"].dt.year.isin(times)]

# Group data by AgeGrp and Location
grouped_df = df.groupby(['AgeGrp', 'Location']).agg({'Male_population': 'sum', 'Female_population': 'sum'}).reset_index()

# Analysis based on Age Group and Location
col1, col2 = st.columns((2))
with col1:
    st.subheader("Age Group and Location wise Population")
    fig = px.bar(grouped_df, x="AgeGrp", y=["Male_population", "Female_population"], color="Location", barmode='group', template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)

with col2:
    st.subheader("Time wise Population")
    time_df = df.groupby(by=["Time"], as_index=False).agg({'Male_population': 'sum', 'Female_population': 'sum'})
    fig = px.line(time_df, x="Time", y=["Male_population", "Female_population"], template="seaborn")
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns((2))
with cl1:
    with st.expander("Age Group and Location Population Data"):
        st.write(grouped_df.style.background_gradient(cmap="Blues"))
        csv = grouped_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Age_Group_Location_Population.csv", mime="text/csv",
                            help='Click here to download the data as a CSV file')

with cl2:
    with st.expander("Time wise Population Data"):
        st.write(time_df.style.background_gradient(cmap="Oranges"))
        csv = time_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Time_Population.csv", mime="text/csv",
                        help='Click here to download the data as a CSV file')

# Convert Time column to period for monthly data
df["month_year"] = df["Time"].dt.to_period("M")
st.subheader('Time Series Analysis')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b")).agg({'Male_population': 'sum', 'Female_population': 'sum'})).reset_index()
fig2 = px.line(linechart, x="month_year", y=["Male_population", "Female_population"], labels={"value": "Population"}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')

# Create a treemap based on Time, Location, and Age Group
st.subheader("Hierarchical view of Population using TreeMap")
fig3 = px.treemap(df, path=["Time", "Location", "AgeGrp"], values="Male_population", hover_data=["Female_population"],
                  color="AgeGrp")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 = st.columns((2))
with chart1:
    st.subheader('Age Group wise Male Population')
    fig = px.pie(df, values="Male_population", names="AgeGrp", template="plotly_dark")
    fig.update_traces(text=df["AgeGrp"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader('Age Group wise Female Population')
    fig = px.pie(df, values="Female_population", names="AgeGrp", template="gridon")
    fig.update_traces(text=df["AgeGrp"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Time wise Population Summary")
with st.expander("Summary_Table"):
    df_sample = df[0:5][["AgeGrp", "Time", "Male_population", "Female_population"]]
    fig = ff.create_table(df_sample, colorscale="Cividis")
    st.plotly_chart(fig, use_container_width=True)

filtered_df = df.copy()

# Data Visualization
st.subheader("Scatter Plot of Male vs Female Population")
data1 = px.scatter(filtered_df, x="Male_population", y="Female_population", size="Male_population", color="AgeGrp")
st.plotly_chart(data1, use_container_width=True)

st.sidebar.markdown('<div style="position: fixed; bottom: 10px; width: 100%;">Developed by **Anwesha Mitra**</div>', unsafe_allow_html=True)
