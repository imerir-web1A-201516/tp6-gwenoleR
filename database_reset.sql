DROP TABLE IF EXISTS prets;
CREATE TABLE prets (id SERIAL PRIMARY KEY ,
                    qui varchar,
                    quoi varchar,
                    statut varchar);
INSERT INTO prets (qui, quoi, statut) VALUES ('fvargas','NXT', 'prete');

DROP TABLE IF EXISTS users;
CREATE TABLE users (id SERIAL PRIMARY KEY,
                    nom varchar,
                    prenom varchar);
INSERT INTO users (nom, prenom) VALUES ('Vargas','Fred');
INSERT INTO users (nom, prenom) VALUES ('Roton','Gwenole');