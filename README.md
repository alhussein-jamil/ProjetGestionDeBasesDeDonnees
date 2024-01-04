# ProjetGestionDeBasesDeDonnees
Projet Genie Logiciel 

## *Dataset* : 
  (No need to download it, it is already in the project)
  Bases de donnees annuelles des accidents corporels de la circulation routiere annees de 2005 a 2022
  https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/

## *Project Structure*:
- *config* : contains the config files
- *data* : contains the data files
- *schemas* : contains the generated schemas of the database, this includes the MCD(Modele Conceptuel de Donnees) and the MLD(Modele Logique de Donnees). 
- *src* : contains the source code of the project


## *Requirements*:
- python >= 3.10.11
install python : https://www.python.org/downloads/

## *Prepare Database*:
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

## *Installation*:
- create a virtual environment using venv, pyenv or conda
- install requirements.txt
```bash
pip install --upgrade -r requirements.txt
```

## *Run*:
```bash
python main.py 
```
you can use the following arguments:
  - -p : to show the plots only 
  - -a : to not run the application


## *Rapport sur overleaf*:
  https://www.overleaf.com/project/6567c4d2836490c0cd1b981b
  
## *Project Instructions* :
### Avancez au maximum sur ces points :
- Une description de votre projet, précisant bien les besoins auxquels elle va répondre.
- Le modèle Entité-Association de votre projet.
- Les services que vous proposez : questions à lesquelles il faut répondre ainsi que les requêtes SQL correspondantes.
- Data visualisation (ex. Plotly).
- Une interface pour l’exploitation des données.
  
### Déposez votre travail sur le Moodle (format PDF) :
- Une présentation de votre travail.
- Les scripts : de création et de peuplement de votre BDD.
- Les codes sources.
  
### Voici un exemple de plan :
- *partie 1*: présentation de l’équipe avec le taux de participation de chaque membre ainsi que sa tâche principale; (1 slide)
- *Partie 2*: Model Conceptuel de Données final : modèle Entité Association, que vous avez fait évoluer durant le projet; (1 slide pour la présentation), un 2ème slide est autorisé si vous avez intégrés des contraintes d’intégrités.
- *Partie 3* – Valorisation de la base de données : volumes (nombre d’années et d’enregistrements) (1 slide)
- *Partie 4* - Méthode: aspects originaux de ce que vous avez effectué (outils utilisés, scripts éventuels, données complémentaires ajoutées...) ET votre retour d'expérience (ce qui a été complexe, les verrous...) ; (1 à 3 slides)
- *Partie 5* - Résultats : présentation de requêtes (en utilisant plusieurs opérateurs SQL de cette liste : JOIN, GROUP BY avec COUNT/SUM/AVG, et WHERE…) et explication de ces résultats. (2 à 5 slides pour la présentation).
