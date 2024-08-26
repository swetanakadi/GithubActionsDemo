#!/bin/bash

python3 manage.py makemigrations --settings=setup.settings.dev
python3 manage.py migrate --settings=setup.settings.dev
python3 manage.py runserver --settings=setup.settings.dev 0.0.0.0:8000