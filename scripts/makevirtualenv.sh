#!/bin/bash

. ./env_setup.sh
venvname="${APPNAME}.nimbus39"

cd ~
virtualenv $venvname -p `which python3.9`
cd ..
. ~/$venvname/bin/activate
cd $ROOT
pip install -r ./requirements.txt


cd $ROOT/scripts
./makevscode.sh

