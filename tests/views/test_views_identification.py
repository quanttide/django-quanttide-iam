from django_tenants.test.cases import TenantTestCase
from django.core.cache import cache
from rest_framework.test import APIRequestFactory
from rest_framework import status

from users.models.user import User
from auth.views.identification import PasswordLoginView, PasswordSignUpView, VCodeLoginView


class PasswordSignInViewTestCase(TenantTestCase):
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


class PasswordSignUpTestCase(TenantTestCase):
    def test_signup(self):
        """
        注册账号，输入值为手机号及验证码、两次密码
        :return:
        """
        signup_data = {'phone_number': '+8619999999999', 'vcode': '123456', 'password': 'ga23gsge23', 'password2': 'ga23gsge23'}
        # 模拟发送验证码
        cache.set(signup_data['phone_number'], signup_data['vcode'])
        request = APIRequestFactory().post('/', data=signup_data, HTTP_REFERER='/', format='json')
        response = PasswordSignUpView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)
        # 验证用户已创建
        self.assertTrue(User.objects.filter(phone_number=signup_data['phone_number']).exists())


class VCodeLoginTestCase(TenantTestCase):
    def setUp(self):
        self.vcode_login_data = {'phone_number': '19999999999', 'vcode': '123456'}
        # 设置缓存模拟验证码发送
        cache.set('+86' + self.vcode_login_data['phone_number'], self.vcode_login_data['vcode'])

    def test_signup(self):
        request = APIRequestFactory().post('/', data=self.vcode_login_data, HTTP_REFERER='/', format='json')
        response = VCodeLoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)
        self.assertTrue(User.objects.filter(phone_number=self.vcode_login_data['phone_number']).exists())

    def test_login(self):
        """
        验证码登录，输入值为手机号及验证码
        :return:
        """
        # 模拟已注册
        User.objects.create(phone_number=self.vcode_login_data['phone_number'])
        request = APIRequestFactory().post('/', data=self.vcode_login_data, HTTP_REFERER='/', format='json')
        response = VCodeLoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)


class WechatLoginTestCase(TenantTestCase):
    def test_wechat_login(self):
        """
        微信登录或注册，输入值为客户端从微信API获取的临时票据code

        :return:
        """
        # data = {'code': 'test'}
        # request = APIRequestFactory().get('/', data=data, HTTP_REFERER='/', format='json')
        # response = WeChatUserLoginView.as_view()(request)
        # self.assertEqual(response.status_code, HTTP_200_OK)
        # self.assertTrue(response.data['jwt'])
        # print(response.data['jwt'])
        pass
