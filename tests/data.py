"""
测试数据
"""
from rest_framework.test import APIRequestFactory

from django_qtcloud_idam.models import AuthUser


class TestDataMixin:
    def setUp(self):
        # 测试工具
        self.factory = APIRequestFactory()
        # 测试数据
        self.user = AuthUser()
        self.id_token = ''
        self.access_token = ''
