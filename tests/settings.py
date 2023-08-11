"""
Django settings for testcases.
"""

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_quanttide_idam',
    'tests',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'django_quanttide_idam.User'
