#!/bin/sh

echo "Waiting for PostgreSQL..."
sleep 8

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 --timeout 300 chatbot_project.wsgi:application
