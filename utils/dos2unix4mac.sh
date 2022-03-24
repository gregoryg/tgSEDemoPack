#!/bin/bash

## remove windows crap for test files

sed -e 's/\r$//' $1 > $2.new
