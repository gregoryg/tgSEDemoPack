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
DROP GRAPH ML_RTFraudGraph

CREATE GRAPH ML_RTFraudGraph()
USE GRAPH ML_RTFraudGraph

CREATE SCHEMA_CHANGE JOB ML_RTFraudGraph_change_job FOR GRAPH ML_RTFraudGraph {

ADD VERTEX phone(PRIMARY_ID phone_id STRING, flag UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE phone_phone(FROM phone, TO phone, num_of_call UINT, total_duration UINT, num_of_rejection UINT, start_time UINT, max_duration UINT) WITH REVERSE_EDGE="phone_phone_reversed";
}

RUN SCHEMA_CHANGE JOB ML_RTFraudGraph_change_job
DROP JOB ML_RTFraudGraph_change_job
''', options=[])
