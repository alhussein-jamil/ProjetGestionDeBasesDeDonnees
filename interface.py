import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd 
# Fonction pour exécuter une requête SQL et récupérer les résultats
def execute_query(query):
    connection = mysql.connector.connect(
        host='localhost',
        user='user4projet',
        password='Hellogenielogiciel2023',
        database='accidentsroutiers',
        auth_plugin='mysql_native_password'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    result = pd.read_sql_query(result,connection)
    return result

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization App")

        # Paramètre modifiable
        self.selected_category = tk.StringVar()
        self.selected_category.set("3")  # Valeur par défaut

        # Créer l'interface utilisateur
        self.create_ui()

    def create_ui(self):
        # Frame principale
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Frame pour le paramètre modifiable
        param_frame = ttk.Frame(main_frame, padding=(10, 10, 10, 10))
        param_frame.grid(row=0, column=0, sticky="nsew")

        label = ttk.Label(param_frame, text="Catégorie Usager:")
        label.grid(row=0, column=0, sticky="w")

        category_combobox = ttk.Combobox(param_frame, values=["1", "2", "3"], textvariable=self.selected_category)
        category_combobox.grid(row=0, column=1, sticky="w")

        update_button = ttk.Button(param_frame, text="Mettre à jour", command=self.update_chart)
        update_button.grid(row=0, column=2, sticky="w")

        # Frame pour le diagramme à barres
        chart_frame = ttk.Frame(main_frame)
        chart_frame.grid(row=1, column=0, sticky="nsew")

        # Zone de texte déroulante pour la requête SQL
        query_text = scrolledtext.ScrolledText(chart_frame, width=50, height=10, wrap=tk.WORD)
        query_text.insert(tk.END, "SELECT caracteristiques.mois AS 'Month',\n"
                                 "       categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category',\n"
                                 "       gravite.gravite AS 'Severity'\n"
                                 "FROM usagers\n"
                                 "JOIN caracteristiques ON Accident_Id = Num_Acc\n"
                                 "JOIN vehicules USING (Num_Acc)\n"
                                 "JOIN categorie_du_vehicule ON vehicules.catv = categorie_du_vehicule.id_categorie_du_vehicule\n"
                                 "JOIN gravite ON usagers.grav = gravite.id_gravite\n"
                                 "JOIN categorie_usager ON usagers.catu = categorie_usager.id_categorie_usager\n"
                                 "WHERE usagers.catu = 3;")
        query_text.grid(row=0, column=0, padx=10, pady=10)

        # Initialiser le diagramme à barres
        self.create_bar_chart(chart_frame)

        # Ajuster le redimensionnement des frames
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def create_bar_chart(self, chart_frame):
            # Fetch the query result
        self.query_result = execute_query(f"SELECT caracteristiques.mois AS 'Month',\n"
                                          f"       categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category',\n"
                                          f"       gravite.gravite AS 'Severity'\n"
                                          f"FROM usagers\n"
                                          f"JOIN caracteristiques ON Accident_Id = Num_Acc\n"
                                          f"JOIN vehicules USING (Num_Acc)\n"
                                          f"JOIN categorie_du_vehicule ON vehicules.catv = categorie_du_vehicule.id_categorie_du_vehicule\n"
                                          f"JOIN gravite ON usagers.grav = gravite.id_gravite\n"
                                          f"JOIN categorie_usager ON usagers.catu = categorie_usager.id_categorie_usager\n"
                                          f"WHERE usagers.catu = {self.selected_category.get()};")

        # Convert the values to integers, replacing non-numeric values with 0
        values = [int(value) if str(value).isdigit() else 0 for value in self.query_result[:]['Severity']]

        # Mapping des valeurs textuelles de Severity à des valeurs numériques
        z_mapping = {'Indemne': 1, 'Blessé léger': 2, 'Blessé hospitalisé': 3, 'Tué': 4}

        # Create the scatter plot with Matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        breakpoint()
        scatter = ax.scatter(
            self.query_result[:]['Month'], self.query_result[:]['Vehicle Category'],
            c=values, cmap='viridis', s=100
        )

        # Add color bar with severity names
        cbar = plt.colorbar(scatter, ax=ax, ticks=list(z_mapping.values()))
        cbar.set_ticklabels(list(z_mapping.keys()), rotation=30, fontsize=10)
        cbar.set_label('Severity')

        # Add labels and title
        ax.set_xlabel('Month')
        ax.set_ylabel('Vehicle Category')
        ax.set_title('Accidents Severity')

        # Embed the Matplotlib figure into the frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)



    def update_chart(self):
        # Mettre à jour le diagramme à barres en fonction du paramètre modifiable
        self.query_result = execute_query(f"SELECT caracteristiques.mois AS 'Month',\n"
                                          f"       categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category',\n"
                                          f"       gravite.gravite AS 'Severity'\n"
                                          f"FROM usagers\n"
                                          f"JOIN caracteristiques ON Accident_Id = Num_Acc\n"
                                          f"JOIN vehicules USING (Num_Acc)\n"
                                          f"JOIN categorie_du_vehicule ON vehicules.catv = categorie_du_vehicule.id_categorie_du_vehicule\n"
                                          f"JOIN gravite ON usagers.grav = gravite.id_gravite\n"
                                          f"JOIN categorie_usager ON usagers.catu = categorie_usager.id_categorie_usager\n"
                                          f"WHERE usagers.catu = {self.selected_category.get()};")

        # Effacer le contenu du subplot
        plt.clf()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(self.query_result[0].keys(), self.query_result[0].values())
        ax.set_xlabel("Categories")
        ax.set_ylabel("Values")
        ax.set_title("Bar Chart")

        # Mettre à jour le contenu du canvas
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

# Application principale
if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizationApp(root)
    root.mainloop()
