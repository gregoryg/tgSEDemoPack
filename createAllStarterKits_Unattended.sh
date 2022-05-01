#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

echo 'This installer will create schemas for all of the public starter kits on any tg instance'
echo ''
echo 'The options are:'
echo '   1. Install via gsql command line'
echo '   3. Install via python script and pyTigerGraph library'
echo ''
echo 'NOTE: Setup on TGCloud is onlt available thru python'
echo ''

if [ ! -f ./.prechk ]
then
	echo ''
	echo "Need to run the pre-checks first"
	exit 22
fi

props_file='./tg.properties'
if [ -f "$props_file" ]
then
  while IFS='=' read -r key value
  do
    key=$(echo $key | tr '.' '_')
    eval ${key}=\${value}
  done < "$props_file"
else
	echo 'Need to set the properties first by running the installer script'
	exit 11
fi

cd starterKits

install_type=$1
if [ $# -eq 0 ]
  then
    echo "No arguments supplied, exiting"
    exit 44
fi
echo "Will install using method $install_type"

if [ $install_type == 'p' ] || [ $install_type == 'P' ] || [ $install_type == 'python' ]; then
	echo "create schemas...."
	for file in "./scripts/py/"create-schema-*.py
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##python $file
		fi
	done
	echo "create data source...."
	## gsql p $tg_password ./scripts/py/tg_createDataSource.py

	echo "create load jobs...."
	for file in "./scripts/py/"create-load-*.py
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##python $file
		fi
	done
	echo "run load jobs...."
	for file in "./scripts/py/"run-load-job-*.py
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##python $file
		fi
	done
elif [ $install_type == 'G' ] || [ $install_type == 'g' ] || [ $install_type == 'gsql' ]; then
	echo "create schemas...."
	for file in "./scripts/gsql/"create-schema-*.gsql
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##gsql -p $tg_password $file
		fi
	done
	echo "create data source.... gsql password is $tg_password"
	## gsql p $tg_password ./scripts/gsql/tg_createDataSource.gsql

	echo "create load jobs...."
	for file in "./scripts/gsql/"create-load-*.gsql
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##gsql -p $tg_password $file
		fi
	done
	echo "run load jobs...."
	for file in "./scripts/gsql/"run-load-job-*.gsql
	do
		if [[ -f "$file" ]] ; then
		echo "running script: $file"
		##gsql -p $tg_password $file
		fi
	done

else
	echo 'The install method needs to be p/python or g/gsql, please specifiy'
	exit 33
fi

echo ''
echo 'All starter kits staged'
echo ''






