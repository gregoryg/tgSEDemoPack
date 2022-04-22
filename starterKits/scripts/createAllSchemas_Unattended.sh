#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

echo 'This installer will create all of the public starter kits on any tg instance'
echo ''
echo 'The options are:'
echo '   1. Install via gsql command line'
echo '   3. Install via python script and pyTigerGraph library'
echo ''
echo 'NOTE: Setup on TGCloud is onlt available thru python'
echo ''

while true; do
	echo ''
	echo 'What would you like to do today?'
	echo '   C/c - create the schemas'
	echo '   D/d - create the S3 data source'
	echo '   L/l - create the load jobs'
	echo '   R/r - run the load jobs'
	read -p "Answer: " tg_task
	if [ -z "$tg_task" ];
	then 
		echo 'Response needs to be c/d/l/r'
	elif [ $tg_task == 'C' ] || [ $tg_task == 'c' ]; then
		fn='create-schema'
		break
	elif [ $tg_task == 'D' ] || [ $tg_task == 'd' ]; then
		fn='tg_createDataS'
		break
	elif [ $tg_task == 'L' ] || [ $tg_task == 'l' ]; then
		fn='create-load-job'
		break
	elif [ $tg_task == 'R' ] || [ $tg_task == 'r' ]; then
		fn='run'
		break
	else
		echo 'Invalid entry, nmeeds to be c/d/l/r or C/D/L/R'
	fi
done

while true; do
	echo ''
	read -p "Do you want to install via GSQL or Python? (G/P/p): " install_type
	if [ -z "$install_type" ];
	then 
		echo "No input provided: should be create/load"
	elif [ $install_type == 'G' ] || [ $install_type == 'g' ] || [ $install_type == 'gsql' ]; then
		for file in "./gsql/"${fn}*.gsql
		do
		  	if [[ -f "$file" ]] ; then
		  		echo "running script: $file"
		  		gsql $file
		  	fi
		done
		break
	elif [ $install_type == 'P' ] || [ $install_type == 'p' ] || [ $install_type == 'python' ]; then
		echo "Running python install, configuring env variables"
		for file in "./py/"${fn}*.py
		do
	  		[[ -f "$file" ]] && echo "Publishing kit $file to the cloud via pyTigerGraph..."
			python3 $file
		done
		break
	else
		echo "Invalid input provided: should be g/p, try again"
	fi
done

echo ''
echo 'All starter kits staged'
echo ''






