
use accidentsroutiers;
-- Query 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved

SELECT 
    usagers.id_usager,
    usagers.catu AS 'User Category',
    usagers.grav AS 'Severity',
    caracteristiques.mois AS 'Month',
    vehicules.catv AS 'Vehicle Category'
FROM 
    usagers
JOIN 
    caracteristiques
JOIN 
    vehicules
WHERE 
    usagers.catu = 3;

-- Query 2: Find the most common atmospheric condition during accidents.
	
SELECT 
    conditions_atmospheriques.conditions_atmospheriques,
    COUNT(*) AS 'Accident Count'
FROM 
    conditions_atmospheriques
JOIN 
    caracteristiques ON conditions_atmospheriques.id_conditions_atmospheriques = caracteristiques.atm
GROUP BY 
    conditions_atmospheriques.conditions_atmospheriques
ORDER BY 
    COUNT(*) DESC
LIMIT 1;


-- Query 3: Find the average number of vehicles involved in accidents for each category of the road.
SELECT 
    categorie_de_route.categorie_de_route,
    AVG(lieux.nbv) AS 'Average Vehicles'
FROM 
    lieux
JOIN 
    categorie_de_route ON lieux.catr = categorie_de_route.id_categorie_de_route
GROUP BY 
    categorie_de_route.categorie_de_route;
-- Query 4: Identify the top 5 locations (lieux) with the highest number of accidents.

SELECT 
    voie, v1, v2,
    COUNT(*) AS 'Accident Count'
FROM 
    lieux
GROUP BY 
    voie, v1, v2
ORDER BY 
    COUNT(*) DESC
LIMIT 5;


-- Query 6: List the different types of motorizations (type_motorisation) and the count of accidents for each type.
SELECT 
    type_motorisation.type_motorisation,
    COUNT(*) AS 'Accident Count'
FROM 
    type_motorisation
JOIN 
    vehicules ON type_motorisation.id_type_motorisation = vehicules.motor
GROUP BY 
    type_motorisation.type_motorisation;


