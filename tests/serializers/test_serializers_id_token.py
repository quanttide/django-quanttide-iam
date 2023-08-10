# -*- coding: utf-8 -*-
"""
序列化层测试
"""

from django_tenants.test.cases import TenantTestCase

from users.models.user import User
from auth.serializers.id_token import IDTokenSerializer


class IDTokenSerializerTestCase(TenantTestCase):
    def setUp(self):
        self.user_model_class = User
        self.user = self.user_model_class()

    def test_serialize(self):
        """
        序列化，使用AuthUser签发IDToken。
        """
        serializer = IDTokenSerializer(self.user)
        id_token: str = serializer.data
        self.assertTrue('id_token' in id_token)

    def test_deserialize(self):
        """
        反序列化，解析IDToken字符串为AuthUser数据模型。
        """
        pass  # serializer = IDTokenSerializer(data=self.id_token)  # self.assertTrue(serializer.is_valid())  # user = serializer.instance
