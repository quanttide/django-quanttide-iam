# drf-remote-auth 

Remote authorization for cloud-native microservices 
with Django REST Framework and without Django default auth,
developed by [QuantTide](github.com/quanttide).

## Motivation

The default Django apps, including `auth`, `admin`、`message`、`session`, 
should be removed to make cloud-native microservices **stateless**. 

After removing them, `RemoteUserAuthentication` class from Django REST Framework cannot be used,
since it requires `RemoteUserBackend` from default `auth`.

This package aims to extend the `TokenAuthentication` with remote authentication protocols, 
so that it can provide resource servers with authorization by remote authorization server.

Besides, this package also aims to provide some methods to adapt service mesh framework like `PolarisMesh`.

## Installation 

Install with `pip`.

```shell
pip install drf-remote-auth
```

Add `drf_remote_auth` to your `INSTALLED_APPS` in Django `settings.py`. 

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
    'drf_remote_auth',
    ...
]

AUTH_USER_MODEL = 'drf_remote_auth.AuthUser'
```

## Usage 

### Resource Server

### Authorization Server 

## License 

This package uses [BSD-3 License](LICENSE)

## Changelog 

[CHANGELOG](CHANGELOG.md)