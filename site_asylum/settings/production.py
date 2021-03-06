# -*- coding:utf-8 -*-
from .base import *
import os
import json

DEBUG = False
TEMPLATE_DEBUG = False

with open(os.path.join(BASE_DIR, 'secret_production.json'), 'rt') as secret:
    SECRET = json.loads(secret.read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRET['DB_NAME'],
        'USER': SECRET['DB_USER'],
        'PASSWORD': SECRET['DB_PW'],
        'HOST': '127.0.0.1',
    }
}

SECRET_KEY = SECRET['SECRET_KEY']
VIRTUAL_ENV = os.environ['VIRTUAL_ENV']
MEDIA_ROOT = os.path.join(VIRTUAL_ENV, 'www/media/')
STATIC_ROOT = os.path.join(VIRTUAL_ENV, 'www/static/')
