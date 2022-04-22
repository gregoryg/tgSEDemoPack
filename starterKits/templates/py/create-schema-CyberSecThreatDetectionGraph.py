#!/usr/bin/env python

# # 1 - TigerGraph Schema Refresh Job
# 
# These scripts are used to automatically refresh the a TigerGraph instance on TGCloud (or EC2)

# FETCH PACKAGES
import sys
import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "http://localhost"
username = "tigergraph_user"
password = "tigergraph_pw"  

## create connection
conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH CyberSecThreatDetectionGraph

CREATE GRAPH CyberSecThreatDetectionGraph()
USE GRAPH CyberSecThreatDetectionGraph

CREATE SCHEMA_CHANGE JOB CyberSecThreatDetectionGraph_change_job FOR GRAPH CyberSecThreatDetectionGraph {

ADD VERTEX IP(PRIMARY_ID id STRING, banned BOOL) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Servers(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX UserID(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Resource(PRIMARY_ID id STRING, Resource_Type STRING, URL STRING, Authentication_Required BOOL, Firewall_Required BOOL) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Event(PRIMARY_ID id STRING, Start_Date DATETIME, Event_Type STRING, End_Date DATETIME, Return_Code UINT, Endpoint STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Device(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Alert(PRIMARY_ID id STRING, Alert_Date DATETIME) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Alert_Type(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Service(PRIMARY_ID id STRING, Service_Name STRING, Service_Type STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD UNDIRECTED EDGE Has_IP(FROM IP, TO Event);
ADD UNDIRECTED EDGE User_Event(FROM UserID, TO Event);
ADD UNDIRECTED EDGE From_Device(FROM Event, TO Device);
ADD UNDIRECTED EDGE Server_Alert(FROM Servers, TO Alert);
ADD UNDIRECTED EDGE Alert_Has_Type(FROM Alert, TO Alert_Type);
ADD UNDIRECTED EDGE From_Server(FROM Servers, TO Event);
ADD UNDIRECTED EDGE Output_To_Resource(FROM Resource, TO Event);
ADD UNDIRECTED EDGE To_Server(FROM Event, TO Servers);
ADD UNDIRECTED EDGE Read_From_Resource(FROM Event, TO Resource);
ADD UNDIRECTED EDGE From_Service(FROM Event, TO Service);
ADD UNDIRECTED EDGE To_Service(FROM Event, TO Service);
ADD UNDIRECTED EDGE Service_Alert(FROM Service, TO Alert);
}

RUN SCHEMA_CHANGE JOB CyberSecThreatDetectionGraph_change_job
DROP JOB CyberSecThreatDetectionGraph_change_job
''', options=[])
