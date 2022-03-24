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
DROP GRAPH NetworkITResourceOptimizationGraph

CREATE GRAPH NetworkITResourceOptimizationGraph()
USE GRAPH NetworkITResourceOptimizationGraph

CREATE SCHEMA_CHANGE JOB NetworkITResourceOptimizationGraph_change_job FOR GRAPH NetworkITResourceOptimizationGraph {

ADD VERTEX LUN(PRIMARY_ID did STRING, name STRING, total_capacity FLOAT, estimated_used FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Pool(PRIMARY_ID pid STRING, name STRING, raw_capacity FLOAT, used_capacity FLOAT, user_capacity FLOAT, subscribed_capacity FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Storage_Array(PRIMARY_ID aid STRING, name STRING, capacity FLOAT, allocated FLOAT, available FLOAT, raw_capacity FLOAT, raw_allocated FLOAT, raw_available FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Host_Server(PRIMARY_ID hid STRING, hid STRING, name STRING, status STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Application(PRIMARY_ID pid STRING, short_name STRING, tier UINT, weight INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Service(PRIMARY_ID sid STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Manager(PRIMARY_ID sid STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Switch(PRIMARY_ID fid STRING, swtich_name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Warning(PRIMARY_ID sid STRING, event_type INT, warn_date DATETIME) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX WanringType(PRIMARY_ID aid STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE Alert_App(FROM Warning, TO Application) WITH REVERSE_EDGE="App_Alert";
ADD DIRECTED EDGE AHA_Alert(FROM WanringType, TO Warning) WITH REVERSE_EDGE="Alert_AHA";
ADD DIRECTED EDGE Pool_Lun(FROM Pool, TO LUN, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE Array_Pool(FROM Storage_Array, TO Pool, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE LUN_Server(FROM LUN, TO Host_Server, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE Server_App(FROM Host_Server, TO Application, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE App_Service(FROM Application, TO Service, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE Service_Manager(FROM Service, TO Manager, goUpper BOOL DEFAULT "true");
ADD DIRECTED EDGE Pool_Array(FROM Pool, TO Storage_Array, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE LUN_Pool(FROM LUN, TO Pool, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE Server_LUN(FROM Host_Server, TO LUN, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE App_Server(FROM Application, TO Host_Server, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE Service_App(FROM Service, TO Application, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE Manager_Service(FROM Manager, TO Service, goLower BOOL DEFAULT "true");
ADD DIRECTED EDGE Switch_Host(FROM Switch, TO Host_Server) WITH REVERSE_EDGE="reverse_Switch_Host";
ADD DIRECTED EDGE Array_Switch(FROM Storage_Array, TO Switch) WITH REVERSE_EDGE="reverse_Array_Switch";
ADD DIRECTED EDGE AppCall(FROM Application, TO Application);
}

RUN SCHEMA_CHANGE JOB NetworkITResourceOptimizationGraph_change_job
DROP JOB NetworkITResourceOptimizationGraph_change_job
''', options=[])
