"""

"""
from uuid import uuid4
import doctest

from django.test import TestCase
from django.contrib.auth import get_user_model

from django_qtcloud_idam.models import AuthUser
from django_qtcloud_idam.serializers import AuthUserSerializer, IDTokenSerializer, AccessTokenSerializer

__test__ = {
    "AuthUserSerializer": AuthUserSerializer
}


class AuthUserSerializerTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.serializer_class = AuthUserSerializer
        cls.user = AuthUser()

    def test_serialize_anonymous_user(self):
        """
        匿名用户空序列化
        :return:
        """
        serializer = self.serializer_class()
        self.assertFalse(serializer.data['user_id'])
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
        self.assertTrue(serializer.data['user_id'])
        self.assertFalse(serializer.data['is_anonymous'])
        self.assertTrue(serializer.data['is_active'])
        self.assertTrue(serializer.data['is_authenticated'])
        self.assertFalse(serializer.data['is_staff'])


class AccessTokenSerializerTestCase(TestCase):
    @classmethod
    def setUpData(cls):
        cls.user_model_class = get_user_model()
        cls.user = cls.user_model_class(id=uuid4(), is_anonymous=False, is_active=True, is_authenticated=True)
        cls.access_token = ''

    def test_serialize(self):
        """
        序列化，使用AuthUser签发AccessToken。
        """
        serializer = AccessTokenSerializer(self.user)
        access_token: str = serializer.data
        # 验证AccessToken

    def test_deserialize(self):
        """
        反序列化，解析AccessToken字符串为AuthUser数据模型。
        """
        serializer = AccessTokenSerializer(data=self.access_token)
        self.assertTrue(serializer.is_valid())
        user = serializer.instance


class IDTokenSerializerTestCase(TestCase):
    @classmethod
    def setUpData(cls):
        cls.user_model_class = get_user_model()
        cls.user = cls.user_model_class(id=uuid4(), is_anonymous=False, is_active=True, is_authenticated=True)
        cls.id_token = ''

    def test_serialize(self):
        """
        序列化，使用User签发IDToken。
        """
        serializer = IDTokenSerializer(self.user)
        id_token: str = serializer.data
        # 验证IDToken

    def test_deserialize(self):
        """
        反序列化，解析IDToken字符串为User数据模型。
        """
        serializer = IDTokenSerializer(data=self.id_token)
        self.assertTrue(serializer.is_valid())
        user = serializer.instance
