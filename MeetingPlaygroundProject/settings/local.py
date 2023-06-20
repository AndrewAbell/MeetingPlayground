from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MeetingPlaygroundDB',
        'USER': 'Andrew',
        'HOST': 'localhost',
        'PASSWORD': "ArsenA@33!",
        'PORT': '5432'
        }
}

INSTALLED_APPS += ['debug_toolbar', ]