DB_CONFIG = {
    'host': 'localhost',
    'user': 'CyberTitan',
    'password': '19216811',
    'database': 'accidentsroutiers',
}

query = """
-- Query_2D 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
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
    usagers.catu=$choice$;
"""
from query import Query
import mysql

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)

import yaml 
with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

query = Query(query, config["query1"], connect_to_db())
breakpoint()