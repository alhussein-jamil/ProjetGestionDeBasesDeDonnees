from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'CyberTitan',
    'password': '19216811',
    'database': 'accidentsroutiers',
}

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(**db_config)

# Route for the main page
@app.route('/')
def index():
    # Fetch data from the database
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)

    # Example query: Retrieve the first 10 rows from the accidents table
    query = 'SELECT * FROM gravite LIMIT 10'
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

    # Close the database connection
    cursor.close()
    connection.close()

    # Render the template with the retrieved data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
