#!/bin/bash
set -e

chmod +x ./compose/django/wait-for-it.sh
./compose/django/wait-for-it.sh -t 300 postgres:5432
python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000

exec "$@"
