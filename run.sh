#!/bin/bash

export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=./app.py
pipenv run flask run -p 5004