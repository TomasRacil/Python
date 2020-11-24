#!/bin/bash
export FLASK_APP=hello.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 --port=5100