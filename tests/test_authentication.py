"""

"""

from django.test import TestCase

from django_quanttide_idam.authentication import AccessTokenAuthentication
from tests.data import TestDataMixin


class AccessTokenAuthenticationTestCase(TestDataMixin, TestCase):
    authentication_class = AccessTokenAuthentication
    authentication_instance = authentication_class()

    def test_authenticate(self):
        request = self.factory.get('/')
        user, auth = self.authentication_instance.authenticate(request)
        self.assertEqual(user, self.user)
        self.assertEqual(auth, self.access_token)

    def test_authenticate_failed(self):
        unauthenticated_request = self.factory.get('/')
        # unauthenticated_response = id_token_authentication_view(request=unauthenticated_request)
        # self.assertEqual(HTTP_401_UNAUTHORIZED, unauthenticated_response.status_code)


class IDTokenAuthenticationTestCase(TestDataMixin, TestCase):
    def test_authenticate(self):
        pass

    def test_authenticate_failed(self):
        unauthenticated_request = self.factory.get('/')
        # unauthenticated_response = id_token_authentication_view(request=unauthenticated_request)
        # self.assertEqual(HTTP_401_UNAUTHORIZED, unauthenticated_response.status_code)
