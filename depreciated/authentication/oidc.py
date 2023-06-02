# -*- coding: utf-8 -*-
"""
Authentication class for OpenID Connect Protocol.

Ref:
  -
"""

from rest_framework.authentication import BaseAuthentication

from django_quanttide_idam.models import AuthUser
from django_quanttide_idam.serializers import AuthUserSerializer


# ----- Access Grant Type -----

class OidcAuthCodeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass


# ----- Access Token and ID Token -----

class OidcAccessTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 获取AccessToken
        tokens = self.get_oidc_tokens_from_authorization_header(request)
        # 反序列化
        serializer = AuthUserSerializer(data=tokens)
        # 验证数据
        serializer.is_valid(raise_exception=True)
        # 返回值
        user = AuthUser(**serializer.validated_data)
        auth = tokens['access_token']
        return user, auth

    def get_oidc_tokens_from_authorization_header(self, request):
        return ''


class OidcIDTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass
