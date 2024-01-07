# Projet Gestion De Bases De Donnees
## 📁 *Dataset* : 
  (No need to download it, it is already in the project)
  Bases de donnees annuelles des accidents corporels de la circulation routiere annees de 2005 a 2022
  https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/
  
## 🤝 *Autors* :
Alhussein JAMIL
Lynda FEDDAK

## 🎯 *Project Structure*:
- *config* : contains the config files
- *data* : contains the data files
- *schemas* : contains the generated schemas of the database, this includes the MCD(Modele Conceptuel de Donnees) and the MLD(Modele Logique de Donnees). 
- *src* : contains the source code of the project


## ⚙️ *Requirements*:
- python >= 3.10.11
install python : https://www.python.org/downloads/

## ⬇️ *Installation*:
- create a virtual environment using venv, pyenv or conda
- install requirements.txt
```bash
pip install --upgrade -r requirements.txt
```

## ⌛ *Prepare Database*:
We use mysql database, we provide the .sql script to create the database and tables.
- create a database named "accidentsroutiers": 
```bash
mysql -u root -p
CREATE DATABASE accidentsroutiers;
```
- create tables and populate them:
```bash
mysql -u root -p accidentsroutiers < accidentsroutiers.sql
```
- create a user named "some_user_name" with password "some_password" and grant him all privileges on the database "accidentsroutiers".
- change the config file config/user_config.yaml with the user name and password you created.

## 🚀 *Run*:
```bash
python main.py 
```
you can use the following arguments:
  - -p : to show the plots only 
  - -a : to not run the application
