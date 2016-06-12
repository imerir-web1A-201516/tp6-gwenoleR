DROP TABLE IF EXISTS prets;
CREATE TABLE prets (id SERIAL PRIMARY KEY ,
                    qui varchar,
                    quoi varchar,
                    statut varchar);
INSERT INTO prets (qui, quoi, statut) VALUES ('fvargas','NXT', 'prete');