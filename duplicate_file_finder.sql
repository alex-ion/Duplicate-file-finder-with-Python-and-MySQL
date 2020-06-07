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



CREATE TABLE duplicates(
id_verificare INT AUTO_INCREMENT,
nume_fisier1 VARCHAR(400),
nume_fisier2 VARCHAR(400),
rezultat VARCHAR(400),
PRIMARY KEY (id_verificare)
) ENGINE = INNODB;

CREATE TABLE run_times (
id INT AUTO_INCREMENT,
run_time DOUBLE(16,14),
PRIMARY KEY (id)
) ENGINE = INNODB;


TRUNCATE TABLE fisier;
TRUNCATE TABLE duplicates;
TRUNCATE TABLE run_times;

SELECT SUM(run_time) FROM run_times;
