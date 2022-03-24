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
LOAD DATA LOCAL INFILE './ldbc/data/comment_sample.csv' INTO TABLE comment FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,creationDate,locationIP,browserUsed,content,length);
LOAD DATA LOCAL INFILE './ldbc/data/forum_0_0.csv' INTO TABLE forum FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,title,creationDate);
LOAD DATA LOCAL INFILE './ldbc/data/organisation_0_0.csv' INTO TABLE organization FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,type,name,url);
LOAD DATA LOCAL INFILE './ldbc/data/person_0_0.csv' INTO TABLE person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,firstName,lastName,gender,birthday,creationDate,locationIP,browserUsed);
LOAD DATA LOCAL INFILE './ldbc/data/place_0_0.csv' INTO TABLE place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url,type);
LOAD DATA LOCAL INFILE './ldbc/data/post_sample.csv' INTO TABLE post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,imageFile,creationDate,locationIP,browserUsed,language,content,length);
LOAD DATA LOCAL INFILE './ldbc/data/tag_0_0.csv' INTO TABLE tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);
LOAD DATA LOCAL INFILE './ldbc/data/tagclass_0_0.csv' INTO TABLE tagClass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);

LOAD DATA LOCAL INFILE './ldbc/data/tag_hasType_tagclass_0_0.csv' INTO TABLE tag_hasType_tagclass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (TagId,TagClassId);
LOAD DATA LOCAL INFILE './ldbc/data/post_hasCreator_person_sample.csv' INTO TABLE post_hasCreator_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PostId,PersonId);
LOAD DATA LOCAL INFILE './ldbc/data/person_workAt_organisation_0_0.csv' INTO TABLE person_workAt_organisation FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,OrganisationId);
LOAD DATA LOCAL INFILE './ldbc/data/person_likes_post_sample.csv' INTO TABLE person_likes_post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,PostId);
LOAD DATA LOCAL INFILE './ldbc/data/person_knows_person_sample.csv' INTO TABLE person_knows_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,FriendId);
LOAD DATA LOCAL INFILE './ldbc/data/person_isLocatedIn_place_0_0.csv' INTO TABLE person_isLocatedIn_place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,PlaceId);
LOAD DATA LOCAL INFILE './ldbc/data/person_hasInterest_tag_0_0.csv' INTO TABLE person_hasInterest_tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,TagId);
LOAD DATA LOCAL INFILE './ldbc/data/forum_hasMember_person_sample.csv' INTO TABLE forum_hasMember_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (ForumId,PersonId);
LOAD DATA LOCAL INFILE './ldbc/data/comment_hasTag_tag_sample.csv' INTO TABLE comment_hasTag_tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (CommentId,TagId);
LOAD DATA LOCAL INFILE './ldbc/data/comment_hasCreator_person_sample.csv' INTO TABLE comment_hasCreator_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (CommentId,PersonId);
