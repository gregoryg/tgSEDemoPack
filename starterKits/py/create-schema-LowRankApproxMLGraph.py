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
DROP GRAPH LowRankApproxMLGraph

CREATE GRAPH LowRankApproxMLGraph()
USE GRAPH LowRankApproxMLGraph

CREATE SCHEMA_CHANGE JOB LowRankApproxMLGraph_change_job FOR GRAPH LowRankApproxMLGraph {

ADD VERTEX MATRIX_ROW(PRIMARY_ID row_index STRING, u LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX MATRIX_COLUMN(PRIMARY_ID column_index STRING, v LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE MATRIX_ELEMENT(FROM MATRIX_ROW, TO MATRIX_COLUMN, element_value DOUBLE);
}

RUN SCHEMA_CHANGE JOB LowRankApproxMLGraph_change_job
DROP JOB LowRankApproxMLGraph_change_job
''', options=[])
