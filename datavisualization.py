import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import MySQLConnection
from query import Query

class DataVisualizationApp:
    def __init__(self, root, query_instance, values):
        self.root = root
        self.root.title("Data Visualization App")

        # Paramètre modifiable
        self.selected_value = tk.StringVar()
        self.values = values
        self.selected_value.set(values[0])  # Valeur par défaut
        self.chart_frame = None

        # Créer l'interface utilisateur
        self.create_ui(query_instance)

    def create_ui(self, query_instance):
        # Frame principale
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Frame pour le paramètre modifiable
        param_frame = ttk.Frame(main_frame, padding=(10, 10, 10, 10))
        param_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(param_frame, text="Catégorie Usager:")
        label.grid(row=0, column=0, sticky="w")

        value_combobox = ttk.Combobox(param_frame, values=self.values, textvariable=self.selected_value)
        value_combobox.grid(row=0, column=1, sticky="w")

        update_button = ttk.Button(param_frame, text="Mettre à jour", command=lambda: self.update_plotting(query_instance))
        update_button.grid(row=0, column=2, sticky="w")

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

    def plot2D(self, df_query, x, y, z, title, scat, pie):
        fig, ax = plt.subplots()

        if scat:
            z_mapping = {"Indemne": 1, "Blessé léger": 2, "Blessé hospitalisé": 3, "Tué": 4}
            df_query["Severity"] = df_query[z].map(z_mapping)

            scatter = ax.scatter(
                df_query[x], df_query[y], c=df_query["Severity"], cmap="viridis", s=100
            )

            # Adding the color bar with severity names
            cbar = plt.colorbar(scatter, ax=ax, ticks=list(z_mapping.values()))
            cbar.set_ticklabels(list(z_mapping.keys()), rotation=30, fontsize=10)
            cbar.set_label("Severity")

            # Adding labels and title
            ax.set_xlabel(x)
            ax.set_ylabel(y)
            ax.set_title(title)

        elif pie:
            # Pie chart
            ax.pie(df_query[y], labels=df_query[x], autopct="%1.1f%%", startangle=140)
            ax.set_title(title)

        else:
            # Bar chart
            ax.bar(df_query[x], df_query[y])
            ax.set_xticklabels(df_query[x], rotation=30, ha="right")

            ax.set_xlabel(x)
            ax.set_ylabel(y)
            ax.set_title(title)

        return fig

    def create_plotting(self, query_instance):
        # Fetch the query result
        query_instance.set_args(self.selected_value.get())

        # Execute the query and get the result as a DataFrame
        query_instance.execute_query()

        # Create the bar chart
        columns = query_instance.df.columns
        fig = self.plot2D(
            query_instance.df,
            *columns[:2],
            title=query_instance.title,
            scat=query_instance.scatter,
            z=None if len(columns) < 3 else columns[2],
            pie=query_instance.pie
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
        query_instance.set_args(self.selected_value.get())

        # Execute the query and get the result as a DataFrame
        query_instance.execute_query()

        # Clear the existing chart
        self.canvas.get_tk_widget().destroy()

        # Create the updated chart
        self.create_plotting(query_instance)




# Application principale
if __name__ == "__main__":
    query_string = """
        -- Query_scatter2D 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
        -- title='Accident Severity by Month and Vehicle Category'
        SELECT 
            caracteristiques.mois AS 'Month',
            categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category',
            gravite.gravite AS 'Severity'
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
            usagers.catu = $choice$;
        """

    config_dict = {
        'args': ['3']
    }

    # Replace 'your_mysql_connection_here' with your actual MySQL connection
    mysql_connection = MySQLConnection(
        host='localhost',
        user='user4projet',
        password='Hellogenielogiciel2023',
        database='accidentsroutiers',
        auth_plugin='mysql_native_password'
    )

    # Create an instance of the Query class
    query_instance = Query(query_string, config_dict, mysql_connection)

    # Execute the query and get the result as a DataFrame
    query_instance.execute_query()

    # Access the DataFrame
    result_dataframe = query_instance.df

    # Display the result
    print("\nQuery Result:")
    print(result_dataframe)

    root = tk.Tk()
    app = DataVisualizationApp(root, query_instance, ["1", "2", "3"])
    root.mainloop()
