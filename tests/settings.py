# -*- coding: utf-8 -*-

import os

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'drf_remote_auth',
    'tests',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": 'db.sqlite3',
    }
}
