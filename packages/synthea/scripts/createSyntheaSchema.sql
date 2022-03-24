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

SET @datadir := '/Users/roberthardaway/tg/projects/tgSolutionPack/ldbc/data/';

CREATE DATABASE IF NOT EXISTS synthea;
USE synthea;

DROP TABLE IF EXISTS allergies;
CREATE  TABLE allergies (
     ID               INT,
     START     DATE,
     STOP     DATE,
     PATIENT    VARCHAR(50),
     ENCOUNTER        INT,
     CODE        VARCHAR(250),
     DESCRIPTION          VARCHAR(250)
);

DROP TABLE IF EXISTS careplans;
CREATE  TABLE careplans (
     ID               VARCHAR(50),
     START     DATE,
     STOP     DATE,
     PATIENT    VARCHAR(50),
     ENCOUNTER        INT,
     CODE        VARCHAR(250),
     DESCRIPTION          VARCHAR(250),
     REASONCODE          INT,
     REASONDESCRIPTION          VARCHAR(250)
);

DROP TABLE IF EXISTS conditions;
CREATE  TABLE conditions (
     ID               INT,
     START     DATE,
     STOP     DATE,
     PATIENT    VARCHAR(50),
     ENCOUNTER        INT,
     CODE        VARCHAR(250),
     DESCRIPTION          VARCHAR(250)
);

DROP TABLE IF EXISTS demographics;
CREATE  TABLE demographics (
     ID               INT,
     COUNTY    VARCHAR(50),
     NAME    VARCHAR(50),
     STNAME    VARCHAR(50),
     POPESTIMATE2015    INT,
     CTYNAME        VARCHAR(250),
     TOT_POP          DOUBLE,
     TOT_MALE          DOUBLE,
     TOT_FEMALE          DOUBLE,
     WHITE          DOUBLE,
     HISPANIC          DOUBLE,
     BLACK          DOUBLE,
     ASIAN          DOUBLE,
     NATIVE          DOUBLE,
     OTHER          DOUBLE,
     ONE          DOUBLE,
     TWO          DOUBLE,
     THREE          DOUBLE,
     FOUR          DOUBLE,
     FIVE          DOUBLE,
     SIX          DOUBLE,
     SEVEN          DOUBLE,
     EIGHT          DOUBLE,
     NINE          DOUBLE,
     TEN          DOUBLE,
     ELEVEN          DOUBLE,
     TWELVE          DOUBLE,
     THIRTEEN          DOUBLE,
     FOURTEEN          DOUBLE,
     FIFTHEEN          DOUBLE,
     SIXTEEN          DOUBLE,
     SEVENTEEN          DOUBLE,
     EIGHTEEN          DOUBLE,
     NUM1          DOUBLE,
     NUM2          DOUBLE,
     NUM3          DOUBLE,
     NUM4          DOUBLE,
     NUM5          DOUBLE,
     NUM6          DOUBLE,
     NUM7          DOUBLE,
     NUM8          DOUBLE,
     NUM9          DOUBLE,
     NUM10          DOUBLE,
     LESS_THAN_HS   VARCHAR(250),
     HS_DEGREE      VARCHAR(250),
     SOME_COLLEGE   VARCHAR(250),
     BS_DEGREE      VARCHAR(250)
);

DROP TABLE IF EXISTS devices;
CREATE  TABLE devices (
     START     DATE,
     STOP     DATE,
     PATIENT    VARCHAR(50),
     ENCOUNTER        INT,
     CODE        VARCHAR(250),
     DESCRIPTION          VARCHAR(250),
     UDI          VARCHAR(250)
);

DROP TABLE IF EXISTS encounters;
CREATE  TABLE encounters (
     Id               INT,
     START     DATE,
     STOP     DATE,
     PATIENT    VARCHAR(50),
     ORGANIZATION        VARCHAR(250),
     PROVIDER          VARCHAR(250),
     PAYER          VARCHAR(250),
     ENCOUNTERCLASS          VARCHAR(25),
     CODE          INT,
     DESCRIPTION          VARCHAR(250),
     BASE_ENCOUNTER_COST          FLOAT,
     TOTAL_CLAIM_COST          FLOAT,
     PAYER_COVERAGE          FLOAT,
     REASONCODE          INT,
     REASONDESCRIPTION          VARCHAR(250)
);

DROP TABLE IF EXISTS patients;
CREATE  TABLE patients (
     Id               INT,
     BIRTHDATE     DATE,
     DEATHDATE    VARCHAR(50),
     SSN    VARCHAR(50),
     DRIVERS    VARCHAR(20),
     PASSPORT    VARCHAR(210),
     PREFIX    VARCHAR(20),
     FIRST    VARCHAR(20),
     LAST    VARCHAR(20),
     SUFFIX    VARCHAR(20),
     MAIDEN    VARCHAR(20),
     MARITAL    VARCHAR(20),
     RACE    VARCHAR(20),
     ETHNICITY    VARCHAR(20),
     GENDER    VARCHAR(20),
     BIRTHPLACE    VARCHAR(20),
     ADDRESS    VARCHAR(20),
     CITY    VARCHAR(20),
     STATE    VARCHAR(20),
     COUNTY    VARCHAR(20),
     ZIP    VARCHAR(20),
     LAT    FLOAT,
     LON    FLOAT,
     HEALTHCARE_EXPENSES    VARCHAR(20),
     HEALTHCARE_COVERAGE    VARCHAR(20)
);

DROP TABLE IF EXISTS payers;
CREATE  TABLE payers (
     Id               INT,
     NAME    VARCHAR(20),
     ADDRESS    VARCHAR(20),
     CITY    VARCHAR(20),
     STATE_HEADQUARTERED    VARCHAR(20),
     ZIP    VARCHAR(20),
     PHONE    VARCHAR(200),
     AMOUNT_COVERED    VARCHAR(200),
     AMOUNT_UNCOVERED    VARCHAR(200),
     REVENUE    VARCHAR(200),
     COVERED_ENCOUNTERS    VARCHAR(200),
     UNCOVERED_ENCOUNTERS    VARCHAR(200),
     COVERED_MEDICATIONS    VARCHAR(200),
     UNCOVERED_MEDICATIONS    VARCHAR(200),
     COVERED_PROCEDURES    VARCHAR(200),
     UNCOVERED_PROCEDURES    VARCHAR(200),
     COVERED_IMMUNIZATIONS    VARCHAR(200),
     UNCOVERED_IMMUNIZATIONS    VARCHAR(200),
     UNIQUE_CUSTOMERS    VARCHAR(200),
     QOLS_AVG    VARCHAR(200),
     MEMBER_MONTHS    VARCHAR(200),
     LAT    FLOAT,
     LON    FLOAT,
     COUNTY    VARCHAR(200)
);





