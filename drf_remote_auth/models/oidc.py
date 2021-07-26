# -*- coding: utf-8 -*-

from django.db import models

from drf_remote_auth.models.base import AuthUser


class OpenIDAuthUser(AuthUser):
    """
    Serialized from IDToken following OpenID Connect Protocol.
    """
    pass


class OpenIDUserProfile(models.Model):
    """
    Serialized from userinfo API.
    """
    class Meta:
        migrate = False
