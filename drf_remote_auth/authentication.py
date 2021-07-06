# -*- coding: utf-8 -*-
"""
TODO：
  - 实现一个SecretKey版本的认证类。
  - 实现一个Staff可访问的认证类。

Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from django_qcloud.api import cloudbase_request_http_api
from requests.exceptions import HTTPError

from .serializers import AuthUserSerializer


class RemoteTokenAuthentication(BaseAuthentication):
    """
    DRF框架下基于远端服务器签发的Token实现的Authentication类。

    """
    def authenticate_header(self, request):
        """
        设置验证失败的响应错误码为`401 Unauthorized`并设置`WWW-Authenticate`（即返回值）。

        以下关于realm字段的说明摘自RFC2617（https://datatracker.ietf.org/doc/html/rfc2617#section-3.2.1）：
          A string to be displayed to users so they know which username and
          password to use. This string should contain at least the name of
          the host performing the authentication and might additionally
          indicate the collection of users who might have access. An example
          might be "registered_users@gotham.news.com".

        PS：暂未搞清楚`WWW-Authenticate`及`realm`参数的意义，遵循官方标准走。
        """
        return 'Bearer realm="jwt"'

    def authenticate(self, request):
        """
        自定义验证，调用量潮用户服务验证是否为量潮用户。

        标准返回值为`(user, auth)`，异常为`NotAuthenticated`和`AuthenticationFailed`。
        """
        # 检查Token是否存在，否则抛出NotAuthenticated异常
        auth: str = request.META.get('Authorization', None)
        if not auth:
            raise NotAuthenticated("Authorization为空")

        # 通过用户服务验证JWT接口验证用户身份，成功则按标准格式返回，失败抛出AuthenticationFailed
        try:
            # 验证成功，返回200
            # TODO：如果需要强制指定Content-Type才可以通过，修改腾讯云SDK的API使之暴露headers参数。
            user_data = cloudbase_request_http_api(method='POST', path='/users/jwt-verify', data={"token": auth})
        except HTTPError:
            # 验证失败，返回400（Bad Request）
            raise AuthenticationFailed(detail='用户服务验证JWT失败')

        # 检查用户数据是否为空
        if not user_data:
            raise NotAuthenticated(detail='无用户数据，请开发者检查用户服务是否有错误逻辑')

        # 反序列化
        serializer = AuthUserSerializer(data=user_data)
        if not serializer.is_valid():
            # 备注：大概率是系统内部错误
            raise AuthenticationFailed(detail='用户数据反序列化异常，请开发者检查本库的模型层和序列化层是否有错误逻辑')
        user = serializer.instance

        # 验证用户模型标记，主要用以处理来自服务内部的自定义逻辑（比如安全机制等）。
        if not user.is_active:
            # 未激活状态
            raise AuthenticationFailed(detail='用户未激活或被封禁')
        if not user.is_authenticated:
            # 未认证通过状态
            raise AuthenticationFailed(detail='用户服务内部验证失败')

        # 返回用户信息
        return user, auth
