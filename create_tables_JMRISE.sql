#------------------------------------------------------------
# Table: _caracteristiques
#------------------------------------------------------------

CREATE TABLE _caracteristiques(
        Accident_id BigInt NOT NULL ,
        jour        BigInt NOT NULL ,
        mois        BigInt NOT NULL ,
        an          BigInt NOT NULL ,
        hrmn        Time NOT NULL ,
        lum         Int NOT NULL ,
        dep         Char (5) NOT NULL ,
        com         Char (5) NOT NULL ,
        agg         Int NOT NULL ,
        int_        Int NOT NULL ,
        atm         Int NOT NULL ,
        col         Int NOT NULL ,
        adr         Char (5) NOT NULL ,
        lat         Decimal NOT NULL ,
        long_       Decimal NOT NULL
	,CONSTRAINT _caracteristiques_PK PRIMARY KEY (Accident_id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _lieux
#------------------------------------------------------------

CREATE TABLE _lieux(
        Num_Acc BigInt NOT NULL ,
        catr    Int NOT NULL ,
        voie    Char (5) NOT NULL ,
        v1      Char (5) NOT NULL ,
        v2      Char (5) NOT NULL ,
        circ    Double NOT NULL ,
        nbv     Int NOT NULL ,
        vosp    Int NOT NULL ,
        prof    Int NOT NULL ,
        pr      Char (5) NOT NULL ,
        pr1     Char (5) NOT NULL ,
        plan    Int NOT NULL ,
        lartcp  Char (5) NOT NULL ,
        larrout Double NOT NULL ,
        surf    Int NOT NULL ,
        infra   Int NOT NULL ,
        situ    Int NOT NULL ,
        vma     Int NOT NULL
	,CONSTRAINT _lieux_PK PRIMARY KEY (Num_Acc)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _usagers
#------------------------------------------------------------

CREATE TABLE _usagers(
        id_usager   Char (255) NOT NULL ,
        Num_Acc     BigInt NOT NULL ,
        id_vehicule Char (255) NOT NULL ,
        num_veh     Char (255) NOT NULL ,
        place       Int NOT NULL ,
        catu        Int NOT NULL ,
        grav        Int NOT NULL ,
        n_nis       Year NOT NULL ,
        trajet      Double NOT NULL ,
        secu1       Double NOT NULL ,
        secu2       Double NOT NULL ,
        secu3       Double NOT NULL ,
        locp        Double NOT NULL ,
        actp        Double NOT NULL ,
        etatp       Double NOT NULL
	,CONSTRAINT _usagers_PK PRIMARY KEY (id_usager)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _vehicules
#------------------------------------------------------------

CREATE TABLE _vehicules(
        id_vehicule Char (255) NOT NULL ,
        Num_Acc     BigInt NOT NULL ,
        num_veh     Char (255) NOT NULL ,
        senc        Int NOT NULL ,
        catv        Int NOT NULL ,
        obs         BigInt NOT NULL ,
        obsm        Int NOT NULL ,
        choc        Int NOT NULL ,
        manv        Int NOT NULL ,
        motor       Int NOT NULL ,
        occutc      Char (5) NOT NULL
	,CONSTRAINT _vehicules_PK PRIMARY KEY (id_vehicule)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _secu1
#------------------------------------------------------------

CREATE TABLE _secu1(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _secu1_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _motif_deplacement
#------------------------------------------------------------

CREATE TABLE _motif_deplacement(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _motif_deplacement_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _obstacle_fixe_heurte
#------------------------------------------------------------

CREATE TABLE _obstacle_fixe_heurte(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _obstacle_fixe_heurte_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _obstacle_mobile_heurte
#------------------------------------------------------------

CREATE TABLE _obstacle_mobile_heurte(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _obstacle_mobile_heurte_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _prof
#------------------------------------------------------------

CREATE TABLE _prof(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _prof_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _regime_de_circulation
#------------------------------------------------------------

CREATE TABLE _regime_de_circulation(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _regime_de_circulation_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _situation_accident
#------------------------------------------------------------

CREATE TABLE _situation_accident(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _situation_accident_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _trace_en_plan
#------------------------------------------------------------

CREATE TABLE _trace_en_plan(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _trace_en_plan_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _type_motorisation
#------------------------------------------------------------

CREATE TABLE _type_motorisation(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _type_motorisation_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _vosp
#------------------------------------------------------------

CREATE TABLE _vosp(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _vosp_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _sexe
#------------------------------------------------------------

CREATE TABLE _sexe(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _sexe_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _secu3
#------------------------------------------------------------

CREATE TABLE _secu3(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _secu3_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _secu2
#------------------------------------------------------------

CREATE TABLE _secu2(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _secu2_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _collision
#------------------------------------------------------------

CREATE TABLE _collision(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _collision_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _action_du_pieton
#------------------------------------------------------------

CREATE TABLE _action_du_pieton(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _action_du_pieton_PK PRIMARY KEY (id)
)ENGINE=InnoDB;

#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: _point_choc_initial
#------------------------------------------------------------

CREATE TABLE _point_choc_initial(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _point_choc_initial_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _sense_de_circulation
#------------------------------------------------------------

CREATE TABLE _sense_de_circulation(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _sense_de_circulation_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _manoeuvre_principale_avant_accident_
#------------------------------------------------------------

CREATE TABLE _manoeuvre_principale_avant_accident_(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _manoeuvre_principale_avant_accident__PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _categorie_usager
#------------------------------------------------------------

CREATE TABLE _categorie_usager(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _categorie_usager_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _conditions_atmospheriques
#------------------------------------------------------------

CREATE TABLE _conditions_atmospheriques(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _conditions_atmospheriques_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _etat_de_la_surface_
#------------------------------------------------------------

CREATE TABLE _etat_de_la_surface_(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _etat_de_la_surface__PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _gravite
#------------------------------------------------------------

CREATE TABLE _gravite(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _gravite_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _infrastructure
#------------------------------------------------------------

CREATE TABLE _infrastructure(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _infrastructure_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _intersection
#------------------------------------------------------------

CREATE TABLE _intersection(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _intersection_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _localisation
#------------------------------------------------------------

CREATE TABLE _localisation(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _localisation_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _locp
#------------------------------------------------------------

CREATE TABLE _locp(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _locp_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _lumiere
#------------------------------------------------------------

CREATE TABLE _lumiere(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _lumiere_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _categorie_de_vehicule
#------------------------------------------------------------

CREATE TABLE _categorie_de_vehicule(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _categorie_de_vehicule_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: _categorite_de_route
#------------------------------------------------------------

CREATE TABLE _categorite_de_route(
        id            Varchar (255) NOT NULL ,
        signification Varchar (255) NOT NULL
	,CONSTRAINT _categorite_de_route_PK PRIMARY KEY (id)
)ENGINE=InnoDB;

