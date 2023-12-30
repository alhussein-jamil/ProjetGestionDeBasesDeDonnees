import mysql.connector
import plotly.express as px
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from collections import defaultdict

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def create_tabbed_panel(figures):
    root = tk.Tk()
    root.title("Figure Tabs")

    # Create a notebook (tabbed panel)
    notebook = ttk.Notebook(root)

    # Iterate through each figure and create a tab for it
    for index, figure in enumerate(figures):
        # Create a tab for each figure
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=f"Figure {index + 1}")

        # Embed the Matplotlib figure into the tab
        canvas = FigureCanvasTkAgg(figure, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Pack the notebook to make it visible
    notebook.pack(expand=1, fill="both")

    # Start the main loop
    root.mainloop()


def plot3d(df: pd.DataFrame, x: str, y: str, z: str, title: str, x_label: str, y_label: str, z_label: str, x_continuous: bool = True, y_continuous: bool = True, z_continuous: bool = True):

    if not x_continuous:
        df[x] = pd.Categorical(df[x])
    else:
        # make into buckets
        df[x] = pd.cut(df[x], 10)
        df[x] = pd.Categorical(df[x])


    if not y_continuous:
        df[y] = pd.Categorical(df[y])
    else:
        # make into buckets
        df[y] = pd.cut(df[y], 10)
        df[y] = pd.Categorical(df[y])

    if not z_continuous:
        df[z] = pd.Categorical(df[z])
    else:
        # make into buckets
        df[z] = pd.cut(df[z], 10)
        df[z] = pd.Categorical(df[z])

    # the one or two variables that are not continuous are categorical
    # the two categorical variables are plotted on the x and y axis
    # and the continuous variable is plotted as the height of the bars
    # transform the categorical variables to numerical representations
    x_categories = list(df[x].cat.categories)
    y_categories = list(df[y].cat.categories)

    df[z] = df[z].cat.codes if df[z].dtype == 'category' else df[z]
    df[x] = df[x].cat.codes if df[x].dtype == 'category' else df[x]
    df[y] = df[y].cat.codes if df[y].dtype == 'category' else df[y]

    # Combine z values for duplicate (x, y) pairs
    data_dict = defaultdict(float)
    for _, row in df.iterrows():
        data_dict[(row[x], row[y])] += row[z]

    # Unpack combined data
    x_combined, y_combined = zip(*data_dict.keys())
    z_combined = list(data_dict.values())

    # Create a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Use bar3d to create 3D bars
    ax.bar3d(x_combined, y_combined, [0] * len(z_combined), 0.8, 0.8, z_combined, shade=True,color = 'blue')

    # Set labels for the axes
    ax.set_xlabel(x_label, ha='right')
    ax.set_ylabel(y_label, ha='left')
    ax.set_zlabel(z_label)
    # Set tick labels for x and y axes
    ax.set_xticks(range(len(x_categories)))
    ax.set_xticklabels(x_categories)

    ax.set_yticks(range(len(y_categories)))
    ax.set_yticklabels(y_categories, rotation=90, fontsize=5)

    ax.set_title(title)

    return fig

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

quereys = [''
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
        quereys[i] += line
        if line.endswith(';\n'):
            i += 1
            quereys.append('')


def plot_query(df_query, title, plot_3D):
    columns = df_query.columns
    breakpoint()
    if plot_3D: 
        figs = []
        for i in range(len(columns)-2): 
            figs.append(
                plot3d(df_query, columns[0], columns[-2], columns[-1], title, columns[0], columns[-2], columns[-1], False, False, False)
            )
        create_tabbed_panel(figs)
    else:
        ...
    


figs = []
df_quereys = []

# sample_categorical_keys= {
#     'Severity': ['HospitalizedAccidents', 'FatalAccidents', 'LightInjuryAccidents'],
#     'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#               'November', 'December'],
#     'Vehicle Category': ['Car', 'Motorcycle', 'Truck', 'Bus', 'Bicycle', 'Pedestrian'],
# }

# sample_categorical_df = pd.DataFrame(columns=['Severity', 'Month', 'Vehicle Category'])
# listing = []
# for i in range(100):
#    listing.append(
#          {
#             'Severity': np.random.choice(sample_categorical_keys['Severity']),
#             'Month': np.random.choice(sample_categorical_keys['Month']),
#             'Vehicle Category': np.random.choice(sample_categorical_keys['Vehicle Category']),
#             }
#     )

# three_continuous_keys = ['HospitalizedAccidents', 'FatalAccidents', 'LightInjuryAccidents']
# data = {
#     'HospitalizedAccidents': np.random.randint(0, 100, 100),
#     'FatalAccidents': np.random.randint(0, 100, 100),
#     'LightInjuryAccidents': np.random.randint(0, 100, 100),
#     'Month': np.random.randint(1, 12, 100),
# }
# fig = plot3d(pd.DataFrame(data), 'Month', 'HospitalizedAccidents', 'FatalAccidents', 'Accident Severity by Month and Vehicle Category', 'Months', 'Vehicle Category', 'Severity', True, True, True)
# breakpoint()



# sample_categorical_df = pd.DataFrame(listing)

# fig = plot3d(sample_categorical_df, 'Month', 'Vehicle Category', 'Severity', 'Accident Severity by Month and Vehicle Category', 'Months', 'Vehicle Category', 'Severity', False, False, False)


# for querey in quereys:
#     df_quereys.append(execute_query(querey))
#     # breakpoint()
# import matplotlib.pyplot as plt
# # Create a 3D bar plot
# df = execute_query(quereys[14])

# # Créer le graphique à barres en 3D avec Matplotlib
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111, projection='3d')

# # Créer une séquence d'indices pour les manœuvres
# x_indices = range(len(df['ManeuverType']))
# # Adjust the space between the bars on the y-axis
# bar_width = 0.8
# ax.bar3d(x_indices, 0, 0, bar_width, 0.2, df['HospitalizedAccidents'], label='Hospitalized Accidents', color='blue', alpha=1)
# ax.bar3d(x_indices, 1, 0, bar_width, 0.2, df['FatalAccidents'], label='Fatal Accidents', color='red', alpha=1)
# ax.bar3d(x_indices, 2, 0, bar_width, 0.2, df['LightInjuryAccidents'], label='Light Injury Accidents', color='green', alpha=1)

# # # Create the 3D bars for each type of accident
# # ax.bar(x_indices, df['HospitalizedAccidents'], zs=0, zdir='y', width=bar_width, label='Hospitalized Accidents', color='blue', alpha=1)
# # ax.bar(x_indices, df['FatalAccidents'], zs=1, zdir='y', width=bar_width, label='Fatal Accidents', color='red', alpha=1)
# # ax.bar(x_indices, df['LightInjuryAccidents'], zs=2, zdir='y', width=bar_width, label='Light Injury Accidents', color='green', alpha=1)

# # Customize the x-axis
# ax.set_xticks(x_indices)
# ax.set_xticklabels(df['ManeuverType'], rotation=45, ha='right')

# # Customize the y-axis
# ax.set_yticks([0, 1, 2])
# ax.set_yticklabels(['HospitalizedAccidents', 'FatalAccidents', 'LightInjuryAccidents'])

# # Customize the z-axis
# ax.set_zlabel('Number of Accidents')

# # Add a legend
# ax.legend()

# # Show the 3D bar chart
# plt.show()


# Query 1: Retrieve information about accidents involving pedestrians
# df_query = execute_query(quereys[0])
# #print column name
# fig = plot3d(df_query, 'Month', 'Vehicle Category', 'Severity', 'Accident Severity by Month and Vehicle Category', 'Months', 'Vehicle Category', 'Severity', False, False, False)
# figs.append(fig)



#
# # df_quereys.append(df_query)
# # fig.show()
# fig.show()


# fig = px.bar(df_query, x='Month', y='Severity', color='Vehicle Category',
#              labels={'Severity': 'Severity', 'Month': 'Months', 'Vehicle Category': 'Vehicle Category'},
#              title='Accident Severity by Month and Vehicle Category',
#              barmode='group')
# fig.show()
# df_quereys.append(df_query)

# import matplotlib.pyplot as plt
# # Create a 3D bar plot
# df = df_query

# breakpoint()
# # Convert categorical variables to numerical representations
# df['Severity'] = pd.Categorical(df['Severity'])
# df['Month'] = pd.Categorical(df['Month'])
# df['Vehicle Category'] = pd.Categorical(df['Vehicle Category'])

# df['Severity'] = df['Severity'].cat.codes
# df['Month'] = df['Month'].cat.codes
# df['Vehicle Category'] = df['Vehicle Category'].cat.codes

# # Create a 3D bar plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# # Group the data by Severity, Month, and Vehicle Category and count occurrences
# grouped_data = df.groupby(['Severity', 'Month', 'Vehicle Category']).size().reset_index(name='Count')

# # Plot the 3D bar with 'Vehicle Category' representing Y, 'Severity' representing height, and 'Month' representing X
# for i, row in grouped_data.iterrows():
#     ax.bar3d(row['Month'], row['Vehicle Category'], 0, 0.8, 0.8, row['Count'], color=plt.cm.viridis(row['Severity'] / max(grouped_data['Severity'])), alpha=0.8)

# # Set labels
# ax.set_xlabel('Month')
# ax.set_ylabel('Vehicle Category')
# ax.set_zlabel('Count')
# ax.set_title('Accidents Involving Pedestrians')

# # Add a legend showing the different severities colors and names
# severity_labels = df
# severity_colors = [plt.cm.viridis(i / max(grouped_data['Severity'])) for i in range(len(severity_labels))]
# legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color) for label, color in zip(severity_labels, severity_colors)]
# ax.legend(handles=legend_elements)

# # Show the plot
# plt.show()
# # Query 2: Find the most common atmospheric condition during accidents.
# df_query = execute_query(quereys[1])
# fig = plot3d(
#     df_query, 'conditions_atmospheriques', 'Accident Count',  'Accident Severity by Month and Vehicle Category', 'Months', 'Vehicle Category', 'Severity', False, False, False
# )
# fig = px.bar(df_query, x='conditions_atmospheriques', y='Accident Count',
#              labels={'conditions_atmospheriques': 'Atmospheric Conditions', 'Accident Count': 'Accident Count'},
#              title='Top 5 Atmospheric Conditions by Accident Count',
#              category_orders={"conditions_atmospheriques": df_query['conditions_atmospheriques'].tolist()[:5]},  # Preserve order
#              )
# df_quereys.append(df_query)
# figs.append(fig)


# # Query 3: Find the average number of accidents for each category of the road.
# df_query = execute_query(quereys[2])
# fig = px.bar(df_query, x='Categorie De Route', y='Avg Num Accidents',
#              labels={'Categorie De Route': 'Category of Road', 'Avg Num Accidents': 'Average Number of Accidents'},
#              title='Average Number of Accidents for Each Category of Road')
# df_quereys.append(df_query)
# figs.append(fig)

# # Query 4: Identify the top 5 locations (lieux) with the highest number of accidents.
# df_query = execute_query(quereys[3])
# fig = px.bar(df_query, x='voie', y='Accident Count',
#              labels={'Location': 'Location', 'Accident Count': 'Accident Count'},
#              title='Top 5 Locations with the Highest Number of Accidents')
# df_quereys.append(df_query)
# figs.append(fig)



# figs[-1].show()

# for fig in figs:
#     fig.show()


# df_query = execute_query(quereys[4])
# fig = plot3d(df_query, "conditions_atmospheriques", "categorie_de_route", "lumiere", "Accident Severity by Month and Vehicle Category", "Months", "Vehicle Category", "Severity", False, False, False)
# figs.append(fig)

# create_tabbed_panel(figs)

#query 10
df_query = execute_query(quereys[9])
breakpoint()
plot_query(df_query, titles[9], plot_3D[9])
#print column names 
# print(df_query.columns)
# fig = plot3d(df_query, 
#             "Safety Equipment 1",
#             "Severity",
#             "Total Accidents",
#             "Accident Severity by Month and Vehicle Category",
#             "Months",
#             "Vehicle Category",
#             "Severity",
#             False,
#             False,
#             False
#             )
# create_tabbed_panel([fig])
# breakpoint()
