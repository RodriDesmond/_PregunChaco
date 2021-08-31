from .base import *
import django_heroku


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', "default_value")

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
LOGIN_REDIRECT_URL = '/'

# Activate Django-Heroku.
django_heroku.settings(locals())
