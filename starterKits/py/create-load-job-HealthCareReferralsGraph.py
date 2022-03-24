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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH HealthCareReferralsGraph

USE GRAPH HealthCareReferralsGraph

BEGIN
CREATE LOADING JOB HealthCareReferralsGraph_load_job FOR GRAPH HealthCareReferralsGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/Specialty.tsv\'}" TO VERTEX Specialty VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/SubSpecialty.tsv\'}" TO VERTEX SubSpecialty VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/Prescriber.tsv\'}" TO VERTEX Prescriber VALUES ($"primary_id", $"pageRank", $"communityId") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/Claim.tsv\'}" TO VERTEX Claim VALUES ($"primary_id", $"rx_fill_date", $"ICD10Code", $"ICD10CodeDescription", $"CodeGroupTitle") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/Patient.tsv\'}" TO VERTEX Patient VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/submitted_by.tsv\'}" TO EDGE submitted_by VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/associated.tsv\'}" TO EDGE associated VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/specialty_subspecialty.tsv\'}" TO EDGE specialty_subspecialty VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/subspecialty_prescriber.tsv\'}" TO EDGE subspecialty_prescriber VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareReferrals/referral.tsv\'}" TO EDGE referral VALUES ($"from", $"to", $"num_patient") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
