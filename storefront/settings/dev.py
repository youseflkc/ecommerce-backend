from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ubkpo&26gl%3fn_9a1#u^zhj7d8+g$1&y@6%6^kpn-x=$x26eo'


if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'storeadmin',
        'PASSWORD': 'password'
    }
}
