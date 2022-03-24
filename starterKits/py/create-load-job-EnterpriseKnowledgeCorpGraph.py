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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH EnterpriseKnowledgeCorpGraph

USE GRAPH EnterpriseKnowledgeCorpGraph

BEGIN
CREATE LOADING JOB EnterpriseKnowledgeCorpGraph_load_job FOR GRAPH EnterpriseKnowledgeCorpGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/Person.tsv\'}" TO VERTEX Person VALUES ($"primary_id", $"gender") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/Company.tsv\'}" TO VERTEX Company VALUES ($"primary_id", $"registered_capital") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/Project.tsv\'}" TO VERTEX Project VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/WorkFor.tsv\'}" TO EDGE WorkFor VALUES ($"from", $"to", $"title") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/PersonInvestCompany.tsv\'}" TO EDGE PersonInvestCompany VALUES ($"from", $"to", $"invest_year", $"amount", $"control_type") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/CompanyInvestCompany.tsv\'}" TO EDGE CompanyInvestCompany VALUES ($"from", $"to", $"invest_year", $"amount", $"control_type") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCorp/BidFor.tsv\'}" TO EDGE BidFor VALUES ($"from", $"to", $"price", $"solution") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
