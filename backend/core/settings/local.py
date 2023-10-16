from .base import *
from environ import Env

env = Env()

Env.read_env()

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('HOST_DB'),
        'PORT': env('PORT_DB'),
        'USER': env('USER_DB'),
        'PASSWORD': env('PASSWORD_DB'),
        'NAME': env('NAME_DB')
    }
}


STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"

