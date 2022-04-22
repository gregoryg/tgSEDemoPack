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
   
GRANT DATA_SOURCE tg_s3_data_source TO GRAPH COVID19Graph

USE GRAPH COVID19Graph

BEGIN
CREATE LOADING JOB COVID19Graph_load_job FOR GRAPH COVID19Graph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/City.tsv\'}" TO VERTEX City VALUES ($"primary_id", $"city", $"elementary_school_count", $"kindergarten_count", $"university_count", $"academy_ratio", $"elderly_population_ratio", $"elderly_alone_ratio", $"nursing_home_count") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Province.tsv\'}" TO VERTEX Province VALUES ($"primary_id", $"province", $"population", $"area") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Country.tsv\'}" TO VERTEX Country VALUES ($"primary_id", $"country") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/SearchStat.tsv\'}" TO VERTEX SearchStat VALUES ($"primary_id", $"cold", $"flu", $"pneumonia", $"coronavirus") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/WeatherStat.tsv\'}" TO VERTEX WeatherStat VALUES ($"primary_id", $"code", $"avg_temp", $"min_temp", $"max_temp", $"precipitation", $"max_wind_speed", $"most_wind_direction", $"avg_relative_humidity") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/InfectionCase.tsv\'}" TO VERTEX InfectionCase VALUES ($"primary_id", $"infection_case", $"confirmed", $"ic_group") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Year_.tsv\'}" TO VERTEX Year_ VALUES ($"primary_id", $"year_") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Month_.tsv\'}" TO VERTEX Month_ VALUES ($"primary_id", $"month_") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Day_.tsv\'}" TO VERTEX Day_ VALUES ($"primary_id", $"day_") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/TravelEvent.tsv\'}" TO VERTEX TravelEvent VALUES ($"primary_id", $"latitude", $"longitude", $"visited_date", $"travel_type") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/Patient.tsv\'}" TO VERTEX Patient VALUES ($"primary_id", $"global_num", $"birth_year", $"infection_case", $"contact_number", $"symptom_onset_date", $"confirmed_date", $"released_date", $"deceased_date", $"state", $"disease", $"sex") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/PROVINCE_IN_COUNTRY.tsv\'}" TO EDGE PROVINCE_IN_COUNTRY VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/CITY_IN_PROVINCE.tsv\'}" TO EDGE CITY_IN_PROVINCE VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/WEATHER_CONDITION.tsv\'}" TO EDGE WEATHER_CONDITION VALUES ($"from", $"to", $"wc_date") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/CASE_IN_CITY.tsv\'}" TO EDGE CASE_IN_CITY VALUES ($"from", $"to", $"latitude", $"longitude") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/CASE_IN_PROVINCE.tsv\'}" TO EDGE CASE_IN_PROVINCE VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/YEAR_MONTH.tsv\'}" TO EDGE YEAR_MONTH VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/MONTH_DAY.tsv\'}" TO EDGE MONTH_DAY VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/SEARCH_STAMP.tsv\'}" TO EDGE SEARCH_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/WEATHER_STAMP.tsv\'}" TO EDGE WEATHER_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/TRAVEL_EVENT_IN.tsv\'}" TO EDGE TRAVEL_EVENT_IN VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/TRAVEL_STAMP.tsv\'}" TO EDGE TRAVEL_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/INFECTED_BY.tsv\'}" TO EDGE INFECTED_BY VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/BELONGS_TO_CASE.tsv\'}" TO EDGE BELONGS_TO_CASE VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/CONFIRM_STAMP.tsv\'}" TO EDGE CONFIRM_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/SYMPTOM_STAMP.tsv\'}" TO EDGE SYMPTOM_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/RELEASED_STAMP.tsv\'}" TO EDGE RELEASED_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/BIRTH_STAMP.tsv\'}" TO EDGE BIRTH_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/DECEASE_STAMP.tsv\'}" TO EDGE DECEASE_STAMP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/PATIENT_FROM_CITY.tsv\'}" TO EDGE PATIENT_FROM_CITY VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/PATIENT_FROM_PROVINCE.tsv\'}" TO EDGE PATIENT_FROM_PROVINCE VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/PATIENT_FROM_COUNTRY.tsv\'}" TO EDGE PATIENT_FROM_COUNTRY VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/PATIENT_TRAVELED.tsv\'}" TO EDGE PATIENT_TRAVELED VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}
''', options=[]))
