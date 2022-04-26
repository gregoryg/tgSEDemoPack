#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

echo ''
echo "Welcome to the TGSEDemo Pack Installer....."
echo '  This package will install TigerGraph graph solutions (graph and data) onto any tigergraph instance including:'
echo '     1) docker - docker container running locally on a mac'
echo '     2) local - from the local computer to a Cloud/VM instance'
echo '     3) any cloud vm'
echo '     4) TGCloud - using python package to deploy to an existing TGCLoud instance'
echo ''
echo 'A key feature of the SEDemo pack is that is supports deploying multiple demo solutions (Cust360 and Fraud for example)'
echo '   to the same instance, so that a user can explore any/all solutions from a single Graph Studio UI'

if [ ! -f ./.prechk ]
then
	echo ''
	echo "First, lets check on some pre-requisites, to make sure your environment is ready"
	./checkPreReqs.sh
fi

echo "Would you like to install a Customer Demo or a TigerGraph Starter Kit?"
echo ''

while true; do
	read -p "  Enter Custom Demo/Starter Kit - C/c/S/s: " choice
	if [[ "$choice" == *"S"* || "$choice" == *"s"* ]]; then
		cd starterKits
		./tgSolutionKitInstall.sh
		exit 0
	elif [[ "$choice" == *"C"* || "$choice" == *"c"* ]]; then
		echo 'Custom demo pack it is.'
		break
	else
		echo "Please provide a valid entry"
	fi
done

props_file='./starterKit/tg.properties'
if [ -f "$props_file" ]
then
  while IFS='=' read -r key value
  do
    key=$(echo $key | tr '.' '_')
    eval ${key}=\${value}
  done < "$props_file"
else
	read -p "Please enter the tigergraph user (tigergraph): " tguser
	if [[ ! -z $tguser ]];
	then 
    	tg_username=$tguser
	else
    	tg_username="tigergraph"
	fi
	read -p "Please enter the tigergraph user password (tigergraph): " tgpw
	if [[ ! -z $tgpw ]];
	then 
    	tg_password=$tgpw
	else
    	tg_password="tigergraph"
	fi
fi

data_file='./packages/tpcds/data/customer.csv'
if [ -f "$data_file" ]
then
	echo 'Using the embedded dataset diles.'
	;;
else
	echo "Next, lets retrieve the dataset content for these demos from S3."
	echo 'This may take a minute....'

	cd ..
	wget https://tgsedemodatabucket.s3.amazonaws.com/tgSEDemoDataPack.tar.gz
	tar -xzvf tgSEDemoDataPack.tar.gz &>/dev/null
	rm -rf tgSEDemoDataPack.tar.gz
	cd tgSEDemoPack

	echo ''
	echo 'Datasets added to custom demo packs'
fi


echo ''
echo "Custom demo install process "
echo ""
echo "1     - Entity Resolution(MDM)"
echo "2     - Fraud Detection"
echo "3     - LDBC Benchmark"
echo "4     - TPC-DS Benchmark"
echo "5     - Synthea HealthCare"
echo '6     - IMDB'
echo "7     - Customer360"
echo '8     - Recommendations'
echo '9     - AML Sim'
echo '10    - Ontime Flight Performance'
echo '11    - Adworks'
echo '12    - NetoworkIT Impact Analysis Graph'
echo "A/a   - Install all of the packs"
echo "Q/q   - To exit the script"
echo "mysql - Stage all of the source data to a local mysql db - NOTE assumes you have mysql installed and accessible..."
echo ''

