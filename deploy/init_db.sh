#!/bin/bash

USERNAME="root"
PASSWORD=$1

DBNAME="lottery"
 
create_db_sql="create database IF NOT EXISTS ${DBNAME}"
mysql -u${USERNAME} -p${PASSWORD} -e "${create_db_sql}"
