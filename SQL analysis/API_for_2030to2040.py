from flask import Flask, jsonify
import pyodbc
import pandas as pd

app_2030_2040 = Flask(__name__)

# Database connection function for 2030-2040
def get_db_connection_2030_2040():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=localhost\SQLEXPRESS;'  # Replace with your server name and instance
        'DATABASE=POPULATION_2030TO2040;'  # Replace with your database name
        'Trusted_Connection=yes;'
    )
    return conn

# Load queries from file for 2030-2040
def load_queries_2030_2040():
    queries = {}
    with open(r'C:\Users\anwes\OneDrive\Desktop\PROJECT\Capstone Project\SQL analysis\population-2030-2040.sql', 'r') as file:
        query_name = None
        query = ""
        for line in file:
            if line.startswith('--'):
                if query_name and query:
                    queries[query_name] = query.strip()
                query_name = line[2:].strip()
                query = ""
            else:
                query += line
        if query_name and query:
            queries[query_name] = query.strip()
    return queries

queries_2030_2040 = load_queries_2030_2040()
print(f"Loaded queries (2030-2040): {queries_2030_2040.keys()}")  # Debugging line

@app_2030_2040.route('/')
def index_2030_2040():
    return "Flask API for Population 2030-2040 is running. Use /query/<query_name> to execute queries."

# Endpoint to execute SQL queries for 2030-2040
@app_2030_2040.route('/query/<string:query_name>', methods=['GET'])
def execute_query_2030_2040(query_name):
    query = queries_2030_2040.get(query_name)
    if not query:
        return jsonify({'error': 'Query not found'}), 404

    conn = get_db_connection_2030_2040()
    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_json(orient='records')

if __name__ == '__main__':
    app_2030_2040.run(port=5001, debug=True)
