# -*- coding: utf-8 -*-

from drf_remote_auth.models import AbstractUser


class CustomUser(AbstractUser):
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
