# -*- coding: utf-8 -*-

from drf_remote_auth.models import AbstractAuthUser


class CustomAuthUser(AbstractAuthUser):
    """
    property属性会覆盖Field属性。
    """
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
