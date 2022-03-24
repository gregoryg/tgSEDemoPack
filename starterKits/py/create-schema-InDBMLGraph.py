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
DROP GRAPH InDBMLGraph

CREATE GRAPH InDBMLGraph()
USE GRAPH InDBMLGraph

CREATE SCHEMA_CHANGE JOB InDBMLGraph_change_job FOR GRAPH InDBMLGraph {

ADD VERTEX USER(PRIMARY_ID user_id STRING, theta LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX MOVIE(PRIMARY_ID movie_id STRING, name STRING, avg_rating DOUBLE, x LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE rate(FROM USER, TO MOVIE, rating DOUBLE, label BOOL DEFAULT "TRUE");
}

RUN SCHEMA_CHANGE JOB InDBMLGraph_change_job
DROP JOB InDBMLGraph_change_job
''', options=[])
