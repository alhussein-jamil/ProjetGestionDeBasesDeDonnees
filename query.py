from mysql.connector import MySQLConnection
import pandas as pd 

class Query: 
    def __init__(self, query:str, config:dict, connection :MySQLConnection):
        self.connection = connection
        self.parse_query(query)
        self.config = config
        self.items = self.query_text.split("$choice$")
        self.args = []
        print(self.config)
        for item in self.config['args']:
            self.args.append(item)

        self.current_args = [arg[0] for arg in self.args]
        self.set_args(self.current_args)
        self.df = None 

    def get_query(self):
        return self.query_text
    # Function to execute a query and return a DataFrame
    def execute_query(self):
        self.df = pd.read_sql_query(self.query_text, self.connection)

    def set_args(self, args):   
        self.current_args = args
        self.query_text = self.items[0]
        for i in range(1, len(self.items)):
            self.query_text += str(self.current_args[i-1])
            self.query_text += self.items[i]

    def parse_query(self, query): 
        lines = query.split("\n")
        self.query_text = ""
        for line in lines:
            if "--" in line or "USE" in line:
                if "title" in line:
                    self.title = line.split("title")[1].split("=")[1].strip().replace("'", "")
                else:
                    if "Query" in line:
                        self.plot_3d = "3D" in line
                        self.scatter = "scatter" in line
                        self.pie = "pie" in line
                continue
            self.query_text += line
            self.query_text += "\n"


if __name__ == "__main__":

    # Replace 'your_query_here' with your actual SQL query
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

    # Replace 'your_config_here' with your actual configuration dictionary
    config_dict = {
        'args': [
            '3'
        ]
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

    # Print the original query
    print("Original Query:")
    print(query_instance.get_query())

    # Set new arguments if needed
    new_args = ['2']
    query_instance.set_args(new_args)

    # Print the modified query with new arguments
    print("\nModified Query:")
    print(query_instance.get_query())

    # Execute the query and get the result as a DataFrame
    query_instance.execute_query()

    # Access the DataFrame
    result_dataframe = query_instance.df

    # Display the result
    print("\nQuery Result:")
    print(result_dataframe)
