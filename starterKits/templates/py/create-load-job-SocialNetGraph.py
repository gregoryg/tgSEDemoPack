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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH SocialNetGraph

USE GRAPH SocialNetGraph

BEGIN
CREATE LOADING JOB SocialNetGraph_load_job FOR GRAPH SocialNetGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/BusRide.tsv\'}" TO VERTEX BusRide VALUES ($"primary_id", $"eventDate") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/TrainRide.tsv\'}" TO VERTEX TrainRide VALUES ($"primary_id", $"eventDate") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/Flight.tsv\'}" TO VERTEX Flight VALUES ($"primary_id", $"eventDate") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/FundsTransfer.tsv\'}" TO VERTEX FundsTransfer VALUES ($"primary_id", $"amount", $"transferEvent") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/PhoneCall.tsv\'}" TO VERTEX PhoneCall VALUES ($"primary_id", $"eventDate", $"callLength", $"callType") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/Person.tsv\'}" TO VERTEX Person VALUES ($"primary_id", $"fullName", $"dob", $"email", $"gender", $"ethic_group") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/HotelStay.tsv\'}" TO VERTEX HotelStay VALUES ($"primary_id", $"eventDate") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/Phone.tsv\'}" TO VERTEX Phone VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/BankAccount.tsv\'}" TO VERTEX BankAccount VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/CaseReport.tsv\'}" TO VERTEX CaseReport VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/Address.tsv\'}" TO VERTEX Address VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasCaseReport.tsv\'}" TO EDGE hasCaseReport VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasFundsTransfer.tsv\'}" TO EDGE hasFundsTransfer VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasHotelStay.tsv\'}" TO EDGE hasHotelStay VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasBusRide.tsv\'}" TO EDGE hasBusRide VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasFlight.tsv\'}" TO EDGE hasFlight VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasPhone.tsv\'}" TO EDGE hasPhone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasTrainRide.tsv\'}" TO EDGE hasTrainRide VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasBankAccount.tsv\'}" TO EDGE hasBankAccount VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasHomeAddress.tsv\'}" TO EDGE hasHomeAddress VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SocialNet/hasPhoneCall.tsv\'}" TO EDGE hasPhoneCall VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
