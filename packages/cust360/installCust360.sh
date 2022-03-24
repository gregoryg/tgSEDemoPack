#!/bin/bash

gsql packages/cust360/scripts/create_cust360_schema.gsql
gsql packages/cust360/scripts/customer360_load_er.gsql
gsql packages/cust360/scripts/customer360_load_camp.gsql
gsql packages/cust360/scripts/customer360_load_events.gsql
gsql packages/cust360/scripts/customer360_load_orders.gsql
gsql packages/cust360/scripts/customer360_load_ratings.gsql
