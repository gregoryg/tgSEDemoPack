#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This script will will install an individual starter kit

echo 'This installer will install any starter kit on any tg instance'
echo ''
echo 'Install options are:'
echo '   1. GSQL - Install via gsql command line to a local'
echo '   3. Python - Install via python script and pyTigerGraph library to a remote instance'
echo ''
echo '     NOTE: Setup on TGCloud is only available thru python install'
echo ''

chadifier="   - "
while true; do
	KITNUMBER=1
	for file in "./gsql/"create-schema*.gsql
	do
		IFS='-'
		if [[ -f "$file" ]] ; then
			read -ra ADDR <<< "$file"

			kitNumArray+=( ${KITNUMBER} )
			kitNameArray+=( ${ADDR[2]::${#ADDR[2]}-10} )
			if [[ ${KITNUMBER} -gt 9 ]]; then
				echo "  ${KITNUMBER}  -  ${ADDR[2]::${#ADDR[2]}-10} "
			else
				echo "  ${KITNUMBER}   -  ${ADDR[2]::${#ADDR[2]}-10} "
			fi
			((KITNUMBER=KITNUMBER+1))
		fi
	done

	echo ''
	echo "choose the kit you want to work with"
	read -p "     Valid kits are 1 thru ${KITNUMBER}: " kitNumber

	## make sure we got a valid number
	if [ -n "$kitNumber" ] && [ "$kitNumber" -eq "$kitNumber" ] 2>/dev/null; then
		echo ''
		echo "starter kit choosen is: " ${kitNumArray[kitNumber-1]}
		echo " corresponding to kit: " ${kitNameArray[kitNumber-1]}
		break
	else
  		echo "Needs to be a number between 1 and ${KITNUMBER-1}"
  		echo ''
	fi
done

## to python or python3
pycmd=$(<.pycmd)
echo "python command is: $pycmd"

while true; do
	echo ''
	echo 'What would you like to do today?'
	echo '   C/c - create kit schema'
	echo '   D/d - create the S3 data source - NOTE: in order to load data, you need a data source'
	echo '   L/l - create a load job for a kit'
	echo '   R/r - run a load job'
	echo '   A/a - Do all 3, create schema and job, and run load for a kit'
	read -p "Answer: " tg_task
	if [ -z "$tg_task" ];
	then 
		echo 'Response needs to be c/d/l/r'
	elif [ $tg_task == 'C' ] || [ $tg_task == 'c' ]; then
		fn='create-schema'
		break
	elif [ $tg_task == 'D' ] || [ $tg_task == 'd' ]; then
		fn='tg_createDataSource.py'
		break
	elif [ $tg_task == 'L' ] || [ $tg_task == 'l' ]; then
		fn='create-load-job'
		break
	elif [ $tg_task == 'R' ] || [ $tg_task == 'r' ]; then
		fn='run-load-job'
		break
	elif [ $tg_task == 'A' ] || [ $tg_task == 'a' ]; then
		fn='all'
		break
	else
		echo 'Invalid entry, needs to be c/d/l/r or C/D/L/R'
	fi
done

while true; do
	echo ''
	read -p "Do you want to install via GSQL or Python? (G/P/p): " install_type
	if [ -z "$install_type" ];
	then 
		echo "No input provided: should be create/load"
	elif [ $install_type == 'G' ] || [ $install_type == 'g' ] || [ $install_type == 'gsql' ]; then
		echo "Cool, gsql it is..."
		echo "executing this command: gsql ./gsql/${fn}-${kitNameArray[kitNumber-1]}Graph.gsql"
	##	gsql "./gsql/${fn}-${kitNameArray[kitNumber-1]}Graph.gsql"
		break
	elif [ $install_type == 'P' ] || [ $install_type == 'p' ] || [ $install_type == 'python' ]; then
		echo "Cool, python it is..."
		echo "Lets make sure python is installed and configured"
		python3 --version
		result=$?
		if [[ $result=0 ]]; then
			echo 'Python installed, checking version'
		else
			echo 'Python is required to install to TGCloud, but not for local installs thru gsql...'
				read -p "     Would you like to continue (Y), or exit and get your python together (N): " yesOrNo
				if [[ $yesOrNo == 'N' ]] || [[ $yesOrNo == 'n' ]]; then
					echo 'Fine, try again once python *and the pyTigerGraph library are installed'
					exit 0
				elif [[ $yesOrNo == 'Y' ]] || [[ $yesOrNo == 'y' ]]; then
					echo "Lets keep going..."
					echo ''
				else
					echo 'I need a Yes or No'
					exit 0
				fi
		fi
		echo 'Update the connection props...'
		./updateConnProps.sh
		echo ''
		if [[ $fn == 'tg_createDataSource.py' ]]; then
			echo "executing the create data source command: python ./py/${fn}"
			$pycmd ./py/tg_createDataSource.py
		elif [[ $fn == 'all' ]]; then
			echo "executing all create /load steps command: $pycmd ./py/${fn}-${kitNameArray[kitNumber-1]}Graph.py"
			$pycmd "./py/create-schema-${kitNameArray[kitNumber-1]}Graph.py"
			$pycmd "./py/create-load-job-${kitNameArray[kitNumber-1]}Graph.py"
			$pycmd "./py/run-load-job-${kitNameArray[kitNumber-1]}Graph.py"
		else
			echo "executing this command: $pycmd ./py/${fn}-${kitNameArray[kitNumber-1]}Graph.py"
			$pycmd "./py/${fn}-${kitNameArray[kitNumber-1]}Graph.py"
		fi
		echo '' 
		break
	else
		echo "Invalid input provided: should be g/p, try again"
	fi
done

echo ''
echo "Starter kit ${kitNameArray[kitNumber-1]} setup is complete"
echo ''







