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
DROP GRAPH ShortestPathAlgorithmsGraph

CREATE GRAPH ShortestPathAlgorithmsGraph()
USE GRAPH ShortestPathAlgorithmsGraph

CREATE SCHEMA_CHANGE JOB ShortestPathAlgorithmsGraph_change_job FOR GRAPH ShortestPathAlgorithmsGraph {

ADD VERTEX Airport(PRIMARY_ID id STRING, name STRING, city STRING, country STRING, IATA STRING, latitude DOUBLE, longitude DOUBLE) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE flight_route(FROM Airport, TO Airport, miles INT);
}

RUN SCHEMA_CHANGE JOB ShortestPathAlgorithmsGraph_change_job
DROP JOB ShortestPathAlgorithmsGraph_change_job
''', options=[])
