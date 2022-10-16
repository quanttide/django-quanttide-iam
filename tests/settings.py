# -*- coding: utf-8 -*-

import os

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_qtcloud_idam',
    'tests',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'django_qtcloud_idam.AuthUser'
