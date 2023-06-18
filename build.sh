#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing the latest version of poetry..."

pip install --upgrade pip

pip install poetry==1.2.0

rm poetry.lock

poetry lock

python -m poetry install
python manage.py collectstatic --no-input
python manage.py makemigrations drfauth
python manage.py migrate drfauth
python manage.py makemigrations
python manage.py migrate
