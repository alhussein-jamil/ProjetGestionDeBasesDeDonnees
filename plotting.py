import mysql.connector
import plotly.express as px
import pandas as pd

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

# Function to execute a query and return a DataFrame
def execute_query(query):
    connection = connect_to_db()
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

# Query 1: Retrieve information about accidents involving pedestrians
query1 = """
SELECT
    usagers.id_usager,
    gravite.gravite AS 'Severity',
    caracteristiques.mois AS 'Month',
    categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category'
FROM
    usagers
        JOIN
    caracteristiques ON Accident_Id = Num_Acc
        JOIN
    vehicules USING (Num_Acc)
        JOIN
    categorie_du_vehicule ON vehicules.catv = categorie_du_vehicule.id_categorie_du_vehicule
        JOIN
    gravite ON usagers.grav = gravite.id_gravite
        JOIN
    categorie_usager ON usagers.catu = categorie_usager.id_categorie_usager
WHERE
    usagers.catu = 3;
"""

# Query 2: Find the most common atmospheric condition during accidents.
query2 = """
SELECT
    conditions_atmospheriques.conditions_atmospheriques,
    COUNT(*) AS 'Accident Count'
FROM
    conditions_atmospheriques
JOIN
    caracteristiques ON conditions_atmospheriques.id_conditions_atmospheriques = caracteristiques.atm
GROUP BY
    conditions_atmospheriques.conditions_atmospheriques
ORDER BY
    COUNT(*) DESC
LIMIT 5;
"""

# Execute queries and fetch data
df_query1 = execute_query(query1)
df_query2 = execute_query(query2)

# # Visualization for Query 1
# fig1 = px.bar(df_query1, x='Month', y='id_usager', color='Severity', facet_col='Vehicle Category',
#               labels={'id_usager': 'User ID', 'Month': 'Month'})

# # Visualization for Query 2
# fig2 = px.bar(df_query2, x='conditions_atmospheriques', y='Accident Count',
#               labels={'conditions_atmospheriques': 'Atmospheric Conditions', 'Accident Count': 'Number of Accidents'})

# # Show the visualizations
# fig1.show()
# fig2.show()

fig = px.bar(df_query1, x='Month', y='Severity', color='Vehicle Category',
             labels={'Severity': 'Severity', 'Month': 'Month', 'Vehicle Category': 'Vehicle Category'},
             title='Accident Severity by Month and Vehicle Category',
             barmode='group')

fig.show()