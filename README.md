# 量潮IdAM Django SDK

## Installation 

Install the package with `pip`.

```shell
pip install django-quanttide-idam
```

Add `django_quanttide_idam` to your `INSTALLED_APPS` in Django `settings.py`. 

```python
# settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...,
    'django_quanttide_idam',
    ...
]
```

## Usage 

修改Auth用户模型

```python
# settings.py

AUTH_USER_MODEL = 'django_quanttide_idam.AuthUser'
```

修改REST Framework的默认Auth和Permission类

```python
# settings.py

REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_quanttide_idam.authentication.IDTokenAuthentication',
    ],
    ...,
    'DEFAULT_PERMISSION_CLASSES': [
        'django_quanttide_idam.permissions.IsAdminUserOrIsAuthenticatedReadOnly',
    ],
}
```

## License 

This package uses [Apache 2.0 License](LICENSE)

## Changelog 

[CHANGELOG](CHANGELOG.md)