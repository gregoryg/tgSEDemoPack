#!/bin/bash
## sync data files to S3

aws s3 cp ../airline/data/L_AIRLINE_ID.csv s3://tgdemodata/airline/
aws s3 cp ../airline/data/L_AIRPORT_ID.csv s3://tgdemodata/airline/
aws s3 cp ../airline/data/L_AIRPORT.csv s3://tgdemodata/airline/
aws s3 cp ../airline/data/On_Time_On_Time_Performance_2016_1.sample.csv s3://tgdemodata/airline/

aws s3 cp ../flightDelay/data/Airlines.csv s3://tgdemodata/flightDelay/
aws s3 cp ../flightDelay/data/Airports.csv s3://tgdemodata/flightDelay/
aws s3 cp ../flightDelay/data/Carriers.csv s3://tgdemodata/flightDelay/
aws s3 cp ../flightDelay/data/DistanceGroup.csv s3://tgdemodata/flightDelay/

aws s3 cp ../imdb/data/name.basics.sample.tsv s3://tgdemodata/imdb/
aws s3 cp ../imdb/data/title.basics.sample.tsv s3://tgdemodata/imdb/
aws s3 cp ../imdb/data/title.ratings.sample.tsv s3://tgdemodata/imdb/
aws s3 cp ../imdb/data/title.basics.justmovies.sample.tsv s3://tgdemodata/imdb/
aws s3 cp ../imdb/data/title.principals.sample.tsv s3://tgdemodata/imdb/

aws s3 cp ../ldbc/data/comment_hasCreator_person_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/comment_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/forum_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/forum_hasMember_person_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/organisation_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/person_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/person_hasInterest_tag_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/person_isLocatedIn_place_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/person_knows_person_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/person_workAt_organisation_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/place_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/post_hasCreator_person_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/post_sample.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/tag_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/tag_hasType_tagclass_0_0.csv s3://tgdemodata/ldbc/
aws s3 cp ../ldbc/data/tagclass_0_0.csv s3://tgdemodata/ldbc/

aws s3 cp ../synthea/data/addHeader.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/demographics.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/immunizations.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/organizations.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/procedures.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/allergies.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/devices.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/medications.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/patients.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/providers.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/careplans.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/encounters.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/normalizedSymptoms.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/payer_transitions.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/zipcodes.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/conditions.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/imaging_studies.csv s3://tgdemodata/synthea/
aws s3 cp ../synthea/data/payers.csv s3://tgdemodata/synthea/

## todo add observations.csv.zip