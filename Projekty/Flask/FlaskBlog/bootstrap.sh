#!/bin/bash
export FLASK_APP=flaskr
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0