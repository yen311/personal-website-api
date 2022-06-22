#!/bin/bash
. ./env_setup.sh

echo "${DB_HOST}:${DB_PORT}:postgres:postgres:${DB_ADMINPASSWORD}" > ./.pgpass
chmod 600 ./.pgpass
export PGPASSFILE=./.pgpass

brew install libpq
brew link --force libpq
