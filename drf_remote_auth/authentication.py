"""
Authentication classes for Django REST Framework.

Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
  - https://github.com/jpadilla/django-rest-framework-jwt/blob/master/rest_framework_jwt/authentication.py
"""

from rest_framework.authentication import BaseAuthentication, get_authorization_header

from drf_remote_auth.serializers import IDTokenSerializer


class IDTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = None
        id_token = get_authorization_header(request).split(' ')[1]
        serializer = IDTokenSerializer(data=id_token)
        if serializer.is_valid(raise_exception=True):
            user = serializer.user
        return user, id_token
