## creates schema for LDBC (Linked Data Benchmark) and loads sample data
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

USE ldbc;

## Load from csv
LOAD DATA LOCAL INFILE './ldbc/data/comments_0_0.csv' INTO TABLE comment FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,creationDate,locationIP,browserUsed,content,length);
LOAD DATA LOCAL INFILE './ldbc/data/forum_0_0.csv' INTO TABLE forum FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,title,creationDate);
LOAD DATA LOCAL INFILE './ldbc/data/organisation_0_0.csv' INTO TABLE organization FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,type,name,url);
LOAD DATA LOCAL INFILE './ldbc/data/person_0_0.csv' INTO TABLE person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,firstName,lastName,gender,birthday,creationDate,locationIP,browserUsed);
LOAD DATA LOCAL INFILE './ldbc/data/place_0_0.csv' INTO TABLE place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url,type);
LOAD DATA LOCAL INFILE './ldbc/data/post_0_0.csv' INTO TABLE post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,imageFile,creationDate,locationIP,browserUsed,language,content,length);
LOAD DATA LOCAL INFILE './ldbc/data/tag_0_0.csv' INTO TABLE tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);
LOAD DATA LOCAL INFILE './ldbc/data/tagclass_0_0.csv' INTO TABLE tagClass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);


