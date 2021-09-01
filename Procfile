release: python manage.py migrate --run-syncdb
web gunicorn PregunChaco.wsgi:application --log-file -