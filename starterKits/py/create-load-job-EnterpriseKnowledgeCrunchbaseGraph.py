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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH EnterpriseKnowledgeCrunchbaseGraph

USE GRAPH EnterpriseKnowledgeCrunchbaseGraph

BEGIN
CREATE LOADING JOB EnterpriseKnowledgeCrunchbaseGraph_load_job FOR GRAPH EnterpriseKnowledgeCrunchbaseGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company.tsv\'}" TO VERTEX company VALUES ($"primary_id", $"name", $"normalized_name", $"permalink", $"category_code", $"status", $"founded_at", $"closed_at", $"domain", $"homepage_url", $"twitter_username", $"logo_url", $"short_description", $"description", $"overview", $"tag_list", $"country", $"state", $"city", $"region", $"first_investment_at", $"last_investment_at", $"first_funding_at", $"last_funding_at", $"funding_rounds", $"funding_total_usd", $"first_milestone_at", $"last_milestone_at", $"relationships", $"created_by", $"created_at", $"update_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/person.tsv\'}" TO VERTEX person VALUES ($"primary_id", $"fullname", $"normalized_name", $"firstname", $"lastname", $"birthplace", $"affiliation_name", $"permalink", $"status", $"domain", $"homepage_url", $"twitter_username", $"logo_url", $"overview", $"tag_list", $"first_milestone_at", $"last_milestone_at", $"created_by", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/financialORG.tsv\'}" TO VERTEX financialORG VALUES ($"primary_id", $"name", $"normalized_name", $"permalink", $"category_code", $"status", $"founded_at", $"closed_at", $"domain", $"homepage_url", $"twitter_username", $"logo_url", $"short_description", $"description", $"overview", $"tag_list", $"country_code", $"state_code", $"city", $"region", $"first_investment_at", $"last_investment_at", $"first_funding_at", $"last_funding_at", $"funding_rounds", $"funding_total_usd", $"first_milestone_at", $"last_milestone_at", $"relationships", $"created_by", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/product.tsv\'}" TO VERTEX product VALUES ($"primary_id", $"name", $"normalized_name", $"permalink", $"status", $"founded_at", $"closed_at", $"domain", $"homepage_url", $"twitter_username", $"logo_url", $"overview", $"tag_list", $"created_at", $"updates_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/university.tsv\'}" TO VERTEX university VALUES ($"primary_id", $"name") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/IPO.tsv\'}" TO VERTEX IPO VALUES ($"primary_id", $"valuation_amount", $"valuation_currency_code", $"raised_amount", $"raised_currency_code", $"public_at", $"stock_symbol", $"source_url", $"source_description", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/funding_rounds.tsv\'}" TO VERTEX funding_rounds VALUES ($"primary_id", $"funded_at", $"funding_round_type", $"funding_round_code", $"raised_amount_usd", $"raised_amount", $"raised_currency_code", $"pre_money_valuation_usd", $"pre_money_valuation", $"pre_money_currency_code", $"post_money_valuation_usd", $"post_money_valuation", $"post_money_currency_code", $"is_first_round", $"is_last_round", $"source_url", $"source_description", $"created_by", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/office.tsv\'}" TO VERTEX office VALUES ($"primary_id", $"description", $"region", $"address1", $"address2", $"city", $"zip_code", $"state_code", $"country_code", $"latitude", $"longitude") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/funds.tsv\'}" TO VERTEX funds VALUES ($"primary_id", $"name", $"funded_at", $"raised_amount", $"raised_currency_code", $"source_url", $"source_description", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/milestone.tsv\'}" TO VERTEX milestone VALUES ($"primary_id", $"milestone_at", $"milestone_code", $"description", $"source_url", $"source_description", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/work_for_company.tsv\'}" TO EDGE work_for_company VALUES ($"from", $"to", $"start_at", $"end_at", $"is_past", $"sequence", $"title", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/hasDegree.tsv\'}" TO EDGE hasDegree VALUES ($"from", $"to", $"degree_type", $"subject", $"graduated_at", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company_ipo.tsv\'}" TO EDGE company_ipo VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company_funding_rounds.tsv\'}" TO EDGE company_funding_rounds VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/financial_funds.tsv\'}" TO EDGE financial_funds VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company_office.tsv\'}" TO EDGE company_office VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/financial_office.tsv\'}" TO EDGE financial_office VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company_product.tsv\'}" TO EDGE company_product VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/person_milestone.tsv\'}" TO EDGE person_milestone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/company_milestone.tsv\'}" TO EDGE company_milestone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/product_milestone.tsv\'}" TO EDGE product_milestone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/financial_milestone.tsv\'}" TO EDGE financial_milestone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/investment_from_person.tsv\'}" TO EDGE investment_from_person VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/investment_from_company.tsv\'}" TO EDGE investment_from_company VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/investment_from_financialORG.tsv\'}" TO EDGE investment_from_financialORG VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/work_for_fOrg.tsv\'}" TO EDGE work_for_fOrg VALUES ($"from", $"to", $"start_at", $"end_at", $"is_past", $"sequence", $"title", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/invested_by_person.tsv\'}" TO EDGE invested_by_person VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/invested_by_financialORG.tsv\'}" TO EDGE invested_by_financialORG VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/acquire.tsv\'}" TO EDGE acquire VALUES ($"from", $"to", $"term_code", $"price_amout", $"price_currency_code", $"acquired_at", $"source_url", $"source_description", $"created_at", $"updated_at") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/EnterpriseKnowledgeCrunchbase/invest.tsv\'}" TO EDGE invest VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
