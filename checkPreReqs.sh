#!/bin/bash

echo ''
echo "The tgSolutionPack requires some basic tools and utilities be available, lets verify your env..."

RED='\033[0;31m'
NC='\033[0m' # No Color

echo ''
echo "First, for local installs, TigerGraph needs to be installed and services must be running. Lets verify that...."
read -p "Hit return to continue" return

echo ''

command -v gadmin >/dev/null 2>&1 || { echo -e >&2 "${RED}TigerGraph is not installed on this host, local install not available.${NC}"; }

resp=$(gsql -v 2>&1)
if [[ "$resp" == *"refused"* || "$resp" == *"not found"* ]]; then
    echo -e "${RED}Tigergraph does not appear to be running on this host. Or perhaps the current user is not configured to access the service?${NC}"
    echo 'You can still continue with a remote (python) installed for another host'
    while true; do
        read -p "  Do you want to continue with remote install pre-requisites? (y/n): " doRemote
        case $doRemote in
            [Yy]* ) 
                "Continue checks..."
                break
            [Nn]* ) 
                "Setup tigergraph and rerun the installer"
                exit
            * ) echo 
                "Please answer yes or no."
        esac
    done
else 
	echo "Services up and running locally"
fi

echo ''
echo "For remote installations, such as TGCloud, python v3 and the pyTigerGraph package is required "
read -p "Hit return to perform these checks " return

python3 --version
result=$?
if [[ $result=0 ]]; then
	echo 'Python v3 is installed. We are all good'
    echo 'python3' > .pycmd
else
    python --version
    result=$?
    if [[ $result=0 ]]; then
        if [[ $(python --version) != *3.* ]]; then
            echo "${RED}Only python 2 is installed, please install python 3.8 or higher...${NG}"
        else
            echo "All good python command is set to v3"
            echo 'python' > .pycmd
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
    echo -e "${RED}pyTigerGraph is not installed you can install using this command: pip install pyTigerGraph.${NC}"
fi

echo ''
echo 'You will need an AWS client access token to access the demo data which is stored on S3'
echo '  A token can be retrieved from the AWS Console, or by contacting a friendly SE'
echo '   The format of a token looks like this:'
echo '     Access key ID,Secret access key'
echo '     ***********OC7EB,**************LPdAZ'
echo ''

read -p "Pre-requisite checks complete, hit return to continue" return
echo ''
