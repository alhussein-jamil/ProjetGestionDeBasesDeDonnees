import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import MySQLConnection
from query import Query
import yaml 
from plotting import plot_query

class DataVisualizationApp:
    def __init__(self, root, query_instance, values, name):
        self.root = root

        self.labels = list(values.keys())
        self.values = list(values.values())

        # Paramètre modifiable
        self.selected_values = [tk.StringVar() for _ in values]
        for i,val in enumerate(self.values):
            self.selected_values[i].set(val[0])
        self.chart_frame = None

        # Créer l'interface utilisateur
        self.create_ui(query_instance)

    def create_ui(self, query_instance):
        # Frame principale
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        self.main_frame = main_frame

        # Frame pour les paramètres modifiables
        param_frame = ttk.Frame(main_frame, padding=(10, 10, 10, 10))
        param_frame.grid(row=0, column=0, sticky="nsew")

        for i in range(len(self.values)):
            label = ttk.Label(param_frame, text=f"{self.labels[i]}:")
            label.grid(row=i, column=0, sticky="w")

            value_combobox = ttk.Combobox(param_frame, values=self.values[i], textvariable=self.selected_values[i])
            value_combobox.grid(row=i, column=1, sticky="w")

        update_button = ttk.Button(param_frame, text="Mettre à jour", command=lambda: self.update_plotting(query_instance))
        update_button.grid(row=len(self.values), column=0, columnspan=2, sticky="w")

        # Frame pour le diagramme à barres
        self.chart_frame = ttk.Frame(main_frame)
        self.chart_frame.grid(row=1, column=0, sticky="nsew")

        # Zone de texte déroulante pour la requête SQL
        query_text = scrolledtext.ScrolledText(self.chart_frame, width=50, height=10, wrap=tk.WORD)
        query_text.insert(tk.END, query_instance.get_query())
        query_text.grid(row=0, column=0, padx=10, pady=10)

        # Initialiser le diagramme à barres
        self.create_plotting(query_instance)

        # Ajuster le redimensionnement des frames
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Ajuster le redimensionnement des paramètres modifiables
        param_frame.columnconfigure(0, weight=1)
        param_frame.columnconfigure(1, weight=1)

        # Ajuster le redimensionnement du diagramme à barres
        self.chart_frame.columnconfigure(0, weight=1)
        self.chart_frame.rowconfigure(0, weight=1)


    # def plot2D(self, df_query, x, y, z, title, scat, pie):
    #     fig, ax = plt.subplots()

    #     if scat:
    #         z_mapping = {"Indemne": 1, "Blessé léger": 2, "Blessé hospitalisé": 3, "Tué": 4}
    #         df_query["Severity"] = df_query[z].map(z_mapping)

    #         scatter = ax.scatter(
    #             df_query[x], df_query[y], c=df_query["Severity"], cmap="viridis", s=100
    #         )

    #         # Adding the color bar with severity names
    #         cbar = plt.colorbar(scatter, ax=ax, ticks=list(z_mapping.values()))
    #         cbar.set_ticklabels(list(z_mapping.keys()), rotation=30, fontsize=10)
    #         cbar.set_label("Severity")

    #         # Adding labels and title
    #         ax.set_xlabel(x)
    #         ax.set_ylabel(y)
    #         ax.set_title(title)

    #     elif pie:
    #         # Pie chart
    #         ax.pie(df_query[y], labels=df_query[x], autopct="%1.1f%%", startangle=140)
    #         ax.set_title(title)

    #     else:
    #         # Bar chart
    #         ax.bar(df_query[x], df_query[y])
    #         ax.set_xticklabels(df_query[x], rotation=30, ha="right")

    #         ax.set_xlabel(x)
    #         ax.set_ylabel(y)
    #         ax.set_title(title)

    #     return fig

    def create_plotting(self, query_instance):
        # Fetch the query result
        query_instance.set_args([selected_value.get() for selected_value in self.selected_values])

        # Execute the query and get the result as a DataFrame
        query_instance.execute_query()

        # Create the bar chart
        columns = query_instance.df.columns

        fig = plot_query(
            query_instance.df, 
            query_instance.title,
            query_instance.plot_3d,
            query_instance.scatter,
            query_instance.pie,
        )

        # Embed the Matplotlib figure into the frame
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

        # Adjust the x-axis labels
        ax = fig.axes[0]
        ax.set_xlabel(columns[0])

    def update_plotting(self, query_instance):
        # Fetch the query result
        query_instance.set_args([selected_value.get() for selected_value in self.selected_values])

        # Execute the query and get the result as a DataFrame
        query_instance.execute_query()

        # Clear the existing chart
        self.canvas.get_tk_widget().destroy()

        # Create the updated chart
        self.create_plotting(query_instance)

def run_app(query_instance_list):

    # Create the main application window
    root = tk.Tk()
    root.title("Multi-Window Data Visualization App")


    tabControl = ttk.Notebook(root)


    # Create an instance of DataVisualizationApp for each set of data
    for i, instance_data in enumerate(query_instance_list):
        # Create an instance of DataVisualizationApp for the current window
        app = DataVisualizationApp(root, query_instance=instance_data, values=instance_data.config['args'], name = "Query {}".format(i+1))
        tabControl.add(app.main_frame, text=f"Query {i+1}")

    tabControl.pack(expand=1, fill="both")

    # Start the main loop
    root.mainloop()

# Application principale
if __name__ == "__main__":

    config_dict = yaml.safe_load(open("config.yaml"))

    # Replace 'your_mysql_connection_here' with your actual MySQL connection
    mysql_connection = MySQLConnection(

            host= "localhost",
            user= "CyberTitan",
            password= "19216811",
            database= "accidentsroutiers",
        
    )

    queries_texts = []
    with open("modified_queries.sql") as f:
        for line in f:
            if "-- Query" in line:
                queries_texts.append("")
            queries_texts[-1] += line

    query_instance_list = []

    for i,query_text in enumerate(queries_texts):
        if f"query{i+1}" in config_dict:
            query_instance_list.append(Query(query_text, config_dict[f"query{i+1}"], mysql_connection))

    run_app(query_instance_list)