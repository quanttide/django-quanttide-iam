# -*- coding: utf-8 -*-

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class QtAuthentication(BaseAuthentication):
    """
    Ref:
      - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
    """
    def authenticate_header(self, request):
        pass

    def authenticate(self, request):
        # 检查Token是否存在，否则返回None
        auth: str = request.META.get('Authorization')
        if not auth:
            return None

        # 从用户服务检查用户是否存在，否则返回AuthenticationFailed
        try:
            user = None
        except:
            raise AuthenticationFailed('No such user')

        # 返回用户信息
        return (user, auth)

