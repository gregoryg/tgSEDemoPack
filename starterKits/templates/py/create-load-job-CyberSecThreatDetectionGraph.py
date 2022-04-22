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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH CyberSecThreatDetectionGraph

USE GRAPH CyberSecThreatDetectionGraph

BEGIN
CREATE LOADING JOB CyberSecThreatDetectionGraph_load_job FOR GRAPH CyberSecThreatDetectionGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/IP.tsv\'}" TO VERTEX IP VALUES ($"primary_id", $"banned") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Servers.tsv\'}" TO VERTEX Servers VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/UserID.tsv\'}" TO VERTEX UserID VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Resource.tsv\'}" TO VERTEX Resource VALUES ($"primary_id", $"Resource_Type", $"URL", $"Authentication_Required", $"Firewall_Required") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Event.tsv\'}" TO VERTEX Event VALUES ($"primary_id", $"Start_Date", $"Event_Type", $"End_Date", $"Return_Code", $"Endpoint") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Device.tsv\'}" TO VERTEX Device VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Alert.tsv\'}" TO VERTEX Alert VALUES ($"primary_id", $"Alert_Date") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Alert_Type.tsv\'}" TO VERTEX Alert_Type VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Service.tsv\'}" TO VERTEX Service VALUES ($"primary_id", $"Service_Name", $"Service_Type") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Has_IP.tsv\'}" TO EDGE Has_IP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/User_Event.tsv\'}" TO EDGE User_Event VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/From_Device.tsv\'}" TO EDGE From_Device VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Server_Alert.tsv\'}" TO EDGE Server_Alert VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Alert_Has_Type.tsv\'}" TO EDGE Alert_Has_Type VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/From_Server.tsv\'}" TO EDGE From_Server VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Output_To_Resource.tsv\'}" TO EDGE Output_To_Resource VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/To_Server.tsv\'}" TO EDGE To_Server VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Read_From_Resource.tsv\'}" TO EDGE Read_From_Resource VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/From_Service.tsv\'}" TO EDGE From_Service VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/To_Service.tsv\'}" TO EDGE To_Service VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/CyberSecThreatDetection/Service_Alert.tsv\'}" TO EDGE Service_Alert VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
