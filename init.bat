























ECHO OFF

python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt

set FLASK_APP=yapp
set FLASK_ENV=development

flask init-db
flask init-keys

flask run --debug
