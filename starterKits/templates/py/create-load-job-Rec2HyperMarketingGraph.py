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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH Rec2HyperMarketingGraph

USE GRAPH Rec2HyperMarketingGraph

BEGIN
CREATE LOADING JOB Rec2HyperMarketingGraph_load_job FOR GRAPH Rec2HyperMarketingGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/product.tsv\'}" TO VERTEX product VALUES ($"primary_id", $"name", $"latitude", $"longitude") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/feature.tsv\'}" TO VERTEX feature VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/customer.tsv\'}" TO VERTEX customer VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/history.tsv\'}" TO VERTEX history VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/demographic.tsv\'}" TO VERTEX demographic VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/context.tsv\'}" TO VERTEX context VALUES ($"primary_id", $"ctxValue") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/demo_customer.tsv\'}" TO EDGE demo_customer VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/customer_history.tsv\'}" TO EDGE customer_history VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/history_product.tsv\'}" TO EDGE history_product VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/demo_feature.tsv\'}" TO EDGE demo_feature VALUES ($"from", $"to", $"affinity") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/customer_feature.tsv\'}" TO EDGE customer_feature VALUES ($"from", $"to", $"affinity") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/product_feature.tsv\'}" TO EDGE product_feature VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/Rec2HyperMarketing/product_context.tsv\'}" TO EDGE product_context VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
