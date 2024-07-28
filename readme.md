# World Population Data Analysis and Visualization

This project involves data cleaning and analysis of two datasets of world population using SQL Server and Python (in Jupyter Notebook). After the data cleaning, a dashboard is prepared using Streamlit for Python data analysis. Additionally, a Flask API is created to fetch data from SQL Server, which is then visualized using Streamlit. The dashboard can also handle an uploaded file with a similar data structure for analysis.

## Project Structure

- **Data Cleaning**: Performed using SQL in SQL Server and Python in Jupyter Notebook.
- **API Creation**: Flask API to fetch data from SQL Server.
- **Dashboard**: Built using Streamlit to visualize data from both the Python analysis and SQL Server through the Flask API.

## Prerequisites

- Python 3.8+
- SQL Server
- Jupyter Notebook
- Streamlit
- Flask
- Required Python packages:
  - pandas
  - pyodbc
  - requests
  - plotly
  - streamlit

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/world-population-analysis.git
   cd world-population-analysis
Install Python dependencies:

bash

pip install -r requirements.txt
Set up SQL Server:

Create a database named POPULATION_2030TO2040.
Import your datasets into SQL Server.
Modify the connection string in the app.py to match your SQL Server configuration.

# Data Cleaning

SQL Server
Data cleaning is performed using SQL scripts stored in the SQL/ directory.

Python
Data cleaning using Python is performed in Jupyter Notebook. Notebooks are stored in the notebooks/ directory.


# Flask API
A Flask API is created to fetch data from SQL Server.

Running the Flask API
Navigate to the Flask API directory:


bash
cd flask_api
Run the Flask application:

bash
python app.py
The API will be available at http://127.0.0.1:5000.
The API will be available at http://127.0.0.1:5001.

Streamlit Dashboard
The Streamlit dashboard fetches data from the Flask API and visualizes it.

Running the Streamlit Dashboard
Navigate to the Streamlit dashboard directory:

bash
cd streamlit_dashboard
Run the Streamlit application:

bash
streamlit run dashboard.py
The dashboard will be available at http://localhost:8501.

Usage
Selecting a Query
Use the sidebar in the Streamlit dashboard to select a query for visualization.
The dashboard will display data and visualizations based on the selected query.
Uploading a File
The dashboard allows you to upload a file with a similar data structure for analysis.
Uploaded data will be processed and visualized in the dashboard.


This `README.md` file provides a comprehensive overview of the project, including installation.

Contact: anweshamitra21268@gmail.com