use accidentsroutiers;
SET AUTOCOMMIT=0;
SET FOREIGN_KEY_CHECKS=0;

START TRANSACTION;  

-- Table: action_du_pieton
ALTER TABLE action_du_pieton
ADD CONSTRAINT pk_action_du_pieton PRIMARY KEY (id);

-- Table: caracteristiques
ALTER TABLE caracteristiques
ADD CONSTRAINT pk_caracteristiques PRIMARY KEY (Accident_Id);

-- Table: vosp
ALTER TABLE vosp
ADD CONSTRAINT pk_vosp PRIMARY KEY (id);

-- Table: vehicules
ALTER TABLE vehicules
ADD CONSTRAINT pk_vehicules PRIMARY KEY (id_vehicule);

-- Table: categorie_de_route
ALTER TABLE categorie_de_route
ADD CONSTRAINT pk_categorie_de_route PRIMARY KEY (id);

-- Table: categorie_du_vehicule
ALTER TABLE categorie_du_vehicule
ADD CONSTRAINT pk_categorie_du_vehicule PRIMARY KEY (id);

-- Table: categorie_usager
ALTER TABLE categorie_usager
ADD CONSTRAINT pk_categorie_usager PRIMARY KEY (id);

-- Table: collision
ALTER TABLE collision
ADD CONSTRAINT pk_collision PRIMARY KEY (id);

-- Table: conditions_atmospheriques
ALTER TABLE conditions_atmospheriques
ADD CONSTRAINT pk_conditions_atmospheriques PRIMARY KEY (id);

-- Table: etat_de_la_surface_
ALTER TABLE etat_de_la_surface_
ADD CONSTRAINT pk_etat_de_la_surface_ PRIMARY KEY (id);

-- Table: extratables
ALTER TABLE extratables
ADD CONSTRAINT pk_extratables PRIMARY KEY (id);

-- Table: gravite
ALTER TABLE gravite
ADD CONSTRAINT pk_gravite PRIMARY KEY (id);

-- Table: infrastructure
ALTER TABLE infrastructure
ADD CONSTRAINT pk_infrastructure PRIMARY KEY (id);

-- Table: intersection
ALTER TABLE intersection
ADD CONSTRAINT pk_intersection PRIMARY KEY (id);

-- Table: lieux
ALTER TABLE lieux
ADD CONSTRAINT pk_lieux PRIMARY KEY (Num_Acc);

-- Table: localisation
ALTER TABLE localisation
ADD CONSTRAINT pk_localisation PRIMARY KEY (id);

-- Table: locp
ALTER TABLE locp
ADD CONSTRAINT pk_locp PRIMARY KEY (id);

-- Table: lumiere
ALTER TABLE lumiere
ADD CONSTRAINT pk_lumiere PRIMARY KEY (id);

-- Table: manoeuvre_principale_avant_accident_
ALTER TABLE manoeuvre_principale_avant_accident_
ADD CONSTRAINT pk_manoeuvre_principale_avant_accident PRIMARY KEY (id);

-- Table: motif_deplacement
ALTER TABLE motif_deplacement
ADD CONSTRAINT pk_motif_deplacement PRIMARY KEY (id);

-- Table: obstacle_fixe_heurte
ALTER TABLE obstacle_fixe_heurte
ADD CONSTRAINT pk_obstacle_fixe_heurte PRIMARY KEY (id);

-- Table: obstacle_mobile_heurte
ALTER TABLE obstacle_mobile_heurte
ADD CONSTRAINT pk_obstacle_mobile_heurte PRIMARY KEY (id);

-- Table: point_choc_initial_
ALTER TABLE point_choc_initial_
ADD CONSTRAINT pk_point_choc_initial_ PRIMARY KEY (id);

-- Table: prof
ALTER TABLE prof
ADD CONSTRAINT pk_prof PRIMARY KEY (id);

-- Table: regime_de_circulation
ALTER TABLE regime_de_circulation
ADD CONSTRAINT pk_regime_de_circulation PRIMARY KEY (id);

-- Table: secu1
ALTER TABLE secu1
ADD CONSTRAINT pk_secu1 PRIMARY KEY (id);

-- Table: secu2
ALTER TABLE secu2
ADD CONSTRAINT pk_secu2 PRIMARY KEY (id);

-- Table: secu3
ALTER TABLE secu3
ADD CONSTRAINT pk_secu3 PRIMARY KEY (id);

-- Table: sens_de_circulation
ALTER TABLE sens_de_circulation
ADD CONSTRAINT pk_sens_de_circulation PRIMARY KEY (id);

-- Table: sexe
ALTER TABLE sexe
ADD CONSTRAINT pk_sexe PRIMARY KEY (id);

-- Table: situation_accident
ALTER TABLE situation_accident
ADD CONSTRAINT pk_situation_accident PRIMARY KEY (id);

-- Table: trace_en_plan
ALTER TABLE trace_en_plan
ADD CONSTRAINT pk_trace_en_plan PRIMARY KEY (id);

-- Table: type_motorisation
ALTER TABLE type_motorisation
ADD CONSTRAINT pk_type_motorisation PRIMARY KEY (id);

-- Table: usagers
ALTER TABLE usagers
ADD CONSTRAINT pk_usagers PRIMARY KEY (id_usager);


ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_localisation
FOREIGN KEY (agg)
REFERENCES localisation(id)
ON DELETE CASCADE;

-- Add foreign key constraint to reference action_du_pieton
ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_intersection
FOREIGN KEY (`int`)
REFERENCES intersection(id)
ON DELETE CASCADE;

ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_lumiere
FOREIGN KEY (lum)
REFERENCES lumiere(id)
ON DELETE CASCADE;


ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_conditions_atmospheriques
FOREIGN KEY (atm)
REFERENCES conditions_atmospheriques(id)
ON DELETE CASCADE;



ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_collision
FOREIGN KEY (col)
REFERENCES collision(id)
ON DELETE CASCADE;



-- Add foreign key constraints to reference other tables
ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_sexe
FOREIGN KEY (sexe)
REFERENCES sexe (id)
ON DELETE CASCADE;

-- Table: vehicules
ALTER TABLE vehicules
ADD CONSTRAINT pk_vehicules PRIMARY KEY (id_vehicule);

-- Add foreign key constraints to reference other tables
ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_type_motorisation
FOREIGN KEY (motor)
REFERENCES type_motorisation (id)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_vehicules
FOREIGN KEY (id_vehicule)
REFERENCES type_motorisation (id)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu1
FOREIGN KEY (secu1)
REFERENCES secu1 (id)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu2
FOREIGN KEY (secu2)
REFERENCES secu2 (id)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu3
FOREIGN KEY (secu3)
REFERENCES secu3 (id)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_sens_de_circulation
FOREIGN KEY (senc)
REFERENCES sens_de_circulation(id)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_point_de_choc_initial
FOREIGN KEY (choc)
REFERENCES point_choc_initial_(id)
ON DELETE CASCADE;


ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_fixe_heurte
FOREIGN KEY (obs)
REFERENCES obstacle_fixe_heurte (id)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_mobile_heurte
FOREIGN KEY (obsm)
REFERENCES obstacle_mobile_heurte(id)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_categorie_du_vehicule
FOREIGN KEY (catv)
REFERENCES categorie_du_vehicule (id)
ON DELETE CASCADE;




ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_fixe_heurte
FOREIGN KEY (obs)
REFERENCES obstacle_fixe_heurte (id)
ON DELETE CASCADE;



commit;
ROLLBACK ;

set autocommit=1;
