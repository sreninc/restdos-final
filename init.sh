#!/bin/sh
# Script to create dev env. Run:
# chmod +x init.sh
# ./init.sh
pip3 install -r requirements.txt
python3 manage.py tailwind install
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username restdos --email restdos@restdos.com
python3 manage.py runserver

