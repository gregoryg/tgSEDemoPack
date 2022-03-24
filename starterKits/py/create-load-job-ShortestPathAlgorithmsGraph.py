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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH ShortestPathAlgorithmsGraph

USE GRAPH ShortestPathAlgorithmsGraph

BEGIN
CREATE LOADING JOB ShortestPathAlgorithmsGraph_load_job FOR GRAPH ShortestPathAlgorithmsGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/ShortestPathAlgorithms/Airport.tsv\'}" TO VERTEX Airport VALUES ($"primary_id", $"name", $"city", $"country", $"IATA", $"latitude", $"longitude") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/ShortestPathAlgorithms/flight_route.tsv\'}" TO EDGE flight_route VALUES ($"from", $"to", $"miles") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
