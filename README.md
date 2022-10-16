# 量潮IdAM云Django服务端SDK

量潮云身份和访问管理平台Django服务端SDK

## Installation 

Install the package with `pip`.

```shell
pip install django-qtcloud-idam
```

Add `django_qtcloud_idam` to your `INSTALLED_APPS` in Django `settings.py`. 

```python
# settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...,
    'django_qtcloud_idam',
    ...
]
```

## Usage 

修改Auth用户模型

```python
# settings.py

AUTH_USER_MODEL = 'django_qtcloud_idam.AuthUser'
```

修改REST Framework的默认Auth和Permission类

```python
# settings.py

REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_qtcloud_idam.authentication.IDTokenAuthentication',
    ],
    ...,
    'DEFAULT_PERMISSION_CLASSES': [
        'django_qtcloud_idam.permissions.IsAdminUserOrIsAuthenticatedReadOnly',
    ],
}
```

## License 

This package uses [BSD-3 License](LICENSE)

## Changelog 

[CHANGELOG](CHANGELOG.md)