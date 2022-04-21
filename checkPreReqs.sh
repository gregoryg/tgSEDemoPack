#!/bin/bash

echo ''
echo "The tgSolutionPack requires some basic tools and utilities be available, lets verify your env..."

RED='\033[0;31m'
NC='\033[0m' # No Color

echo ''
echo "First, for local installs, TigerGraph needs to be installed and services must be running. Lets verify that...."
read -p "Hit return to continue " return

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
                echo "Continue checks..."
                break
                ;;
            [Nn]* ) 
                echo "Setup tigergraph and rerun the installer"
                exit
                ;;
            * ) 
                echo "Please answer yes or no."
                ;;
        esac
    done
else 
	echo "Services up and running locally"
fi

echo ''
echo "For remote installations, such as to TGCloud, python v3 and the pyTigerGraph package are required "
read -p "Hit return to perform these checks " return

python3 --version
result=$?
if [[ $result=0 ]]; then
	echo 'Python v3 is installed. So we are all good there'
    echo 'python3' > ./starterKits/.pycmd
else
    python --version
    result=$?
    if [[ $result=0 ]]; then
        if [[ $(python --version) != *3.* ]]; then
            echo "${RED}Only python 2 is installed, please install python 3.8 or higher...${NG}"
        else
            echo "All good python command is set to v3"
            echo 'python' > ./starterKits/.pycmd
        fi
    else
        echo -e "${RED}Python v3 needs to be installed${NG}"
    fi
fi

echo ''
echo "This utility uses the python pyTigerGraph library, which needs to be installed via pip"
read -p "Hit return to continue " return

pipVersion="$(pip --version 2>&1)"
if [[ $pipVersion == *"python3"* ]];
then
    echo 'pip points to python 3, check'
    pipcmd='pip'
else
    pip3Version="$(pip3 --version 2>&1)"
    if [[ $pip3Version == *"python3"* ]];
    then
        echo 'pip3points to python 3, check' 
        pipcmd='pip3'
    else
        echo -e "{RED}pip v3 needs to be installed${NG}"
    fi
fi

echo ''
pyTGresult="$($pipcmd list --format=columns | grep Tiger 2>&1)"
if [[ $pyTGresult == *"pyTiger"* ]];
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

read -p "Pre-requisite checks complete, hit return to continue " return
echo ''

echo "Pre-checks completed on $(date)" > .prechk

