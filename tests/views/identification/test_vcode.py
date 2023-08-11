from django.test import TestCase


class VCodeLoginTestCase(TestCase):
    def setUp(self):
        self.vcode_login_data = {'phone_number': '19999999999', 'verification_code': '123456'}
        # 设置缓存模拟验证码发送
        cache.set('+86' + self.vcode_login_data['phone_number'], self.vcode_login_data['verification_code'])

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


class WechatLoginTestCase(TestCase):
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
