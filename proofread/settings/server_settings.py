import os
import dj_database_url

# did you set your secret key yet?

# Try CloudMailIn for incoming mail
# https://addons.heroku.com/cloudmailin


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

#DATABASES = {
#   'default': {
#        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#        # The following settings are not used with sqlite3:
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#        'PORT': '',                      # Set to empty string for default.
#    }
#}

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

DEBUG = os.environ.get('DJANGO_DEBUG', "False").lower() == "true"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')