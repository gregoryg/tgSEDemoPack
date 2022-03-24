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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH SupplyChainGraph

USE GRAPH SupplyChainGraph

BEGIN
CREATE LOADING JOB SupplyChainGraph_load_job FOR GRAPH SupplyChainGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/product.tsv\'}" TO VERTEX product VALUES ($"primary_id", $"name", $"price", $"formula") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/site.tsv\'}" TO VERTEX site VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/p_order.tsv\'}" TO VERTEX p_order VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/stocking.tsv\'}" TO VERTEX stocking VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/usedBy.tsv\'}" TO EDGE usedBy VALUES ($"from", $"to", $"formula_order", $"useAmount") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/deliver.tsv\'}" TO EDGE deliver VALUES ($"from", $"to", $"itemId") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/produce.tsv\'}" TO EDGE produce VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/prodOrder.tsv\'}" TO EDGE prodOrder VALUES ($"from", $"to", $"amount") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/SupplyChain/prodStocking.tsv\'}" TO EDGE prodStocking VALUES ($"from", $"to", $"amount") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
