import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D

# Replace these with your MySQL database credentials
db_config = {
    "host": "localhost",
    "user": "user4projet",
    "password": "Hellogenielogiciel2023",
    "database": "accidentsroutiers",
    "auth_plugin": "mysql_native_password",
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


queries = [""]
titles = []
plot_3D = []

# ignore comments starting with -- and each query starts with SELECT and ends with ; annd can be on multiple lines
with open("Queries.sql") as f:
    i = 0
    for line in f:
        if "--" in line or "USE" in line:
            if "title" in line:
                titles.append(
                    line.split("title")[1].split("=")[1].strip().replace("'", "")
                )
                print(titles[-1])
            else:
                if "Query" in line:
                    if "3D" in line:
                        print(line)
                        plot_3D.append(True)
                    else:
                        plot_3D.append(False)
            continue
        queries[i] += line
        if line.endswith(";\n"):
            i += 1
            queries.append("")

# # Query 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
# query1 = queries[0]
# print(query1)
# df_query1 = execute_query(query1)

# # Plot for Query 1
# #fig = px.bar(df_query1, x='Vehicle Category', color='Severity', title='Accidents Severity')
# # Mapping des valeurs textuelles de Severity à des valeurs numériques
# severity_mapping = {'Indemne': 1, 'Blessé léger': 2, 'Blessé hospitalisé': 3, 'Tué': 4}
# df_query1['Severity'] = df_query1['Severity'].map(severity_mapping)

# # Création du scatter plot
# plt.figure(figsize=(10, 6))
# scatter = plt.scatter(df_query1['Month'], df_query1['Vehicle Category'], c=df_query1['Severity'], cmap='viridis', s=100)

# # Ajout de la barre de couleur avec les noms de gravité
# cbar = plt.colorbar(scatter, ticks=list(severity_mapping.values()))
# cbar.set_ticklabels(list(severity_mapping.keys()))
# cbar.set_label('Severity')

# # Ajout des labels et du titre
# plt.xlabel('Month')
# plt.ylabel('Vehicle Category')
# plt.title('Scatter Plot of Severity by Month and Vehicle Category')

# # Affichage du plot
# plt.show()

# breakpoint()
# # Query 2: Find the most common atmospheric condition during accidents.
# query2 = queries[1]
# print(query2)
# df_query2 = execute_query(query2)
# # Plot for Query 2

# fig = px.bar(df_query2, x='Conditions Atmospheriques', y='Accident Count', title='Most Common Atmospheric Conditions')
# fig.show()

# # Query 3: Find the average number of accidents for each category of the road.
# query3 = queries[2]
# df_query3 = execute_query(query3)
# # Plot for Query 3

# fig = px.bar(df_query3, x='Categorie De Route', y='Avg Num Accidents', title='Average Number of Accidents for Each Road Category')
# fig.show()

# # Query 4: List the different types of motorizations (type_motorisation) and the count of accidents for each type.
# query4 = queries[3]
# df_query4 = execute_query(query4)
# # Plot for Query 4
# fig = px.bar(df_query4, x='Type of Motorization', y='Accident Count', title='Accidents by Motorization Type')
# fig.show()

# # Query 6: Analyze the severity of accidents by looking at the number of fatalities, injuries, and the types of vehicles involved.
# query6 = queries[5]
# df_query6 = execute_query(query6)
# # Plot for Query 6
# fig = px.pie(df_query6, names='severity', values='severity_count', title='Severity of Accidents')
# fig.show()

# #  Query 7: Explore the involvement of different vehicle categories (catv) in accidents and analyze their contribution to overall road safety.
# query7 = queries[6]
# df_query7 = execute_query(query7)
# # Plot for Query 7
# fig = px.pie(df_query7, names='Vehicle Category', values='Total Accident', title='Accidents by Vehicle Category')
# fig.show()

# # Query 8: Examine the types of collisions (col) that occur most frequently. Determine if certain collision types are associated with higher injury rates.
# query8 = queries[7]
# df_query8 = execute_query(query8)
# # Plot for Query 8
# fig = px.bar(df_query8, x='Collision Type', y='Total Accident', title='Most Frequent Collision Types')
# fig.show()

# # Query 9: Analyze the age and gender (sexe) distribution of individuals involved in accidents and determine if there are age or gender-specific patterns. Safety Equipment Usage:
# query9 = queries[8]
# df_query9 = execute_query(query9)
# # Plot for Query 9
# fig = px.bar(df_query9, x='Gender', y='Average Equipment Use Score', title='Average Equipment Use Score by Gender')
# fig.show()

# # Query 11: Focus on pedestrian-related data (catu=3) to understand the locations (locp) and actions (actp) leading to pedestrian accidents. Vehicle Manoeuvres:
# query11 = queries[10]
# df_query11 = execute_query(query11)
# # Plot for Query 12
# fig = px.bar(df_query11, x="Location of Pedestrian", y="Total Accidents", color="Action of Pedestrian", title='Pedestrian Accidents')
# fig.show()


# Query 12 Investigate the types of manoeuvres performed by vehicles before accidents and their impact on collision outcomes.
query12 = queries[11]
df_query12 = execute_query(query12)
# # Plot for Query 12
# fig = go.Figure(data=[
#     go.Bar(name="Death Accidents", x=df_query12['Manoeuvre'], y=df_query12["Death Accidents"]),
#     go.Bar(name="Serious Injury Accidents", x=df_query12['Manoeuvre'], y=df_query12["Serious Injury Accidents"]),
#     go.Bar(name="Unscathed Accidents", x=df_query12['Manoeuvre'], y=df_query12["Unscathed Accidents"])
# ])

# fig.update_layout(barmode='stack', title='Manoeuvre Types and Accident Outcomes')
# fig.show()


def plotManoeuvreOutcomes(df_query, title):
    figure, ax = plt.subplots(figsize=(12, 8))

    # Bar chart
    bar_width = 0.6
    bar_positions = range(len(df_query["Manoeuvre"]))

    # Bar pour les accidents mortels
    ax.bar(
        bar_positions,
        df_query["Death Accidents"],
        width=bar_width,
        label="Death Accidents",
    )

    # Bar pour les accidents avec blessures graves
    ax.bar(
        bar_positions,
        df_query["Serious Injury Accidents"],
        bottom=df_query["Death Accidents"],
        width=bar_width,
        label="Serious Injury Accidents",
    )

    # Bar pour les accidents sans blessure
    ax.bar(
        bar_positions,
        df_query["Unscathed Accidents"],
        bottom=df_query["Death Accidents"] + df_query["Serious Injury Accidents"],
        width=bar_width,
        label="Unscathed Accidents",
    )

    # Configurations d'axe et de titre
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(df_query["Manoeuvre"], rotation=45, ha="right", fontsize=10)
    ax.set_xlabel("Manoeuvre Types")
    ax.set_ylabel("Number of Accidents")
    ax.set_title(title)
    ax.legend()

    return figure


# # Exemple d'utilisation :
fig_query12 = plotManoeuvreOutcomes(df_query12, "Manoeuvre Types and Accident Outcomes")
plt.show()  # Afficher la figure si nécessaire
