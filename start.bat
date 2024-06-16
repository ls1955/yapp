ECHO OFF

source ./.venv/bin/activate

set FLASK_APP=yapp
set FLASK_ENV=development

flask run --debug
