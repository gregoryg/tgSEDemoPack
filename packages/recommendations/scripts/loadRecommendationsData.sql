## creates schema for FRIENDS (based on IMDB data) and loads sample data
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

SET @@GLOBAL.local_infile = 1;

USE recommendations;

## Load from csv
LOAD DATA LOCAL INFILE '../data/ratings.sample.csv' INTO TABLE ratings FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (userId,movieId,rating,tmstamp);
LOAD DATA LOCAL INFILE '../data/name.basics.sample.tsv' INTO TABLE nameBasics FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (nconst,primaryName,birthYear,deathYear,primaryProfession,knownForTitles);
LOAD DATA LOCAL INFILE '../data/title.basics.sample.tsv' INTO TABLE titles FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS (tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres);
LOAD DATA LOCAL INFILE '../data/movie.csv' INTO TABLE movies FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (movieId,title,genres);
LOAD DATA LOCAL INFILE '../data/friendships.csv' INTO TABLE friendships FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (person,friend,dateMet);
LOAD DATA LOCAL INFILE '../data/people.csv' INTO TABLE people FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (nameId,firstName,lastName,gender,age,language);
LOAD DATA LOCAL INFILE '../data/link.csv' INTO TABLE links FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (movieId,imdbId,tmdbId);
LOAD DATA LOCAL INFILE '../data/tag.sample.csv' INTO TABLE tags FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (userId,movieId,tag,tmstamp);
LOAD DATA LOCAL INFILE '../data/genres.txt' INTO TABLE genres FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (genresName);


