# -*- coding: utf-8 -*-
"""
Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from django_qcloud.api import cloudbase_request_http_api


class QtAuthentication(BaseAuthentication):
    """
    QtApps的DRF服务的通用Authentication类。

    注意：
      - 此Auth类为QtApps唯一鉴权类，因此Auth不存在时抛出异常而不是返回None，和官方文档建议的实践不同。
    """
    def authenticate_header(self, request):
        pass

    def authenticate(self, request):
        # 检查Token是否存在，否则抛出NotAuthenticated异常
        auth: str = request.META.get('Authorization')
        if not auth:
            raise NotAuthenticated("Authorization为空")

        # 从用户服务检查用户是否存在，否则返回AuthenticationFailed
        try:
            # TODO：如果需要强制指定Content-Type才可以通过，修改腾讯云SDK的API使之暴露headers参数。
            user = cloudbase_request_http_api(method='POST', path='/users/jwt-verify', data={"token": auth})
        except Exception:
            raise AuthenticationFailed(detail='用户验证失败')

        # 返回用户信息
        return user, auth
