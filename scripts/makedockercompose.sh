#!/bin/bash
. ./env_setup.sh

# Run from the Nimbus/ directory
# Starts the docker compose for PG and REDIS
docker compose up -d
