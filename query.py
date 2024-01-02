from mysql.connector import MySQLConnection
import pandas as pd 

class Query: 
    def __init__(self, query:str, config:dict, connection :MySQLConnection):
        self.connection = connection
        self.parse_query(query)
        self.config = config
        self.items = self.query_text.split("$choice$")
        self.args = []
        self.labels = []

        for k,v in self.config['args'].items():
            self.args.append(v)
            self.labels.append(k)

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