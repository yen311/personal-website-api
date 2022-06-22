#!/bin/bash 

. ./env_setup.sh
venvname="${APPNAME}.nimbus39"

cd $ROOT/.vscode

inputfile=./launch.json.template

echo "Updating Environment in launch.json"
cat $inputfile | 
	sed -e s/\$DB_NAME/${DB_NAME}/ |
	sed -e s/\$DB_USER/${DB_USER}/ |
	sed -e s/\$DB_PASSWORD/${DB_PASSWORD}/ |
	sed -e s/\$REDIS_PASSWORD/${REDIS_PASSWORD}/ |
	sed -e s/\$APPNAME/${APPNAME}/ |
	sed -e s/\$REDIS_USER/${REDIS_USER}/ > launch.json

echo "Updating paths in settings.json"
cat ./settings.json.template | sed -e s/nimbus39/${APPNAME}.nimbus39/ > ./settings.json
