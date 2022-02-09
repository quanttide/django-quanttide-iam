"""
Authentication classes for Django REST Framework.

Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

# from .token import RemoteTokenAuthentication
from .oidc import *
