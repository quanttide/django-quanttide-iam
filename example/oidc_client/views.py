# -*- coding: utf-8 -*-

from django.conf import settings

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from authlib.oidc.discovery import get_well_known_url
import requests


@api_view(['GET'])
@authentication_classes([])
def oidc_discover_view(request):
    """
    Cannot work on macOS without fix the SSL Certificate Problem.

    Ref:
        - https://medium.com/@yen.hoang.1904/resolve-issue-ssl-certificate-verify-failed-when-trying-to-open-an-url-with-python-on-macos-46d868b44e10
    """
    data = requests.get(
        get_well_known_url(
            settings.OIDC_AUTH['OIDC_ENDPOINT'],
            external=True
        )
    ).json()
    return Response(data=data)
