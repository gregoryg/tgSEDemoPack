## creates schema for MOVIES (based on IMDB data) and loads sample data
##
## NOTE: script will DROP existing tables before creating new ones
##
## NOTE2: loading data from local csv is turned OFF by defult on mysql on mac
##
##   server Ide
##      SHOW GLOBAL VARIABLES LIKE 'local_infile';
##      SET GLOBAL local_infile=1;
##   client Ide
##      mysql --local-infile=1
##

DROP DATABASE IF EXISTS ldbc;
CREATE DATABASE ldbc;
USE ldbc;

## allow cascading deletes
SET foreign_key_checks = 0;

DROP TABLE IF EXISTS comment;
CREATE TABLE comment (
     id               INT NOT NULL,
     creationDate     DATE,
     locationIP     VARCHAR(25),
     browserUsed    VARCHAR(20),
     content        VARCHAR(250),
     length          INT,
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS forum;
CREATE  TABLE forum (
     id               INT NOT NULL,
     title     VARCHAR(25),
     creationDate    DATE,
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS organization;
CREATE  TABLE organization (
     id               INT NOT NULL,
     type     VARCHAR(25),
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS person;
CREATE  TABLE person (
     id               INT NOT NULL,
     firstName     VARCHAR(25),
     lastName     VARCHAR(25),
     gender     VARCHAR(25),
     birthday     VARCHAR(25),
     creationDate     VARCHAR(30),
     locationIP    VARCHAR(25),
     browserUsed        VARCHAR(25),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS place;
CREATE  TABLE place (
     id               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     type     VARCHAR(25),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS post;
CREATE  TABLE post (
     id               INT NOT NULL,
     imageFile     VARCHAR(40),
     creationDate     VARCHAR(25),
     locationIP     VARCHAR(25),
     browserUsed     VARCHAR(25),
     language    VARCHAR(25),
     content        VARCHAR(25),
     length        VARCHAR(25),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tag;
CREATE  TABLE tag (
     id               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tagClass;
CREATE  TABLE tagClass (
     id               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (id)
);

DROP TABLE IF EXISTS comment_hasCreator_person;
CREATE  TABLE comment_hasCreator_person (
     CommentId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     PRIMARY KEY (CommentId),
     FOREIGN KEY (PersonId) REFERENCES person(id)
);

DROP TABLE IF EXISTS comment_hasTag_tag;
CREATE  TABLE comment_hasTag_tag (
     CommentId     INT  NOT NULL,
     TagId     INT  NOT NULL,
     PRIMARY KEY (CommentId),
     FOREIGN KEY (TagId) REFERENCES tag(id)
);

DROP TABLE IF EXISTS forum_hasMember_person;
CREATE  TABLE forum_hasMember_person (
     ForumId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     joinDate     DATE,
     PRIMARY KEY (ForumId),
     FOREIGN KEY (PersonId) REFERENCES person(id)
);

DROP TABLE IF EXISTS person_hasInterest_tag;
CREATE  TABLE person_hasInterest_tag (
     PersonId     INT  NOT NULL,
     TagId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (TagId) REFERENCES tag(id)
);

DROP TABLE IF EXISTS person_isLocatedIn_place;
CREATE  TABLE person_isLocatedIn_place (
     PersonId     INT  NOT NULL,
     PlaceId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (PlaceId) REFERENCES place(id)
);

DROP TABLE IF EXISTS person_knows_person;
CREATE  TABLE person_knows_person (
     PersonId     INT  NOT NULL,
     FriendId     INT  NOT NULL,
     creationDate     DATE,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (FriendId) REFERENCES person(id)
);

DROP TABLE IF EXISTS person_likes_post;
CREATE  TABLE person_likes_post (
     PersonId     INT  NOT NULL,
     PostId     INT  NOT NULL,
     creationDate     DATE,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (PostId) REFERENCES post(id)
);

DROP TABLE IF EXISTS person_workAt_organisation;
CREATE  TABLE person_workAt_organisation (
     PersonId     INT  NOT NULL,
     OrganisationId     INT  NOT NULL,
     workFrom     INT,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (OrganisationId) REFERENCES organisation(id)
);

DROP TABLE IF EXISTS post_hasCreator_person;
CREATE  TABLE post_hasCreator_person (
     PostId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     PRIMARY KEY (PostId),
     FOREIGN KEY (PersonId) REFERENCES person(id)
);

DROP TABLE IF EXISTS tag_hasType_tagclass;
CREATE  TABLE tag_hasType_tagclass (
     TagId     INT  NOT NULL,
     TagClassId     INT  NOT NULL,
     PRIMARY KEY (TagId),
     FOREIGN KEY (TagClassId) REFERENCES tagClass(id)
);
