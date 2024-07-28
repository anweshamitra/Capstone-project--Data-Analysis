
from flask import Flask, jsonify # type: ignore
import pyodbc # type: ignore
import pandas as pd

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=localhost\SQLEXPRESS;'  # Replace with your server name and instance
        'DATABASE=POPULATION_2020TO2029;'  # Replace with your database name
        'Trusted_Connection=yes;'
    )
    return conn

# Load queries from file
def load_queries():
    queries = {}
    with open(r'Population2020-2029.sql', 'r') as file:
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

queries = load_queries()
print(f"Loaded queries: {queries.keys()}")  # Debugging line

@app.route('/')
def index():
    return "Flask API is running. Use /query/<query_name> to execute queries."

# Endpoint to execute SQL queries
@app.route('/query/<string:query_name>', methods=['GET'])
def execute_query(query_name):
    query = queries.get(query_name)
    if not query:
        return jsonify({'error': 'Query not found'}), 404

    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
