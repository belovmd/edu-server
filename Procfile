release: python manage.py migrate
release: sudo apt-get fp-compiler
web: gunicorn edu_server.wsgi --log-file -
