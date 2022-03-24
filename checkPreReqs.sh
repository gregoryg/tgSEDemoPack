#!/bin/bash

echo ''
echo "The tgSolutionPack requires some basic tools and utilities be available, lets verify your env..."
echo ''
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "For a local, gsql based install, Tigergraph must be installed..."
command -v gadmin >/dev/null 2>&1 || { echo -e >&2 "${RED}TigerGraph is not installed on this host, local install not available.${NC}"; }

echo "Ensure TigerGraph is currently running (check gadmin) and gsql is available"
resp=$(gsql -v 2>&1)
if [[ "$resp" == *"refused"* || "$resp" == *"not found"* ]]; then
    echo -e "${RED}Tigergraph does not appear to be running on this host, please start it using gadmin.${NC}"
else 
	echo "Services up and running"
fi

echo ''
echo "For remote installations, such as TGCloud, python-3 is required your version is"
python3 --version
result=$?
if [[ $result=0 ]]; then
	echo 'Python v3 is installed. We are all good'
else
    python --version
    result=$?
    if [[ $result=0 ]]; then
        if [[ $(python --version) != *3.* ]]; then
            echo "${RED}Only python 2 is installed, please update${NG}"
        else
            echo "All good python command is set to v3"
        fi
    else
        echo "${RED}Python v3 needs to be installed${NG}"
    fi
fi

echo ''
echo "This utility uses the python pyTigerGraph library, which needs to be installed via pip"
pyTGresult="$(pip list |grep Tiger 2>&1)"
if [[ $pyTGresult == *"pyTigerGraph"* ]];
then
    echo "pyTigerGraph installed, versions are:"
    echo $pyTGresult
else
    echo -e "${RED}pyTigerGraph is not installed you can install using pip install pyTigerGraph.${NC}"
fi

echo ''
echo 'You will need an AWS client access token to access the demo data which is stored on S3'
echo '  A token can be retrieved from the AWS Console, or by contacting a friendly SE'
echo '   The format of a token looks like this:'
echo '     Access key ID,Secret access key'
echo '     ***********OC7EB,**************LPdAZ'
echo ''