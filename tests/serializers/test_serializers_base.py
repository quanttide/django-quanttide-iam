# -*- coding: utf-8 -*-
"""
序列化层测试
"""

from authlib.jose import jwt
from django.conf import settings
from django_tenants.test.cases import TenantTestCase

from users.models.user import User
from auth.serializers.base import AuthUserSerializer

__test__ = {
    "AuthUserSerializer": AuthUserSerializer
}


class AuthUserSerializerTestCase(TenantTestCase):
    @classmethod
    def setUp(cls):
        cls.serializer_class = AuthUserSerializer
        cls.user = User()

    def test_serialize_anonymous_user(self):
        """
        匿名用户空序列化
        :return:
        """
        serializer = self.serializer_class()
        self.assertTrue(serializer.data['sub'])
        self.assertTrue(serializer.data['is_anonymous'])
        self.assertFalse(serializer.data['is_active'])
        self.assertFalse(serializer.data['is_authenticated'])
        self.assertFalse(serializer.data['is_staff'])

    def test_serialize_authenticated_user(self):
        """
        认证用户序列化
        :return:
        """
        serializer = self.serializer_class(self.user)
        self.assertTrue(serializer.data['sub'])
        self.assertFalse(serializer.data['is_anonymous'])
        self.assertTrue(serializer.data['is_active'])
        self.assertTrue(serializer.data['is_authenticated'])
        self.assertFalse(serializer.data['is_staff'])