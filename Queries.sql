USE accidentsroutiers;

-- INSERT INTO accidentsroutiers.categorie_du_vehicule
-- VALUES
-- ('-1', 'unconnue');

-- Query_3D 1: Retrieve information about accidents involving pedestrians, including their characteristics and the type of vehicle involved
-- title='Accident Severity by Month and Vehicle Category'
SELECT 
    usagers.id_usager AS 'User ID',
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

-- Query_2D 2: Find the most common atmospheric condition during accidents.
-- title='Most Common Atmospheric Conditions'
SELECT 
    conditions_atmospheriques.conditions_atmospheriques AS "Conditions Atmospheriques"
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

-- Query_2D 3: Find the average number of accidents for each category of the road.
-- title='Average Number of Accidents for Each Road Category'
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

-- Query_2D 4: List the different types of motorizations (type_motorisation) and the count of accidents for each type.
-- title='Accidents by Motorization Type'
SELECT 
    type_motorisation.type_motorisation AS 'Type of Motorization',
    COUNT(*) AS 'Accident Count'
FROM 
    type_motorisation
JOIN 
    vehicules ON type_motorisation.id_type_motorisation = vehicules.motor
GROUP BY 
    type_motorisation.type_motorisation;

-- Query_3D 5: Retrieve the distribution of accidents across different categories such as time of day (lum), weather conditions (atm), and road types (catr).
-- title='Severity of Accidents across lighting conditions, weather conditions and road types'
SELECT 
conditions_atmospheriques.conditions_atmospheriques AS 'Weather Conditions',
    categorie_de_route.categorie_de_route AS 'Road Type',
    lumiere.lumiere AS 'Lighting Conditions',
    infrastructure.infrastructure AS 'Infrastructure',
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

-- Query_2D 6: Analyze the severity of accidents by looking at the number of fatalities, injuries, and the types of vehicles involved.
-- title='Accidents by the number of fatalities, injuries and vehicle Category '
SELECT gravite AS severity
, COUNT(*) aS severity_count
 as severity_count FROM gravite JOIN usagers ON grav = id_gravite GROUP BY grav;

-- Query_2D 7: Explore the involvement of different vehicle categories (catv) in accidents and analyze their contribution to overall road safety.
-- title='Accidents by Vehicle Category'
SELECT 
    categorie_du_vehicule AS 'Vehicle Category',
    COUNT(*) as 'Total Accident'
FROM 
    vehicules
JOIN 
    categorie_du_vehicule ON categorie_du_vehicule.id_categorie_du_vehicule = catv
GROUP BY 
    categorie_du_vehicule;

-- Query_2D 8: Examine the types of collisions (col) that occur most frequently. Determine if certain collision types are associated with higher injury rates.
-- title='Most Frequent Collision Types'
SELECT 
    collision.collision AS 'Collision Type',
    COUNT(*) as 'Total Accident'
FROM
    caracteristiques
JOIN
    collision ON collision.id_collision = col
GROUP BY
    collision;

-- Query_2D 9: Analyze the age and gender (sexe) distribution of individuals involved in accidents and determine if there are age or gender-specific patterns. Safety Equipment Usage:
-- title='Average Equipment Use Score by Gender'
SELECT 
    sexe.sexe as 'Gender'
    AVG(usagers.secu1 + usagers.secu2 + usagers.secu3) AS 'Average Equipment Use Score'
FROM
    usagers
JOIN
    sexe ON sexe.id_sexe = usagers.sexe
WHERE 
    usagers.secu1 NOT IN ('-1', '0', '8', '9') AND usagers.secu2 NOT IN ('-1', '0', '8', '9') AND  usagers.secu3 NOT IN ('-1', '0', '8', '9') 
GROUP BY 
    sexe.sexe;

-- Query_3D 10: Explore the usage of safety equipment (secu1, secu2, secu3) and its correlation with injury severity. Driver Analysis:
-- title='Safety Equipment Usage and Injury Severity'
SELECT
    secu1.secu1 AS "Safety Equipment 1",
    secu2.secu2 AS "Safety Equipment 2",
    secu3.secu3 AS "Safety Equipment 3",
    gravite.gravite AS "Severity",
    COUNT(*) AS "Total Accidents"
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
    u.catu = 1
GROUP BY
    u.secu1, u.secu2, u.secu3, u.grav;

-- Query_3D 11: Focus on pedestrian-related data (catu=3) to understand the locations (locp) and actions (actp) leading to pedestrian accidents. Vehicle Manoeuvres:
-- title='Pedestrian Accidents'
SELECT
    locp.locp AS "Location of Pedestrian"
    action_du_pieton AS "Action of Pedestrian"
    COUNT(*) AS "Total Accidents"
FROM
    Usagers u
JOIN 
    locp ON  id_locp = u.locp
JOIN 
    action_du_pieton ON  id_action_du_pieton = actp
WHERE
    u.catu = 3 -- Filtering for pedestrians
GROUP BY
    u.locp, u.actp;

-- Query_3D 12: Investigate the types of manoeuvres performed by vehicles before accidents and their impact on collision outcomes.
-- title='Manoeuvre Types and Accident Outcomes'
SELECT
    m.manoeuvre_principale_avant_accident_ AS "Manoeuvre",
    COUNT(*) AS "Total Accidents"n
    SUM(CASE WHEN u.grav = 2 THEN 1 ELSE 0 END) AS "Serious Injury Accidents"
    SUM(CASE WHEN u.grav = 3 THEN 1 ELSE 0 END) AS "Death Accidents"
    SUM(CASE WHEN u.grav = 4 THEN 1 ELSE 0 END) AS "Unscathed Accidents"
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
