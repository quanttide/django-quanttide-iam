"""
Ref:
  - https://stackoverflow.com/questions/45959768/django-assert-many-to-many-relation-exists-in-test
"""

from django_tenants.test.cases import TenantTestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from users.views.group import UserGroupViewSet
from users.models import User, UserGroup
from staff.models import Staff


class UserGroupViewSetTestCase(TenantTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        # 授权员工
        self.staff_user = User.objects.create()
        Staff.objects.create(user=self.staff_user)
        # 用户
        self.user = User.objects.create(phone_number='+8618888888888')
        # 用户组
        self.group = UserGroup.objects.create(name='test-group')

    def test_add_user(self):
        self.assertFalse(self.group.users.exists())
        request = self.factory.post(path='/groups/test-group/adduser/', data={'phone_number': '+8618888888888'}, format='json')
        force_authenticate(request, user=self.staff_user)
        response = UserGroupViewSet.as_view({'post': 'add_user'})(request, name='test-group')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(self.group.users.exists())

    def test_remove_user(self):
        # 准备数据
        self.group.users.add(self.user)
        self.assertTrue(self.group.users.exists())
        # 调用
        request = self.factory.post(path='/groups/test-group/adduser/', data={'phone_number': '+8618888888888'}, format='json')
        force_authenticate(request, user=self.staff_user)
        response = UserGroupViewSet.as_view({'post': 'remove_user'})(request, name='test-group')
        # 验证
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(self.group.users.exists())
