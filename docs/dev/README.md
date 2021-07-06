# 开发者设计文档

`django-qtauth`计划升级成`drf-remote-auth`项目，作为通用的微服务鉴权客户端插件，计划支持的特性包括：
- 支持SSO单点登录。
- 支持CAS集中式鉴权。
- 支持OpenID Connect鉴权协议。
- 支持JWT作为鉴权Token。

此库需要整合来自社区的大量在维护和过时的库。 
考虑到这些库的API不统一、功能可能重合或者冲突，还有很多库过时不好维护，且设计出发点和我们不一样，零零散散的库对用户接入也十分不方便，
在思考很久以后放弃了补充少量插件的计划，而用这个库来打包社区现有方案、提供一个相对完整的支持以上特性的微服务远程鉴权解决方案。

## 社区现有积累

### 官方Auth框架
- 自定义DRF的Authentication类：https://www.django-rest-framework.org/api-guide/authentication/
- 自定义Django的AuthBackend：https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

### CAS客户端

### `django-cas-ng`

地址：https://djangocas.dev/docs/latest/index.html

这个库的核心机制是：
- 提供了一个类似于Django官方RemoteBackend的CASBackend，在CAS客户端接入。
- 提供了一些开箱即用的视图函数，在CAS服务端可以直接用。

使用方法见：
- https://www.linkedin.com/pulse/integrate-django-cas-sso-ui-json-web-token-jwt-razaqa-dhafin-haffiyan/

### OAuth2和OpenID Connect客户端

#### drf-oidc-auth

https://github.com/ByteInternet/drf-oidc-auth

核心特性：
- 提供了DRF的Authentication类。

### JWT客户端

`drf-jwt`提供了基于JWT的DRF的TokenAuthentication类，不再赘述。