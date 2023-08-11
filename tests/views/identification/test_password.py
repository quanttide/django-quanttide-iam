from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import APIRequestFactory
from rest_framework import status

from django_quanttide_idam.models import User
from django_quanttide_idam.views import PasswordLoginView, PasswordSignUpView


class PasswordLoginViewTestCase(TestCase):
    def setUp(self):
        self.login_data = {'phone_number': '18888888888', 'password': 'ge34ttgxt43'}
        User.objects.create(**self.login_data)

    def test_login(self):
        """
        密码登录，输入值为手机号、密码
        :return:
        """
        request = APIRequestFactory().post('/', data=self.login_data, HTTP_REFERER='/', format='json')
        response = PasswordLoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)

    def test_login_password_error(self):
        login_data = {'phone_number': '18888888888', 'password': 'error'}
        request = APIRequestFactory().post('/', data=login_data, HTTP_REFERER='/', format='json')
        response = PasswordLoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PasswordSignUpTestCase(TestCase):
    def test_signup(self):
        """
        注册账号，输入值为手机号及验证码、两次密码
        :return:
        """
        signup_data = {'phone_number': '+8619999999999', 'verification_code': '123456', 'password': 'ga23gsge23', 'password2': 'ga23gsge23'}
        # 模拟发送验证码
        cache.set(signup_data['phone_number'], signup_data['verification_code'])
        request = APIRequestFactory().post('/', data=signup_data, HTTP_REFERER='/', format='json')
        response = PasswordSignUpView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)
        # 验证用户已创建
        self.assertTrue(User.objects.filter(phone_number=signup_data['phone_number']).exists())
