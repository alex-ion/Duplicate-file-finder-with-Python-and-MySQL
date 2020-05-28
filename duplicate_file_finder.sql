CREATE SCHEMA duplicate_file_finder;

CREATE TABLE fisier(
id_fisier INT AUTO_INCREMENT,
nume_fisier VARCHAR(400),
nume_fisier_trunchiat VARCHAR(400),
path VARCHAR(400),
size VARCHAR(400),
creation_date VARCHAR(30),
modify_date VARCHAR(30),
PRIMARY KEY (id_fisier)
) ENGINE=INNODB;



CREATE TABLE verificat(
id_verificare INT AUTO_INCREMENT,
id_fisier1 INT,
id_fisier2 INT,
nume_fisier1 VARCHAR(400),
nume_fisier2 VARCHAR(400),
rezultat VARCHAR(400),
descriere VARCHAR(400),
PRIMARY KEY (id_verificare)
) ENGINE = INNODB;



TRUNCATE TABLE fisier;

DELETE FROM fisier WHERE id_fisier > 100;