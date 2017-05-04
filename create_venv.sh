#!/usr/bin/env bash

. project.properties

virtualenv --no-site-packages --distribute $VENV_NAME
source $VENV_NAME/bin/activate
pip install -r requirements.txt
