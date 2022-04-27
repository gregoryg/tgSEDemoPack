#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## Get TG connection info

props_file='./tg.properties'
if [ -f "$props_file" ]
then
  while IFS='=' read -r key value
  do
    key=$(echo $key | tr '.' '_')
    eval ${key}=\${value}
  done < "$props_file"
else
  echo "$props_file file not found, using defaults"
  ## Default to local docker
  tg_host='http://localhost'
  tg_username="tigergraph_user"
  tg_password="tigergraph_pw"
  tg_s3_data_source="tg_s3_data_source"
  tg_s3_bucket_name="tg-workshop-us"
  tg_access_key_ID="AKIA45R*********"
  tg_secret_access_key="jeO8GXIVCpjDkYVccHfuLL**************"
fi

echo ''
echo 'The current property settings are:'
echo ''
echo "tg_host = $tg_host"
echo "tg_username = $tg_username"
echo "tg_password = $tg_password"
echo "tg_s3_data_source = $tg_s3_data_source"
echo "tg_s3_bucket_name = $tg_s3_bucket_name"
echo "tg_access_key_ID = $tg_access_key_ID"
echo "tg_secret_access_key = $tg_secret_access_key"
echo ''

read -p "Do you want to modify any of these properties? (Y/n) " updateProps
if [[ "$updateProps" == *"Y"* || "$updateProps" == *"y"* || "$updateProps" == *"Yes"* || "$updateProps" == *"yes"* ]]; then
    echo "Updating the props..."
else
    echo "Continuing with current props..."
    echo ''
    exit 0
fi

echo 'Enter the connection info for the TigerGraph instance. Hit enter for no change'
echo ''
read -p "tg_host <$tg_host>: " new_host
if [[ ! -z $new_host ]];
then 
    tg_host_new=$new_host
else
    tg_host_new=$tg_host
fi
echo ''
read -p "tg_username <$tg_username>: " new_username
if [[ ! -z $new_username ]];
then 
    tg_username_new=$new_username
else
    tg_username_new=$tg_username
fi
echo ''
read -p "tg_password <$tg_password>: " new_password
if [[ ! -z $new_password ]];
then 
    tg_password_new=$new_password
else
    tg_password_new=$tg_password
fi
echo ''
read -p "tg_s3_data_source <$tg_s3_data_source>: " new_tg_s3_data_source
if [[ ! -z $new_tg_s3_data_source ]];
then 
    tg_datasource_new=$new_tg_s3_data_source
else
    tg_datasource_new=$tg_s3_data_source
fi
echo ''
echo 'Dont change the bucket name unless the new bucket has been built to contain the datasets'
echo ''
read -p "tg_s3_bucket_name <$tg_s3_bucket_name>: " new_tg_s3_bucket_name
if [[ ! -z $new_tg_s3_data_source ]];
then 
    tg_bucketname_new=$new_tg_s3_bucket_name
else
    tg_bucketname_new=$tg_s3_bucket_name
fi
echo ''
read -p "tg_access_key_ID <$tg_access_key_ID>: " new_tg_access_key_ID
if [[ ! -z $new_tg_access_key_ID ]];
then 
    tg_access_key_ID_new=$new_tg_access_key_ID
else
    tg_access_key_ID_new=$tg_access_key_ID
fi
echo ''
read -p "tg_secret_access_key <$tg_secret_access_key>: " new_tg_secret_access_key
if [[ ! -z $new_tg_secret_access_key ]];
then 
    tg_secret_access_key_new=$new_tg_secret_access_key
else
    tg_secret_access_key_new=$tg_secret_access_key
fi

echo ''
echo 'NOTE: these credentails will be written to the python load scripts in clear text'
echo ''
echo "Host new is: $tg_host_new"
echo ''
echo 'Configure the S3 access token'
echo ''

## need to escape special chars in any imput
tg_host_new_escaped=$(printf '%s\n' "$tg_host_new" | sed -e 's/[\/&]/\\&/g')
tg_host_escaped=$(printf '%s\n' "$tg_host" | sed -e 's/[\/&]/\\&/g')
tg_key_escaped_new=$(printf '%s\n' "$tg_secret_access_key_new" | sed -e 's/[\/&]/\\&/g')


## add the keys to the load job template
sed "s/ACCESSKEYID/${tg_access_key_ID_new}/g" ./templates/py/tg_createDataSource_orig.py > bob.tmp
sed "s/SECRETACCESSKEY/${tg_key_escaped_new}/g" bob.tmp > ./templates/py/tg_createDataSource.py
rm -rf bob.tmp

## Write new props to tg.properties file
echo "update the props filename"
echo "tg_host=$tg_host_new" > ./tg.properties
echo "tg_username=$tg_username_new" >> ./tg.properties
echo "tg_password=$tg_password_new" >> ./tg.properties
echo "tg_s3_data_source=$tg_datasource_new" >> ./tg.properties
echo "tg_s3_bucket_name=$tg_bucketname_new" >> ./tg.properties
echo "tg_access_key_ID=$tg_access_key_ID_new" >> ./tg.properties
echo "tg_secret_access_key=$tg_secret_access_key_new" >> ./tg.properties

## Replace tokens in the template with actual values
for file in "./templates/py/"*.py
  do
    sed "s/${tg_host_escaped}/${tg_host_new_escaped}/g" $file > bob.tmp
    sed "s/${tg_username}/${tg_username_new}/g" bob.tmp > bob2.tmp
    sed "s/${tg_password}/${tg_password_new}/g" bob2.tmp > bob3.tmp

    newFile=$(echo "$file" | sed "s/templates/scripts/")
    ##echo "adding props to file: $newFile"

    mv bob3.tmp $newFile
    rm -rf bob*.tmp
  done

echo 'Create the gsql scripts'
cp ./templates/gsql/*.gsql ./scripts/gsql/

echo ''
echo 'Python scripts updated to reflect connection info..'
