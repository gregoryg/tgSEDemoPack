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
## Tigergraph Key
print(conn.gsql('''

CREATE DATA_SOURCE S3 tg_s3_data_source = "{'file.reader.settings.fs.s3a.access.key':'AKIA45R*********','file.reader.settings.fs.s3a.secret.key':'jeO8GXIVCpjDkYVccHfuLL**************'}"

''', options=[]))
