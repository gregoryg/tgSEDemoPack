## load schema for MOVIES (based on IMDB data) and loads sample data
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

USE imdb;

## Load from csv
LOAD DATA LOCAL INFILE './imdb/data/title.basics.tsv' INTO TABLE title_basics FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (titleId,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres);
LOAD DATA LOCAL INFILE './imdb/data/name.basics.tsv' INTO TABLE name_basics FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (nameId,primaryName,birthYear,deathYear,primaryProfession,knownForTitles);
LOAD DATA LOCAL INFILE './imdb/data/title.ratings.tsv' INTO TABLE title_ratings FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (titleId,averageRating,numVotes);
LOAD DATA LOCAL INFILE './imdb/data/title.principals.tsv' INTO TABLE title_principals FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (principalId,ordering,nameId,category,job,characters);





