# drf-remote-auth 

Remote authorization for cloud-native microservices 
with Django REST Framework and without Django default auth,
developed by [QuantTide](https://github.com/quanttide).

## Motivation

由于OAuth2和OpenID Connect协议是为第三方登录设计，因此要求鉴权服务发送登录页面到客户端、客户端调用浏览器渲染。
这样会保证账号密码不会泄露给第三方，并且方便单点登录；但对于第一方应用来说，这样会损失用户体验。

本库假设鉴权客户端和鉴权服务端在本库的基础上由同一个开发主体负责。
实现一套代替的第一方应用的登录注册视图，使用OAuth2和OpenID Connect的AccessToken和IDToken机制实现鉴权和认证机制。
鉴权客户端基于Token鉴权的方式实现，拓展Django REST Framework的Authentication Class实现；鉴权服务端使用类似于
OAuth2协议的Resource Owner Password Grant实现，在此基础上增加IDToken，此实践尽可以在第一方应用中使用。
This practice is inspired by [Firebase](https://firebase.google.com).

The default Django apps, including `auth`, `admin`、`message`、`session`, 
should be removed to make cloud-native microservices **stateless**. 
After removing them, `RemoteUserAuthentication` class from Django REST Framework cannot be used directly,
since it requires `RemoteUserBackend` from default `auth`. 
This package extends the user model and authentication classes of Django REST Framework with remote authentication protocols, 
so that it can provide resource servers with authorization by remote authorization server.

Besides, this package also aims to provide some methods to adapt service mesh framework like `PolarisMesh`.

## Installation 

Install with `pip`.

```shell
 pip install drf-remote-auth -i  https://quanttide-pypi.pkg.coding.net/qtapps-django/drf-remote-auth/simple
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