"""
序列化层测试
"""

from authlib.jose import jwt
from django.conf import settings
from django_tenants.test.cases import TenantTestCase

from users.models.user import User
from auth.serializers.access_token import AccessTokenSerializer


class AccessTokenSerializerTestCase(TenantTestCase):
    def setUp(self):
        self.user_model_class = User
        self.user = self.user_model_class()

    def test_serialize(self):
        """
        序列化，使用AuthUser签发AccessToken。
        """
        serializer = AccessTokenSerializer(instance=self.user)
        access_token: str = serializer.data.get('access_token')
        self.assertTrue(access_token)
        claims = jwt.decode(access_token, settings.AUTH_PUBLIC_KEY)
        # example:
        # {'iss': 'fake-iss', 'aud': 'fake-aud', 'iat': 1672042597, 'exp': 1672046197, 'auth_time': 1672042597,
        # 'id': '404d361c-18d8-4b01-baf0-69f99ab09bf3', 'is_anonymous': False, 'is_active': True,
        # 'is_authenticated': True, 'is_staff': False, 'is_superuser': False}
        self.assertEqual(claims['iss'], settings.AUTH_ISS)
        self.assertEqual(claims['aud'], settings.AUTH_AUD)
        # TODO: 完整覆盖字段校验
        # print(claims)

    def test_deserialize(self):
        """
        反序列化，解析AccessToken字符串为AuthUser数据模型。
        """
        # 模拟生成AccessToken
        header = {'alg': 'RS256'}
        payload = {'iss': settings.AUTH_ISS, 'sub': str(self.user.id), 'aud': settings.AUTH_AUD}
        access_token = jwt.encode(header, payload, settings.AUTH_PRIVATE_KEY)
        # 校验
        serializer = AccessTokenSerializer(self.user, data={'access_token': access_token})
        self.assertTrue(serializer.is_valid())
        # OrderedDict([('sub', UUID('9b63c9e9-2df5-4f31-9069-a28e53787bf1')),
        # ('is_anonymous', True), ('is_active', False), ('is_authenticated', False),
        # ('is_staff', False), ('is_superuser', False)])
        # print(serializer.validated_data)