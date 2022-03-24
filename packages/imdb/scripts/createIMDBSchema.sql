## creates schema for MOVIES (based on IMDB data) and loads sample data
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

CREATE DATABASE IF NOT EXISTS imdb;
USE imdb;

DROP TABLE IF EXISTS title_basics;
CREATE  TABLE title_basics (
     titleId     VARCHAR(20),
     titleType     VARCHAR(20),
     primaryTitle     VARCHAR(25),
     originalTitle    VARCHAR(25),
     isAdult          INT,
     startYear        INT,
     endYear          INT,
     runtimeMinutes   INT,
     genres           VARCHAR(100)
);

DROP TABLE IF EXISTS name_basics;
CREATE  TABLE name_basics (
     nameId             VARCHAR(20),
     primaryName        VARCHAR(20),
     birthYear          INT,
     deathYear          INT,
     primaryProfession  VARCHAR(20),
     knownForTitles     VARCHAR(20)
);

DROP TABLE IF EXISTS title_ratings;
CREATE  TABLE title_ratings (
     titleId            VARCHAR(20),
     averageRating      FLOAT(3,1),
     numVotes           INT
);


DROP TABLE IF EXISTS title_principals;
CREATE  TABLE title_principals (
     principalId        VARCHAR(20),
     ordering           INT,
     nameId             VARCHAR(20),
     category           VARCHAR(20),
     job                VARCHAR(20),
     characters         VARCHAR(100)
);





