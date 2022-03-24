#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

echo 'But first, lets ensure mysql is installed and running on the host'
echo ''

myResult=$(mysql -V)
if [[ "$myResult" == "" ]]; then
	echo 'mysql doesnt appear to be installed, please address'
	exit 2
fi

echo "select version();" > .version.txt
myResult2=$(mysql -u$1 -p\'$2\' < .version.txt)
rtv=$?
if [[ "$rtv" == 1 ]]; then
	echo 'mysql doesnt appear to be running, please address'
	echo ''
	exit 2
else
	echo "All good, lets go"
	echo ''
fi

FILE=/usr/local/mysql/bin/mysql
if [[ -f "$FILE" ]]; then
    echo 'mysql is installed at /usr/local/mysql.'
else
	echo 'if running on a Mac, mysql doesnt appear to be installed, please address'
	exit 2
fi

exit 0
