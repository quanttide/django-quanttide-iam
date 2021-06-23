# -*- coding: utf-8 -*-
"""
Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from django_qcloud.api import cloudbase_request_http_api
from requests.exceptions import HTTPError


class QtAuthentication(BaseAuthentication):
    """
    QtApps的DRF服务的通用Authentication类。

    注意：
      - 此Auth类为QtApps唯一鉴权类，因此Auth不存在时抛出异常，和官方文档建议返回None的实践不同。
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
            user = cloudbase_request_http_api(method='POST', path='/users/jwt-verify', data={"token": auth})
            # 返回用户信息
            return user, auth
        except HTTPError:
            # 验证失败，返回400（Bad Request）
            raise AuthenticationFailed(detail='用户验证失败')
