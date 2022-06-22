#!/bin/bash
. ./env_setup.sh

echo "${DB_HOST}:${DB_PORT}:postgres:${DB_NAME}:${DB_PASSWORD}" >> ./.pgpass
export PGPASSFILE=./.pgpass

#docker exec -it nimbus_database createuser -d -P $DB_USER -U postgres -w
psql -h $DB_HOST -U postgres -p $DB_PORT postgres -w -c "CREATE USER $DB_USER WITH CREATEDB"
psql -h $DB_HOST -U postgres -p $DB_PORT postgres -w -c "ALTER USER $DB_USER WITH PASSWORD '${DB_PASSWORD}'"
psql -h $DB_HOST -U $DB_NAME -p $DB_PORT -w postgres -c "CREATE DATABASE $DB_NAME"