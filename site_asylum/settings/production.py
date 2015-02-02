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
        'PASSWORD': SECRET['DB_PW']
    }
}