while true; do
read -p "Pick a number, or enter a/A for all: " choice

	case $choice in

		1)
			echo ''
			echo "Install Entity Resolution (MDM)"
			gsql -p $tg_password packages/entityResMDM/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/entityResMDM/scripts/02-load-data.gsql
			gsql -p $tg_password packages/entityResMDM/scripts/03-add-queries.gsql
			break
		    ;;
		2)
		    echo "Install Anti-Fraud (AML)"
			gsql -p $tg_password packages/fraud/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/fraud/scripts/02-load-data.gsql
			break
		    ;;
		3)
			echo ''
			echo "Install LDBC - with small sample dataset"
			gsql -p $tg_password packages/ldbc/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/ldbc/scripts/02-load-data-sample.gsql
			break
		    ;;
		4)
		    echo ''
		    echo "Install TPC-DS"
			gsql -p $tg_password packages/tpcds/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/tpcds/scripts/02-load-data.gsql
			break
		    ;;
		5)
		    echo ''
		    echo "Install Synthea"
			gsql -p $tg_password packages/synthea/scripts/createSyntheaSchema.gsql
			./packages/synthea/scripts/installLoadJobs.sh
			gsql -p $tg_password packages/synthea/scripts/runSyntheaLoadJobs.gsql
			break
		    ;;
		6)
		    echo ''
		    echo "Install IMDB"
		    gsql -p $tg_password packages/imdb/scripts/01-create-schema.gsql
		    gsql -p $tg_password packages/imdb/scripts/02-load-data.gsql
			break
		    ;;
		7)
		    echo ''
		    echo "Install Cust360"
		    ./packages/cust360/installCust360.sh
			break
		    ;;
		8)
		    echo ''
		    echo "Install Recommendations"
			gsql -p $tg_password packages/recommendations/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/recommendations/scripts/02-load-data.gsql
			break
		    ;;
		9)
		    echo ''
		    echo "Install AML Sim"
			gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
			gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
			break
		    ;;
		10)
		    echo ''
		    echo "Install Ontime Perf Graph"
			gsql work-in-progress/airline/scripts/01-create-schema.gsql
			gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
			break
		    ;;
		11)
		    echo ''
		    echo "Install Adworks Graph"
			gsql work-in-progress/adWorks/scripts/01-create-schema.gsql
			break
		    ;;
		12) 
		    echo ''
		    echo "Install NetoworkIT Impact Analysis Graph"
			gsql -p $tg_password packages/NetworkITResOpt/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/NetworkITResOpt/scripts/02-load-data.gsql
			break
			;;
		13) 
		    echo ''
		    echo "Install Shortest Path Flights Graph"
			gsql -p $tg_password packages/shortestPathFlights/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/shortestPathFlights/scripts/02-load-data.gsql
			break
			;;
		a|A)
		    echo ''
		    echo 'Lets load all of the schemas'
			gsql -p $tg_password packages/entityResMDM/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/entityResMDM/scripts/02-load-data.gsql
			gsql -p $tg_password packages/entityResMDM/scripts/03-add-queries.gsql
		    echo "Install Fraud/AML - data tbd"
			gsql -p $tg_password packages/fraud/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/fraud/scripts/02-load-data.gsql
			echo ''
			echo "Install LDBC - with small sample dataset"
			gsql -p $tg_password packages/ldbc/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/ldbc/scripts/02-load-data-sample.gsql
		    echo ''
		    echo "Install TPC-DS - data tbd"
			gsql -p $tg_password packages/tpcds/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/tpcds/scripts/02-load-data.gsql
		    echo ''
		    echo "Install Synthea"
			gsql -p $tg_password packages/synthea/scripts/createSyntheaSchema.gsql
			./packages/synthea/scripts/installLoadJobs.sh
			gsql -p $tg_password packages/synthea/scripts/runSyntheaLoadJobs.gsql
		    echo ''
		    echo "Install IMDB"
		    gsql -p $tg_password packages/imdb/scripts/01-create-schema.gsql
		    gsql -p $tg_password packages/imdb/scripts/02-load-data.gsql
		    echo ''
		    echo "Install Cust360"
		    ./packages/cust360/installCust360.sh
		    echo ''
		    echo "Install Recommendations"
			gsql -p $tg_password packages/recommendations/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/recommendations/scripts/02-load-data.gsql
		    echo ''
		    echo "Install AML Sim"
			gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
			gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
		    echo "Install Ontime Perf Graph"
			gsql work-in-progress/airline/scripts/01-create-schema.gsql
			gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
		    echo ''
		    echo "Install Adworks Graph"
			gsql work-in-progress/adWorks/scripts/01-create-schema.gsql
		    echo ''
		    echo ''
		    echo "Install NetoworkIT Impact Analysis Graph"
			gsql -p $tg_password packages/NetworkITResOpt/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/NetworkITResOpt/scripts/01-create-schema.gsql
		    echo ''
		    echo "Install Shortest Path Flights Graph"
			gsql -p $tg_password packages/shortestPathFlights/scripts/01-create-schema.gsql
			gsql -p $tg_password packages/shortestPathFlights/scripts/02-load-data.gsql
			break
		    ;;
		mysql)
		    echo ''
		    echo 'Lets stage all of the schemas to mysql'
		    echo ''
		    ./mcySQLSetup.sh
		    echo ''
			break
		    ;;
		q)
			echo 'exiting installer...'
			break
			;;
		Q)
			echo 'exiting installer...'
			break
			;;		
		*) 
			echo "Sorry, $choice is an invalid option, enter a valid option."
	    	;;
	esac
done

echo ''
echo 'Finished with setup....'
echo ''
