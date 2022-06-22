## 1. Setup the environment appropriately

The first thing is to tell the environment what the base directory is

```
# export ROOT=~/git/storeapp
```

The environment variable source file ~/scripts/env*setup.sh contains default values and at the end it
sources \_env_application.sh* which overrides specific passwords and other names.

## 2. Building a Virtual Environment

Run a script to build the virtual environment. You should create a file $NIMBUSBASE/application.requirements.txt for app-specific packages. _Only run this once per application you work on._

```
# cd $ROOT/scripts
# ./makevirtualenv.sh
```

Note that this will update $NIMBUSBASE/.vscode/settings.json and $NIMBUSBASE/.vscode/launch.json. This is done by the script $NIMBUSBASE/scripts/makevscode.sh which is called by makevirtualenv.sh Once you have run this you can activate the
virtual environment with the following:

```
# cd $ROOT/scripts
# . ./activatevenv.sh
```

## 3. Build the Docker Containers

This constructs a docker compose environment that stands up postgres and redis. _ Only run this for your first project on the development workstation._
As a pre-requisite for this you'll need to install Docker Desktop https://www.docker.com/products/docker-desktop

```
# cd $ROOT/scripts
# . ./env_setup.sh
# ./makedockercompose.sh
```

## 4. Setup the Database Base Environment

This will configure the credentials using the DB*ADMINPASSWORD environment variable. \_Do this once when you setup the application*.

```
# cd $ROOT/scripts
# . ./env_setup.sh
# ./makebasedbenvironment.sh
```

Next you will need to create the application-level user included in $DB_USER and $DB_PASSWORD. The database commands for this are executed as the
"postgres" user using $DB_ADMINPASSWORD as the password (created as part of makbasedbenvironment.sh). In each case a file $NIMBUSBASE/scripts/.pgpass is
created which contains credentials.

```
# cd $ROOT/scripts
# . ./env_setup.sh
# ./makedbenvironment.sh
```

## 5. Comment out some stuff real quick

We need these lines in but they cannot exist until we make the application

```
# COMMENT out the following line in nimbus/settings.py
# os.environ.get('APPNAME')
# this is line 55 at time of writing

# You may also need to COMMENT out the following line in nimbus/urls.py
# path("", include(f"{os.environ.get('APPNAME')}.urls")),
# this is line 27 at time of writing

## 6. Make a new application in Django ##
The environment variable $APPNAME should be set in env_application.sh.  This environment variable is used in nimbus/settings.py to know what application to load
but for the application to be valid we need to make it.

```

# cd $NIMBUSBASE/scripts/

# . ./env_setup.sh

# cd $NIMBUSBASE

# ./manage.py startapp $APPNAME

# ./manage.py makemigrations

# ./manage.py migrate

```

You should also remember to setup a superuser for your environment:

```

# cd $NIMBUSBASE

# ./manage.py createsuperuser

```

## 7. Undo step 5
```
