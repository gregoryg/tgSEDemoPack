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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH FinServPaymentFraudGraph

USE GRAPH FinServPaymentFraudGraph

BEGIN
CREATE LOADING JOB FinServPaymentFraudGraph_load_job FOR GRAPH FinServPaymentFraudGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/email.tsv\'}" TO VERTEX email VALUES ($"primary_id", $"address") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/bank.tsv\'}" TO VERTEX bank VALUES ($"primary_id", $"name", $"ABA_routing_number", $"swift_code") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/device.tsv\'}" TO VERTEX device VALUES ($"primary_id", $"manufacturer", $"model", $"IMEI", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/payment.tsv\'}" TO VERTEX payment VALUES ($"primary_id", $"amount", $"transaction_date", $"transactionEpoch", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/phone_number.tsv\'}" TO VERTEX phone_number VALUES ($"primary_id", $"number") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/merchant_account.tsv\'}" TO VERTEX merchant_account VALUES ($"primary_id", $"create_date", $"createEpoch", $"phone_number", $"email") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/user_account.tsv\'}" TO VERTEX user_account VALUES ($"primary_id", $"created_date", $"createEpoch", $"trust_score") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/user.tsv\'}" TO VERTEX user VALUES ($"primary_id", $"id", $"created_date", $"mobile", $"trust_score", $"createEpoch") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/used_with.tsv\'}" TO EDGE used_with VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/used_for.tsv\'}" TO EDGE used_for VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/receives_pmnt.tsv\'}" TO EDGE receives_pmnt VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/has_num.tsv\'}" TO EDGE has_num VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/has_email.tsv\'}" TO EDGE has_email VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/sends.tsv\'}" TO EDGE sends VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/receives.tsv\'}" TO EDGE receives VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/user_account_bank.tsv\'}" TO EDGE user_account_bank VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/associated_with.tsv\'}" TO EDGE associated_with VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/sends_pmnt.tsv\'}" TO EDGE sends_pmnt VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/merchant_account_device.tsv\'}" TO EDGE merchant_account_device VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/merchant_account_bank.tsv\'}" TO EDGE merchant_account_bank VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/authenticated_by_num.tsv\'}" TO EDGE authenticated_by_num VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/authenticated_by_email.tsv\'}" TO EDGE authenticated_by_email VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/FinServPaymentFraud/sets_up.tsv\'}" TO EDGE sets_up VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
