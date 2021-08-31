from .base import *

SECRET_KEY = 'django-insecure-+g#!ki4#anzhib_$-d)-uzlk4yb%74z+s1dd3i^g3fsd#jg8$c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR,"static")
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
LOGIN_REDIRECT_URL = '/'
