"""
Authentication classes for Django REST Framework.

Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

from rest_framework.authentication import BaseAuthentication


class IDTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass
