# -*- coding: utf-8 -*-

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from drf_remote_auth.authentication.oauth2 import LegacyApplicationAuthentication


@api_view(['GET'])
@authentication_classes([LegacyApplicationAuthentication])
def legacy_app_auth_view(request):
    return Response(data='success')


class LegacyApplicationAuthenticationTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_authenticate(self):
        unauthenticated_request = self.factory.get('/')
        unauthenticated_response = legacy_app_auth_view(request=unauthenticated_request)
        self.assertEqual(HTTP_401_UNAUTHORIZED, unauthenticated_response.status_code)
