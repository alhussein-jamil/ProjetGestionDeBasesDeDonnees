-- Query 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
USE accidentsroutiers;

-- INSERT INTO accidentsroutiers.categorie_du_vehicule
-- VALUES
-- ('-1', 'unconnue');

SELECT 
    usagers.id_usager,
    gravite.gravite AS 'Severity',
    caracteristiques.mois AS 'Month',
    categorie_du_vehicule.categorie_du_vehicule AS 'Vehicle Category'
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

-- Query 7: Retrieve the distribution of accidents across different categories such as time of day (lum), weather conditions (atm), and road types (catr).
SELECT 
    conditions_atmospheriques.conditions_atmospheriques,
    categorie_de_route.categorie_de_route,
    lumiere.lumiere,
    infrastructure.infrastructure,
    COUNT(*) as accident_count
FROM 
    caracteristiques
JOIN 
    lieux ON lieux.Num_Acc = caracteristiques.Accident_Id
JOIN 
    conditions_atmospheriques ON id_conditions_atmospheriques = atm
JOIN 
    categorie_de_route ON id_categorie_de_route = catr
JOIN 
    lumiere ON id_lumiere = lum
JOIN
    infrastructure ON id_infrastructure = infra
GROUP BY 
    conditions_atmospheriques, categorie_de_route, lumiere, infrastructure
ORDER BY 
    accident_count DESC;

-- Query 8: Analyze the severity of accidents by looking at the number of fatalities, injuries, and the types of vehicles involved.
SELECT gravite, COUNT(*) as severity_count FROM gravite JOIN usagers ON grav = id_gravite GROUP BY grav;

-- Query 9: Explore the involvement of different vehicle categories (catv) in accidents and analyze their contribution to overall road safety.
SELECT 
    categorie_du_vehicule,
    COUNT(*) as accident_count
FROM 
    vehicules
JOIN 
    categorie_du_vehicule ON categorie_du_vehicule.id_categorie_du_vehicule = catv
GROUP BY 
    categorie_du_vehicule;

-- Query 10: Examine the types of collisions (col) that occur most frequently. Determine if certain collision types are associated with higher injury rates.
SELECT 
    collision.collision AS 'Collision Type',
    COUNT(*) as 'Total Accident'
FROM
    caracteristiques
JOIN
    collision ON collision.id_collision = col
GROUP BY
    collision;
    

-- Query 11: Analyze the age and gender (sexe) distribution of individuals involved in accidents and determine if there are age or gender-specific patterns. Safety Equipment Usage:
-- This query needs to check the average sum of equipements used by each individual by each sex.
SELECT 
    sexe.sexe,
    AVG(usagers.secu1 + usagers.secu2 + usagers.secu3) AS 'Average Safety Equipment Used'
FROM
    usagers
JOIN
    sexe ON sexe.id_sexe = usagers.sexe
GROUP BY
    sexe.sexe;

 -- Query 12: Analyze the age and gender (sexe) distribution of individuals involved in accidents and determine if there are age or gender-specific patterns. Safety Equipment Usage:
SELECT 
    sexe.sexe as Gender,
    AVG(usagers.secu1 + usagers.secu2 + usagers.secu3) AS 'Average Equipment Use Score'
FROM
    usagers
JOIN
    sexe ON sexe.id_sexe = usagers.sexe
WHERE 
    usagers.secu1 NOT IN ('-1', '0', '8', '9') AND usagers.secu2 NOT IN ('-1', '0', '8', '9') AND  usagers.secu3 NOT IN ('-1', '0', '8', '9') 
GROUP BY 
    sexe.sexe;

 -- Query 13: Explore the usage of safety equipment (secu1, secu2, secu3) and its correlation with injury severity. Driver Analysis:
SELECT
    secu1.secu1 AS SafetyEquipment1,
    secu2.secu2 AS SafetyEquipment2,
    secu3.secu3 AS SafetyEquipment3,
    gravite.gravite AS InjurySeverity,
    COUNT(*) AS TotalAccidents
FROM
    Usagers u
JOIN 
    secu1 ON  id_secu1 = u.secu1
JOIN 
    secu2 ON  id_secu2 = u.secu2
JOIN 
    secu3 ON  id_secu3 = u.secu3
JOIN 
    gravite ON gravite.id_gravite = u.grav
WHERE
    u.catu = 1 -- Filtering for driver
GROUP BY
    u.secu1, u.secu2, u.secu3, u.grav 
ORDER BY
    TotalAccidents DESC;

 -- Query 14: Focus on pedestrian-related data (catu=3) to understand the locations (locp) and actions (actp) leading to pedestrian accidents. Vehicle Manoeuvres:
SELECT
    locp.locp AS PedestrianLocation,
    action_du_pieton AS PedestrianAction,
    COUNT(*) AS TotalPedestrianAccidents
FROM
    Usagers u
JOIN 
    locp ON  id_locp = u.locp
JOIN 
    action_du_pieton ON  id_action_du_pieton = actp
WHERE
    u.catu = 3 -- Filtering for pedestrians
GROUP BY
    u.locp, u.actp
ORDER BY
    TotalPedestrianAccidents DESC;

 -- Query 15: Investigate the types of manoeuvres performed by vehicles before accidents and their impact on collision outcomes.
SELECT
    m.manoeuvre_principale_avant_accident_ AS ManeuverType,
    COUNT(*) AS TotalAccidents,
    SUM(CASE WHEN u.grav = 2 THEN 1 ELSE 0 END) AS FatalAccidents,
    SUM(CASE WHEN u.grav = 3 THEN 1 ELSE 0 END) AS HospitalizedAccidents,
    SUM(CASE WHEN u.grav = 4 THEN 1 ELSE 0 END) AS LightInjuryAccidents
FROM
    Vehicules v
JOIN
    Usagers u ON v.Num_Acc = u.Num_Acc AND v.num_veh = u.num_veh
JOIN 
    manoeuvre_principale_avant_accident_ m ON id_manoeuvre_principale_avant_accident_ = manv 
GROUP BY
    v.manv
ORDER BY
    TotalAccidents DESC;
