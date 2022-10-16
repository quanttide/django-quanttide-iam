# -*- coding: utf-8 -*-

import uuid

from django.test import TestCase
from django.db.utils import OperationalError

from django_qtcloud_idam.models import AuthUser
from .models import CustomUser


class AuthUserTestCase(TestCase):
    """
    Default AuthUser for Resource Server
    """
    def test_init(self):
        # 未激活用户
        inactive_user = AuthUser(is_active=False)
        # 匿名用户
        anonymous_user = AuthUser()
        # 鉴权用户
        auth_user = AuthUser(id=uuid.uuid4(), is_authenticated=True)
        # 员工
        staff = AuthUser(id=uuid.uuid4(), is_authenticated=True, is_staff=True)
        # 系统管理员
        super_user = AuthUser(id=uuid.uuid4(), is_authenticated=True, is_staff=True, is_superuser=True)


class CustomAuthUserTestCase(TestCase):
    """
    Custom AuthUser for Authorization Server
    """
    model_class = CustomUser

    def test_model_fields(self):
        # ref: https://stackoverflow.com/questions/3106295/django-get-list-of-model-fields
        model_fields = {f.name for f in self.model_class._meta.get_fields()}
        self.assertEqual({'user_id', 'is_staff', 'is_superuser'}, model_fields)

    def test_init(self):
        auth_user = CustomUser(user_id=uuid.uuid4())
        auth_user.save()
