# 测试框架
from django.conf import settings
from django_tenants.test.cases import TenantTestCase as TestCase
from rest_framework.test import APIRequestFactory

# 测试单元
from auth.views.authorization import PublicKeyView

# 测试工具
# from rest_framework_jwt.protocols import jwt_encode_handler
# from authentication import jwt_payload_handler


class PublicKeyViewTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get(self):
        request = self.factory.get('/')
        response = PublicKeyView.as_view()(request)
        self.assertEqual(response.content_type, 'application/x-pem-file')
        self.assertEqual(response.data, settings.AUTH_PUBLIC_KEY)


# class VerifyAuthViewTestCase(TestCase):
#     def setUp(self):
#         # 测试工具
#         self.factory = APIRequestFactory()
#         # 测试数据
#         self.user = User.objects.create()
#         self.payload = jwt_payload_handler(self.user)
#         self.token = jwt_encode_handler(self.payload)
#
#     def test_verify_auth_token(self):
#         request = self.factory.post(path='/', data={'token': self.token}, format='json')
#         response = VerifyAuthView.as_view()(request)
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertTrue(response.data['user_id'])
#         self.assertTrue(response.data['is_authenticated'])
#


