web: gunicorn send_mail.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
