# The DB_HOST of localhost is used for development locally where the PG server is run inside of a docker container.
# Note that lots of projects can be run off the same Docker Postgres images.
export DB_HOST="localhost"
# The default PG port is 5432 and the Docker Compose application stack exposes 54320 as the external port for the 
# container which maps to 5432 inside the container.  This allows the docker image to be run on an environment
# where PostgreSQL might already be running.
export DB_PORT="54321"
# These are defaults and will be overridden by environment variables in env_application.sh
export DB_NAME="appname"
export DB_USER="appname"
# This can be used by all developers as a default passowrd or it can be overridden in env_application.sh
export DB_ADMINPASSWORD="kkeeu2i3u1234!2SaA"
export DB_PASSWORD="kkeeu2i3u1234!2SaA"

# REDIS is run inside of a docker container locally
export REDIS_HOST="localhost"
# The username/password used to connecto the RDSI service
export REDIS_USERNAME="appname"
export REDIS_PASSWORD="kkeeu2i3u1234!2SaA"
# The internal port number for REDIS in the docker image is 6379 but is exposed externally as 63790.  This allows
# docker to be used when there's a number of 
export REDIS_PORT="63791"

# This is the name of the application we're building.  It'll be the related to the project name.  This should
# be overridden in env_applicaiton.sh
export APPNAME="storeapp"

# Application-specific overrides or environments are loaded from here
. ./env_application.sh

# This is a default location where the repository might have been cloned to.  This is used to set the
# base directory where many files and scripts will be referenced from.
export ROOT=$HOME/git/$APPNAME/backend
