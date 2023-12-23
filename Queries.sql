
use accidentsroutiers;
-- Query 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved

INSERT INTO accidentsroutiers.categorie_du_vehicule
VALUES
('-1',
'unconnue');

SELECT 
    usagers.id_usager,
    gravite.gravite AS 'Severity',
    caracteristiques.mois AS 'Month',
    categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category'
FROM 
    usagers
JOIN 
    caracteristiques on ( Accident_Id = Num_Acc)
JOIN 
    vehicules
using ( Num_Acc)
JOIN
	categorie_du_vehicule on ( vehicules.catv = categorie_du_vehicule.id_categorie_du_vehicule)
JOIN
	gravite on ( usagers.grav = gravite.id_gravite)
JOIN 
	categorie_usager on ( usagers.catu = categorie_usager.id_categorie_usager)
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
LIMIT 5;


-- Query 3: Find the average number of accidents for each category of the road.
SELECT
    cat AS "Categorie De Route",
    c_acc / (SELECT COUNT(*) FROM categorie_de_route) AS "Avg Num Accidents"
FROM (
    SELECT
        categorie_de_route.categorie_de_route AS cat,
        COUNT(*) AS c_acc
    FROM
        lieux
    JOIN
        categorie_de_route ON categorie_de_route.id_categorie_de_route = catr
    GROUP BY
        catr
) AS T;

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

-- Query 5: List the different types of motorizations (type_motorisation) and the count of accidents for each type.
SELECT 
    type_motorisation.type_motorisation,
    COUNT(*) AS 'Accident Count'
FROM 
    type_motorisation
JOIN 
    vehicules ON type_motorisation.id_type_motorisation = vehicules.motor
GROUP BY 
    type_motorisation.type_motorisation;

