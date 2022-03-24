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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH HealthCareFAERSGraph

USE GRAPH HealthCareFAERSGraph

BEGIN
CREATE LOADING JOB HealthCareFAERSGraph_load_job FOR GRAPH HealthCareFAERSGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/ReportedCase.tsv\'}" TO VERTEX ReportedCase VALUES ($"primary_id", $"caseid", $"caseversion", $"fda_dt", $"mfr_sndr", $"reporter_country", $"occr_country") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/PharmaCompany.tsv\'}" TO VERTEX PharmaCompany VALUES ($"primary_id", $"mfr_sndr") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/DrugSequence.tsv\'}" TO VERTEX DrugSequence VALUES ($"primary_id", $"seqid", $"role_cod", $"drugname") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Drug.tsv\'}" TO VERTEX Drug VALUES ($"primary_id", $"drugname", $"prod_ai") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Reaction.tsv\'}" TO VERTEX Reaction VALUES ($"primary_id", $"pt", $"drug_rec_act") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Outcome.tsv\'}" TO VERTEX Outcome VALUES ($"primary_id", $"outc_code") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/ReportSource.tsv\'}" TO VERTEX ReportSource VALUES ($"primary_id", $"rpsr_code") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Patient.tsv\'}" TO VERTEX Patient VALUES ($"primary_id", $"age", $"age_code", $"age_grp", $"sex", $"weight", $"wt_code", $"occp_cod") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Therapy.tsv\'}" TO VERTEX Therapy VALUES ($"primary_id", $"dsg_drug_seq", $"start_date", $"end_date") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/Indication.tsv\'}" TO VERTEX Indication VALUES ($"primary_id", $"indi_drug_seq", $"indi_pt") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasOutcomes.tsv\'}" TO EDGE hasOutcomes VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasReactions.tsv\'}" TO EDGE hasReactions VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasReportSources.tsv\'}" TO EDGE hasReportSources VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasPatient.tsv\'}" TO EDGE hasPatient VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasSequences.tsv\'}" TO EDGE hasSequences VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasDrugs.tsv\'}" TO EDGE hasDrugs VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/isUsedInTherapy.tsv\'}" TO EDGE isUsedInTherapy VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/hasIndications.tsv\'}" TO EDGE hasIndications VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/relatedTo.tsv\'}" TO EDGE relatedTo VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/HealthCareFAERS/similarCaseTo.tsv\'}" TO EDGE similarCaseTo VALUES ($"from", $"to", $"wt") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
