"""
身份认证类
"""

from rest_framework.authentication import BaseAuthentication, get_authorization_header

from django_quanttide_idam.serializers.serializers import IDTokenSerializer, AccessTokenSerializer


class AccessTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = None
        access_token = get_authorization_header(request).split(' ')[1]
        serializer = AccessTokenSerializer(data=access_token)
        if serializer.is_valid(raise_exception=True):
            user = serializer.instance
        return user, access_token


class IDTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = None
        id_token = get_authorization_header(request).split(' ')[1]
        serializer = IDTokenSerializer(data=id_token)
        if serializer.is_valid(raise_exception=True):
            user = serializer.instance
        return user, id_token
