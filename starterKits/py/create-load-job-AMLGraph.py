#!/usr/bin/env python
# coding: utf-8

# # 1 - TigerGraph Schema Refresh Job
# 
# This script is used to automatically refresh the Stanza TigerGraph instance on TGCloud
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Create load jobs
#     4. Run load jobs
# 


# FETCH PACKAGES
import subprocess
import sys

import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# 
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "http://localhost"
username = "tigergraph_user"
password = "tigergraph_pw" 

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# Create load jobs

print(conn.gsql('''
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH AMLGraph

USE GRAPH AMLGraph

BEGIN
CREATE LOADING JOB AMLGraph_load_job FOR GRAPH AMLGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/Transaction.tsv\'}" TO VERTEX Transaction VALUES ($"primary_id", $"ts", $"amount") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User.tsv\'}" TO VERTEX User VALUES ($"primary_id", $"signupEpoch", $"mobile", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/Device_Token.tsv\'}" TO VERTEX Device_Token VALUES ($"primary_id", $"is_banned", $"os_name", $"os_version", $"model", $"carrier", $"is_rooted", $"is_emulator", $"device_name", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/Payment_Instrument.tsv\'}" TO VERTEX Payment_Instrument VALUES ($"primary_id", $"token_handle", $"token_type", $"card_issuing_country_iso2", $"card_issuing_bank", $"card_bin", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User_Transfer_Transaction.tsv\'}" TO EDGE User_Transfer_Transaction VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User_Recieve_Transaction.tsv\'}" TO EDGE User_Recieve_Transaction VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User_to_Device.tsv\'}" TO EDGE User_to_Device VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User_to_Payment.tsv\'}" TO EDGE User_to_Payment VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/AML/User_Refer_User.tsv\'}" TO EDGE User_Refer_User VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
