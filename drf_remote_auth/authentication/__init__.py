# -*- coding: utf-8 -*-
"""
Ref:
  - https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
"""

from .token import RemoteTokenAuthentication
from .oidc import *
