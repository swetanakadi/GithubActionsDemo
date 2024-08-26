#!/bin/bash

python3 manage.py makemigrations --settings=setup.settings.prod
python3 manage.py migrate --settings=setup.settings.prod
python3 manage.py runserver --settings=setup.settings.prod 0.0.0.0:8000