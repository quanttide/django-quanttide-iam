"""

"""
from uuid import uuid4

from django.test import TestCase
from django.contrib.auth import get_user_model

from drf_remote_auth.serializers import UserSerializer, IDTokenSerializer


class UserSerializerTestCase(TestCase):
    def test_serialize(self):
        pass


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
