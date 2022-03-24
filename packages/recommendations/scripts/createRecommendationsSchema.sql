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

CREATE DATABASE IF NOT EXISTS recommendations;
USE recommendations;

DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
     userId          INT,
     movieId          INT,
     rating          DECIMAL(3,1),
     tmstamp          DOUBLE
);

DROP TABLE IF EXISTS nameBasics;
CREATE TABLE nameBasics (
     nconst          VARCHAR(20),
     primaryName     VARCHAR(60),
     birthYear          INT,
     deathYear          INT,
     primaryProfession          VARCHAR(50),
     knownForTitles           VARCHAR(300)
);

DROP TABLE IF EXISTS titles;
CREATE TABLE titles (
     tconst                 INT,
     titleType              VARCHAR(40),
     primaryTitle           VARCHAR(100),
     originalTitle          VARCHAR(100),
     isAdult                INT,
     startYear                INT,
     endYear                INT,
     runtimeMinutes                INT,
     genres                 VARCHAR(300)
);

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
     movieId          INT,
     title           VARCHAR(70),
     genres          VARCHAR(200)
);

DROP TABLE IF EXISTS friendships;
CREATE  TABLE friendships (
     person             INT,
     friend             INT,
     dateMet          DATE
);

DROP TABLE IF EXISTS people;
CREATE  TABLE people (
     nameId     VARCHAR(20),
     firstName     VARCHAR(40),
     lastName     VARCHAR(40),
     gender     VARCHAR(25),
     age          INT,
     language           VARCHAR(100)
);

DROP TABLE IF EXISTS links;
CREATE  TABLE links (
     movieId             INT,
     imdbId             INT,
     tmdbId          INT
);

DROP TABLE IF EXISTS tags;
CREATE  TABLE tags (
     userId             INT,
     movieId            INT,
     tag                VARCHAR(100),
     tmstamp            DATE
);

DROP TABLE IF EXISTS genres;
CREATE  TABLE genres (
     genresName             VARCHAR(50)
);
