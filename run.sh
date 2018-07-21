#!/bin/bash

export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=./app.py
pipenv run gunicorn -k eventlet --bind localhost:5004 app:app -w 1 --error-logfile "-" --access-logfile "-"