from .base import *
import os
import json

DEBUG = True

TEMPLATE_DEBUG = True
with open(os.path.join(BASE_DIR, 'secret_local.json'), 'rt') as secret:
    SECRET = json.loads(secret.read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'site_asylum',
        'USER': 'site_asylum',
        'PASSWORD': '',
        'HOST': '',
    }
}

SECRET_KEY = SECRET['SECRET_KEY']
IMPORT_DELIRIUM = True
