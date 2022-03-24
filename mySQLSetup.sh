#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

echo 'This script will create and populate a local mysql db for use in'
echo 'demonstrating the database schema import capbilities on Tigergraph'
echo ''
echo ' Run this command to ensure the user can login by providing a pw'
echo ''
echo '   mysql -ubob -p'
echo ''
echo ' for user bob, and supplying their password, login is successful.'
echo ''
echo " Running on ${OSTYPE}"
echo ''

echo 'Enter a user/pw to be used for local access'
echo ''
read -p "Username: " userName
echo ''
read -s -p "Password: " pw
echo ''
##./scripts/checkServerStatus.sh ${userName} ${pw}
retVal=1

if [[ "$retVal" == 2 ]]; then
	echo 'mysql doesnt appear to be installed or running, please address'
	echo ''
	exit 2
fi

echo "Install IMDB schema"
echo ''
mysql -u${userName} -p${pw} < ./imdb/scripts/createIMDBSchema.sql
echo "Install Synthea schema"
echo ''
mysql -u${userName} -p${pw} < ./synthea/scripts/createSyntheaSchema.sql
echo "Install LDBC schema"
echo ''
mysql -u${userName} -p${pw} < ./ldbc/scripts/createLDBCSchema.sql
echo "Install Airline schema"
echo ''
mysql -u${userName} -p${pw} < ./airline/scripts/createAirlineSchema.sql
echo "Install Recommendations schema"
echo ''
mysql -u${userName} -p${pw} < ./recommendations/scripts/createRecommendationsSchema.sql
echo ''
echo "Install TPC-DS schema"
echo ''
mysql -u${userName} -p${pw} < ./tpc-ds/scripts/createTPCDSSchema.sql
echo ''
echo "Install TPC-H schema"
echo ''
mysql -u${userName} -p${pw} < ./tpc-h/scripts/createTPCHSchema.sql
echo ''
echo "Install AdWorks schema"
echo ''
mysql -u${userName} -p${pw} < ./adWorks/scripts/create_adWorks_schema.sql
echo ''
echo ''
read -p "Do you also want to load data for each database? (Y/y or N/n): " loadData

if [[ "$loadData" == "Y" || "$loadData" == "y" ]]; then
	echo ''
    echo "lets do it"

	mysql --local-infile=1 -u${userName} -p${pw} < ./imdb/scripts/loadIMDBDataSamples.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./synthea/scripts/loadSyntheaData.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./ldbc/scripts/loadLDBCDataSample.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./airline/scripts/loadAirlineData.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./recommendations/scripts/loadRecommendationsData.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./tpc-ds/scripts/createTPCDSSchema.sql
	mysql --local-infile=1 -u${userName} -p${pw} < ./tpc-h/scripts/createTPCHSchema.sql

else
	echo ''
    echo "ok, maybe later"
fi


