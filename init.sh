#!/usr/bin/bash

# This script setup and run app in debug mode

python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=yapp
export FLAKS_ENV=development

flask init-db
flask init-keys

flask run --debug
