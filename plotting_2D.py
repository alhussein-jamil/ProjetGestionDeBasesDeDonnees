import mysql.connector
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Replace these with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'user4projet',
    'password': 'Hellogenielogiciel2023',
    'database': 'accidentsroutiers',
    'auth_plugin' : "mysql_native_password"
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

queries = [''
]
titles =[

]
plot_3D= [

]
    #ignore comments starting with -- and each query starts with SELECT and ends with ; annd can be on multiple lines
with open('Queries.sql') as f:
    i = 0
    for line in f:
        if "--" in line or "USE" in line:
            if "title" in line:
                titles.append(line.split("title")[1].split("=")[1].strip().replace("'", ""))
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
        if line.endswith(';\n'):
            i += 1
            print(queries[-1])
            breakpoint()
            queries.append('')

# Query 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
query1 = queries[0]
print(query1)
breakpoint()
df_query1 = execute_query(query1)


# Plot for Query 1
fig = px.bar(df_query1, x='Month', y='Severity', color='Vehicle Category',
             labels={'Severity': 'Severity', 'Month': 'Month', 'Vehicle Category': 'Vehicle Category'},
             title='Accident Severity by Month and Vehicle Category',
             barmode='group')

fig.show()


fig = px.bar(df_query1, x='Vehicle Category', y='Month', color='Severity', title='Accidents Severity')
fig.show()

# Query 2: Find the most common atmospheric condition during accidents.
query2 = queries[1]
print(query2)
breakpoint()
df_query2 = execute_query(query2)
# Plot for Query 2

fig = px.bar(df_query2, x='Conditions Atmospheriques', y='Accident Count', title='Most Common Atmospheric Conditions')
fig.show()

# Query 3: Find the average number of accidents for each category of the road.
query3 = queries[2]
df_query3 = execute_query(query3)
# Plot for Query 3

fig = px.bar(df_query3, x='Categorie De Route', y='Avg Num Accidents', title='Average Number of Accidents for Each Road Category')
fig.show()

# Query 4: List the different types of motorizations (type_motorisation) and the count of accidents for each type.
query4 = queries[3]
df_query4 = execute_query(query4)
# Plot for Query 4
fig = px.bar(df_query4, x='Type of Motorization', y='Accident Count', title='Accidents by Motorization Type')
fig.show()

# Query 5: Retrieve the distribution of accidents across different categories such as time of day (lum), weather conditions (atm), and road types (catr).
query5 = queries[4]
df_query5 = execute_query(query5)
# Plot for Query 5
fig = px.bar(df_query5, x='Weather Conditions', y='accident_count', color='Lighting Conditions', barmode='group', title='Accident Distribution by Conditions')
fig.show()

# Query 6: Analyze the severity of accidents by looking at the number of fatalities, injuries, and the types of vehicles involved.
query6 = queries[5]
df_query6 = execute_query(query6)
# Plot for Query 7
fig = px.pie(df_query6, values='severity_count', names='severity', title='Severity of Accidents')
fig.show()

#  Query 7: Explore the involvement of different vehicle categories (catv) in accidents and analyze their contribution to overall road safety.
query7 = queries[6]
df_query7 = execute_query(query7)
# Plot for Query 7
fig = px.pie(df_query7, values='Total Accident', names='Vehicle Category', title='Accidents by Vehicle Category')
fig.show()

# Query 8: Examine the types of collisions (col) that occur most frequently. Determine if certain collision types are associated with higher injury rates.
query8 = queries[7]
df_query8 = execute_query(query8)
# Plot for Query 8
fig = px.bar(df_query8, x='Collision Type', y='Total Accident', title='Most Frequent Collision Types')
fig.show()

# Query 9: Analyze the age and gender (sexe) distribution of individuals involved in accidents and determine if there are age or gender-specific patterns. Safety Equipment Usage:
query9 = queries[8]
df_query9 = execute_query(query9)
# Plot for Query 9
fig = px.bar(df_query9, x='Gender', y='Average Equipment Use Score', title='Average Equipment Use Score by Gender')
fig.show()

# Probleme de query 
# Query 10: Explore the usage of safety equipment (secu1, secu2, secu3) and its correlation with injury severity. Driver Analysis:
query10 = queries[9]
df_query10 = execute_query(query10)
# Plot for Query 10
fig = px.bar(df_query10, x=['SafetyEquipment1', 'SafetyEquipment2', 'SafetyEquipment3'], y='TotalAccidents', color='InjurySeverity', title='Safety Equipment Usage and Injury Severity')
fig.show()

# Query 11: Focus on pedestrian-related data (catu=3) to understand the locations (locp) and actions (actp) leading to pedestrian accidents. Vehicle Manoeuvres:
query11 = queries[10]
df_query11 = execute_query(query11)
# Plot for Query 12
fig = px.bar(df_query11, x="Location of Pedestrian", y="Total Accidents", color="Action of Pedestrian", title='Pedestrian Accidents')
fig.show()


# Query 12 Investigate the types of manoeuvres performed by vehicles before accidents and their impact on collision outcomes.
query12 = queries[11]
df_query12 = execute_query(query12)
# Plot for Query 12
fig = go.Figure(data=[
    go.Bar(name='Fatal Accidents', x=df_query12['ManeuverType'], y=df_query12['FatalAccidents']),
    go.Bar(name='Hospitalized Accidents', x=df_query12['ManeuverType'], y=df_query12['HospitalizedAccidents']),
    go.Bar(name='Light Injury Accidents', x=df_query12['ManeuverType'], y=df_query12['LightInjuryAccidents'])
])

fig.update_layout(barmode='stack', title='Manoeuvre Types and Accident Outcomes')
fig.show()