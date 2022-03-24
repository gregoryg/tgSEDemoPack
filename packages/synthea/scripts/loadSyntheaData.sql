## creates schema for Synthea (Healthcare dataset) and loads sample data
##
## NOTE: script will DROP existing tables before creating new ones
##
## NOTE2: loading data from local csv is turned OFF by defult on mysql on mac
##
##   server side
##      SHOW GLOBAL VARIABLES LIKE 'local_infile';
##      SET GLOBAL local_infile=1;
##   client side
##      mysql --local-infile=1
##

USE synthea;

## Load from csv
LOAD DATA LOCAL INFILE './synthea/data/allergies.csv' INTO TABLE allergies FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/careplans.csv' INTO TABLE careplans FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/conditions.csv' INTO TABLE conditions FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/demographics.csv' INTO TABLE demographics FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/devices.csv' INTO TABLE devices FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/encounters.csv' INTO TABLE encounters FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/patients.csv' INTO TABLE patients FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();
LOAD DATA LOCAL INFILE './synthea/data/payers.csv' INTO TABLE payers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS ();





