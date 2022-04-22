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
DROP GRAPH RecEngMovieGraph

CREATE GRAPH RecEngMovieGraph()
USE GRAPH RecEngMovieGraph

CREATE SCHEMA_CHANGE JOB RecEngMovieGraph_change_job FOR GRAPH RecEngMovieGraph {

ADD VERTEX person(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX movie(PRIMARY_ID id STRING, title STRING, genres STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE rate(FROM person, TO movie, rating DOUBLE, rated_at DATETIME) WITH REVERSE_EDGE="reverse_rate";
}

RUN SCHEMA_CHANGE JOB RecEngMovieGraph_change_job
DROP JOB RecEngMovieGraph_change_job
''', options=[])
