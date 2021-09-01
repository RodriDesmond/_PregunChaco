from .base import *
import django_heroku

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', "default_value")

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['pregunchaco.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfebk58a6ks6qk',
        'USER': 'pfkuelosulmrmv',
        'PASSWORD':'37b3d75f30f45963265a42f0ffb188020fd50522ec6f290792c33f7d93fd25e5',
        'HOST':'ec2-44-195-247-84.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
LOGIN_REDIRECT_URL = '/'

# Activate Django-Heroku.
django_heroku.settings(locals())
