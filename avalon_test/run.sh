#! /bin/bash
.env/bin/pip install --upgrade -r requirements.txt
.env/bin/python manage.py makemigrations
.env/bin/python manage.py migrate
.env/bin/python manage.py runserver 8000
exit 0
 
