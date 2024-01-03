import tkinter as tk
from tkinter import scrolledtext, ttk

import matplotlib.pyplot as plt
import yaml
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mysql.connector import MySQLConnection

from plotting import plot_query
from query import Query


class DataVisualizationApp:
    def __init__(self, root, query_instance, values, mapping, name):
        self.root = root

        self.labels = list(values.keys())
        self.values = list(values.values())
        self.mapping = list(mapping.values())

        # Paramètre modifiable
        self.selected_values = [tk.StringVar() for _ in values]
        for i, val in enumerate(self.mapping):
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

        for i in range(len(self.mapping)):
            label = ttk.Label(param_frame, text=f"{self.labels[i]}:")
            label.grid(row=i, column=0, sticky="w")

            # Increase the font size in the Combobox
            value_combobox = ttk.Combobox(
                param_frame,
                values=self.mapping[i],
                textvariable=self.selected_values[i],
                style='TCombobox',  # This style is added for increased font size
            )
            value_combobox.grid(row=i, column=1, sticky="w")

        update_button = ttk.Button(
            param_frame,
            text="Update",
            command=lambda: self.update(query_instance),
        )
        update_button.grid(row=len(self.mapping), column=0, columnspan=2, sticky="w")

        # Frame pour le diagramme
        self.chart_frame = ttk.Frame(main_frame)
        self.chart_frame.grid(row=1, column=0, sticky="nsew")


        # Zone de texte déroulante pour la requête SQL
        self.query_text = scrolledtext.ScrolledText(
            self.chart_frame, width=80, height=30, wrap=tk.WORD
        )
        self.query_text.insert(tk.END, query_instance.get_query())
        self.query_text.grid(row=0, column=0, padx=10, pady=10)

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

    def create_plotting(self, query_instance):
        # Fetch the query result
        query_instance.set_args(
            [
                str(self.values[i][self.mapping[i].index(var.get())])
                for i, var in enumerate(self.selected_values)
            ]
        )

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
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

        # Adjust the x-axis labels
        ax = fig.axes[0]
        ax.set_xlabel(columns[0])

    def update(self, query_instance):
        # Fetch the query result
        query_instance.set_args(
            [
                str(self.values[i][self.mapping[i].index(var.get())])
                for i, var in enumerate(self.selected_values)
            ]
        )
        

        # Execute the query and get the result as a DataFrame
        query_instance.execute_query()
        

        self.query_text.delete("1.0", tk.END)
        

        self.query_text.insert(tk.END, query_instance.get_query())

        self.update_plotting(query_instance)

    def update_plotting(self, query_instance):
        # Clear the existing chart
        self.canvas.get_tk_widget().destroy()

        # Create the updated chart
        self.create_plotting(query_instance)


def run_app(query_instance_list):
    # Create the main application window
    root = tk.Tk()
    root.title("Genie Logiciel Visualization App")

    tabControl = ttk.Notebook(root)

    # Create an instance of DataVisualizationApp for each set of data
    for i, instance_data in enumerate(query_instance_list):
        # Create an
        #  instance of DataVisualizationApp for the current window
        app = DataVisualizationApp(
            root,
            query_instance=instance_data,
            values=instance_data.config["args"],
            mapping=instance_data.config["mapping"],
            name="Query {}".format(i + 1),
        )
        tabControl.add(app.main_frame, text=f"Query {i+1}")

    tabControl.pack(expand=1, fill="both")

    # Start the main loop
    root.mainloop()


# Application principale
if __name__ == "__main__":
    config_dict = yaml.safe_load(open("config.yaml"))

    # Replace 'your_mysql_connection_here' with your actual MySQL connection
    # mysql_connection = MySQLConnection(
    #     host="localhost",
    #     user="CyberTitan",
    #     password="19216811",
    #     database="accidentsroutiers",
    # )

    mysql_connection = MySQLConnection(
        host="localhost",
        user="user4projet",
        password="Hellogenielogiciel2023",
        database="accidentsroutiers",
        auth_plugin="mysql_native_password",
    )

    queries_texts = []
    with open("modified_queries.sql") as f:
        for line in f:
            if "-- Query" in line:
                queries_texts.append("")
            queries_texts[-1] += line

    query_instance_list = []

    for i, query_text in enumerate(queries_texts):
        if f"query{i+1}" in config_dict:
            query_instance_list.append(
                Query(query_text, config_dict[f"query{i+1}"], mysql_connection)
            )

    run_app(query_instance_list)
