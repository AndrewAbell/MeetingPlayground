from .base import *
import os

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MeetingPlaygroundDB',
        'USER': os.getenv('USER'),
        'HOST': 'localhost',
        'PASSWORD': os.getenv('PASSWORD'),
        'PORT': '5432'
        }
}

INSTALLED_APPS += ['debug_toolbar', ]