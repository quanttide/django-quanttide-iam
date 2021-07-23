# -*- coding: utf-8 -*-
"""
OpenID Connect协议
"""

import os

from rest_framework.authentication import BaseAuthentication
from oauthlib.oauth2 import LegacyApplicaitonClient
from requests_oauthlib import OAuth2Session


class OAuth2Authentication(BaseAuthentication):
    def authenticate(self, request):
        pass


class LegacyApplicationAuthentication(BaseAuthentication):
    """
    Resource Owner Password Credentials Grant
    """
    def authenticate(self, request):
        username = request.data['username']
        password = request.data['password']
        client_id = os.environ['CLIENT_ID']
        client_secret = os.environ['CLIENT_SECRET']
        oauth = OAuth2Session(client=LegacyApplicaitonClient(client_id=client_id))
        token = oauth.fetch_token(token_url=os.environ['OIDC_ENDPOINT'], username=username, password=password,
                                  client_id=client_id, client_secret=client_secret)
