#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py collectstatic --noinput

python /app/manage.py migrate

exec /usr/local/bin/gunicorn main.wsgi --bind 0.0.0.0:8000 --chdir=/app