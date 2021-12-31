# -*- coding: utf-8 -*-

import uuid

from django.test import TestCase
from django.db.utils import OperationalError

from drf_remote_auth.models import AuthUser
from .models import CustomAuthUser


# ----- Default AuthUser for Resource Server -----

class AuthUserTestCase(TestCase):
    def test_init(self):
        auth_user = AuthUser(user_id=uuid.uuid4())
        with self.assertRaises(OperationalError) as e:
            auth_user.save()


# ----- Custom AuthUser for Authorization Server -----


class CustomAuthUserTestCase(TestCase):
    def test_init(self):
        auth_user = CustomAuthUser(user_id=uuid.uuid4())
        # TODO: 未知原因没有迁移。
        auth_user.save()
