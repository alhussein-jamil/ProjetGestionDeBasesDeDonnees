use accidentsroutiers;
SET AUTOCOMMIT=0;
SET FOREIGN_KEY_CHECKS=0;

START TRANSACTION;  

-- Table: caracteristiques
ALTER TABLE caracteristiques
ADD CONSTRAINT pk_caracteristiques PRIMARY KEY (Accident_Id);

-- Table: usagers
ALTER TABLE usagers
ADD CONSTRAINT pk_usagers PRIMARY KEY (id_usager);

-- Table: vehicules
ALTER TABLE vehicules
ADD CONSTRAINT pk_vehicules PRIMARY KEY (id_vehicule);

-- Table: lieux
ALTER TABLE lieux
ADD CONSTRAINT pk_lieux PRIMARY KEY (Num_Acc);

-- Table: vosp
ALTER TABLE vosp
ADD CONSTRAINT pk_vosp PRIMARY KEY (id);

-- Table: action_du_pieton
ALTER TABLE action_du_pieton
ADD CONSTRAINT pk_action_du_pieton PRIMARY KEY (id);

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

-- Table: etatp
ALTER TABLE etatp
ADD CONSTRAINT pk_etatp PRIMARY KEY (id);


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

-- ---------------------------------------------------------------------------
-- caracteristiques : Add foreign key constraint 

ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_localisation
FOREIGN KEY (agg)
REFERENCES localisation(id_localisation)
ON DELETE CASCADE;


ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_intersection
FOREIGN KEY (`int`)
REFERENCES intersection(id_intersection)
ON DELETE CASCADE;

ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_lumiere
FOREIGN KEY (lum)
REFERENCES lumiere(id_lumiere)
ON DELETE CASCADE;

ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_conditions_atmospheriques
FOREIGN KEY (atm)
REFERENCES conditions_atmospheriques(id_conditions_atmospheriques)
ON DELETE CASCADE;

ALTER TABLE caracteristiques
ADD CONSTRAINT fk_caracteristiques_collision
FOREIGN KEY (col)
REFERENCES collision(id_collision)
ON DELETE CASCADE;

-- ---------------------------------------------------------------------------
-- usagers : Add foreign key constraint 

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_sexe
FOREIGN KEY (sexe)
REFERENCES sexe (id_sexe)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_vehicules
FOREIGN KEY (id_vehicule)
REFERENCES type_motorisation (id_type_motorisation )
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu1
FOREIGN KEY (secu1)
REFERENCES secu1 (id_secu1)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu2
FOREIGN KEY (secu2)
REFERENCES secu2 (id_secu2)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_secu3
FOREIGN KEY (secu3)
REFERENCES secu3 (id_secu3)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_gravite
FOREIGN KEY (grav)
REFERENCES gravite(id_gravite)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_locp
FOREIGN KEY (locp)
REFERENCES locp(id_locp)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_action_du_pieton
FOREIGN KEY (actp)
REFERENCES action_du_pieton(id_action_du_pieton)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_etatp
FOREIGN KEY (etatp)
REFERENCES etatp(id_etatp)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_motif_deplacement
FOREIGN KEY (trajet)
REFERENCES motif_deplacement(id_motif_deplacement)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_catu
FOREIGN KEY (catu)
REFERENCES categorie_usager(id_categorie_usager)
ON DELETE CASCADE;

ALTER TABLE usagers
ADD CONSTRAINT fk_usagers_caracteristiques
FOREIGN KEY (Num_Acc)
REFERENCES etatp(Accident_Id)
ON DELETE CASCADE;
-- ---------------------------------------------------------------------------
-- vehicules : Add foreign key constraint 

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_type_motorisation
FOREIGN KEY (motor)
REFERENCES type_motorisation (id_type_motorisation )
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_sens_de_circulation
FOREIGN KEY (senc)
REFERENCES sens_de_circulation(id_sens_de_circulation)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_point_de_choc_initial
FOREIGN KEY (choc)
REFERENCES point_choc_initial_(id_point_choc_initial_)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_fixe_heurte
FOREIGN KEY (obs)
REFERENCES obstacle_fixe_heurte (id_obstacle_fixe_heurte)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_mobile_heurte
FOREIGN KEY (obsm)
REFERENCES obstacle_mobile_heurte(id_obstacle_mobile_heurte)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_categorie_du_vehicule
FOREIGN KEY (catv)
REFERENCES categorie_du_vehicule (id_categorie_du_vehicule)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_obstacle_fixe_manoeuvre
FOREIGN KEY (manv)
REFERENCES manoeuvre_principale_avant_accident_(id_manoeuvre_principale_avant_accident_)
ON DELETE CASCADE;

ALTER TABLE vehicules
ADD CONSTRAINT fk_vehicules_lieux
FOREIGN KEY (Num_Acc)
REFERENCES lieux(Num_Acc);

-- ---------------------------------------------------------------------------
-- vehicules : Add foreign key constraint 

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_categorie_de_route
FOREIGN KEY (catr)
REFERENCES categorie_de_route(id_categorie_de_route)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_regime_de_circulation
FOREIGN KEY (circ)
REFERENCES regime_de_circulation(id_regime_de_circulation)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_vosp
FOREIGN KEY (vosp)
REFERENCES vosp(id_vosp)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_prof 
FOREIGN KEY (prof)
REFERENCES prof(id_prof)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_trace_en_plan
FOREIGN KEY (plan)
REFERENCES trace_en_plan(id_trace_en_plan)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_etat_de_la_surface
FOREIGN KEY (surf)
REFERENCES etat_de_la_surface_(id_etat_de_la_surface_)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_infrastructure
FOREIGN KEY (infra)
REFERENCES infrastructure(id_infrastructure)
ON DELETE CASCADE;

ALTER TABLE lieux
ADD CONSTRAINT fk_lieux_situation_accident
FOREIGN KEY (situ)
REFERENCES situation_accident(id_id_situation_accident)
ON DELETE CASCADE;

commit;
ROLLBACK ;

set autocommit=1;
