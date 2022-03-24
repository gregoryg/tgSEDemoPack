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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH InDBMLGraph

USE GRAPH InDBMLGraph

BEGIN
CREATE LOADING JOB InDBMLGraph_load_job FOR GRAPH InDBMLGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBML/USER.tsv\'}" TO VERTEX USER VALUES ($"primary_id", SPLIT($"theta", "#")) USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBML/MOVIE.tsv\'}" TO VERTEX MOVIE VALUES ($"primary_id", $"name", $"avg_rating", SPLIT($"x", "#")) USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBML/rate.tsv\'}" TO EDGE rate VALUES ($"from", $"to", $"rating", $"label") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
