release: python manage.py migrate
release: apt-get fp-compiler
web: gunicorn edu_server.wsgi --log-file -
