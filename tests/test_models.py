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
    model_class = CustomAuthUser

    def test_model_fields(self):
        # ref: https://stackoverflow.com/questions/3106295/django-get-list-of-model-fields
        model_fields = {f.name for f in self.model_class._meta.get_fields()}
        self.assertEqual({'user_id', 'is_staff', 'is_superuser'}, model_fields)

    def test_init(self):
        auth_user = CustomAuthUser(user_id=uuid.uuid4())
        auth_user.save()
