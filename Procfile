release: python manage.py migrate
web: gunicorn django_schedule.wsgi --log-file -
web: python manage.py runserver