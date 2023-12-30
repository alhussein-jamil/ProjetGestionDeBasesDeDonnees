import mysql.connector
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Replace these with your MySQL database credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'CyberTitan',
    'password': '19216811',
    'database': 'accidentsroutiers',
}
quereys = ['']
titles = []
plot_3D= []
scatter = []
figs = []
df_quereys = []

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

    # Run the application
    root.mainloop()

def plot3d(df: pd.DataFrame, x: str, y: str, z:str, t:str, title: str, x_label: str, y_label: str, z_label: str,  x_continuous: bool = True, y_continuous: bool = True, z_continuous: bool = True, t_continuous: bool = True):
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

    if not t_continuous: 
        df[t] = pd.Categorical(df[t])
    else:
        # make into buckets
        df[t] = pd.cut(df[t], 10)
        df[t] = pd.Categorical(df[t])


    # the one or two variables that are not continuous are categorical
    # the two categorical variables are plotted on the x and y axis
    # and the continuous variable is plotted as the height of the bars
    # transform the categorical variables to numerical representations
    x_categories = list(df[x].cat.categories)
    y_categories = list(df[y].cat.categories)
    t_categories = list(df[t].cat.categories)

    df[z] = df[z].cat.codes if df[z].dtype == 'category' else df[z]
    df[x] = df[x].cat.codes if df[x].dtype == 'category' else df[x]
    df[y] = df[y].cat.codes if df[y].dtype == 'category' else df[y]
    df[t] = df[t].cat.codes if df[t].dtype == 'category' else df[t]

    # Combine z values for duplicate (x, y) pairs
    data_dict = {}
    for _, row in df.iterrows():
        if row[t] not in data_dict:
            data_dict[row[t]] = defaultdict(int)
        data_dict[row[t]][(row[x], row[y])] += row[z]

    # Create a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Use bar3d to create 3D bars
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink', 'black', 'brown', 'gray']
    offsets = {}
    for i, ti in enumerate(data_dict.keys()):
        x_combined, y_combined = zip(*data_dict[ti].keys())
        z_combined = list(data_dict[ti].values())
        local_offset = [offsets.get((x, y), 0) for x, y in zip(x_combined, y_combined)]
        ax.bar3d(x_combined, y_combined,local_offset, 0.8, 0.8,  z_combined, shade=True,color = colors[i % len(colors)], alpha=1)
        offsets.update({(x, y): z + offset for x, y, z, offset in zip(x_combined, y_combined, z_combined, local_offset)})

    # Set labels for the axes
    ax.set_xlabel(x_label, ha='right')
    ax.set_ylabel(y_label, ha='left')
    ax.set_zlabel(z_label)

    # Set tick labels for x and y axes
    ax.set_xticks(range(len(x_categories)))
    ax.set_xticklabels(x_categories, rotation=45, fontsize=5)

    ax.set_yticks(range(len(y_categories)))
    ax.set_yticklabels(y_categories, rotation=90, fontsize=5)

    ax.set_title(title)
    ax.legend(t_categories)
    return fig

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)

# Function to execute a query and return a DataFrame
def execute_query(query):
    connection = connect_to_db()
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

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
                        plot_3D.append(True)
                    else:
                        plot_3D.append(False)
                    if "scatter" in line:
                        scatter.append(True)
                    else:
                        scatter.append(False)
            continue
        quereys[i] += line
        if line.endswith(';\n'):
            i += 1
            quereys.append('')
#remove last empty query
quereys.pop()


def plot_query(df_queries, titles, Plot_3D, scatter):
    figs = []
    for df_query, title, plot_3D,scat in zip(df_queries, titles, Plot_3D, scat):
        if plot_3D: 
            #add an artifical column if len(columns) < 4
            if len(df_query.columns) < 4:
                df_query['artificial'] = 0
            columns = df_query.columns
            figs.append(
                plot3d(df_query,*columns[:4], title, *columns[:3], False, False, False, False)
            )
        else:
            pass 
            # plot_2D(df_query, title, scat)

    create_tabbed_panel(figs)

plot_query([execute_query(query) for query in quereys], titles, plot_3D, scatter)
