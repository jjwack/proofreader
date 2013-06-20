import os

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

DEBUG = os.environ.get('DJANGO_DEBUG', True)