"""

"""

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.status import HTTP_401_UNAUTHORIZED

from .views import id_token_authentication_view


class AccessTokenAuthenticationTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_authenticate(self):
        pass

    def test_authenticate_failed(self):
        unauthenticated_request = self.factory.get('/')
        unauthenticated_response = id_token_authentication_view(request=unauthenticated_request)
        self.assertEqual(HTTP_401_UNAUTHORIZED, unauthenticated_response.status_code)


class IDTokenAuthenticationTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_authenticate(self):
        pass

    def test_authenticate_failed(self):
        unauthenticated_request = self.factory.get('/')
        unauthenticated_response = id_token_authentication_view(request=unauthenticated_request)
        self.assertEqual(HTTP_401_UNAUTHORIZED, unauthenticated_response.status_code)
