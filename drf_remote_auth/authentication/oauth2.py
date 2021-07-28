# -*- coding: utf-8 -*-
"""
Authentication class for Django REST Framework for resource server by OAuth2 Protocol.

OpenID Connect Protocol will be implemented by inheriting this module.

`AccessTokenAuthentication` and its subclass are used to authenticate for the resource server
following [Section 7 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-7) and
[RFC 7762](https://datatracker.ietf.org/doc/html/rfc7662).

Ref:
    - The OAuth 2.0 Authorization Framework (RFC 6749): https://datatracker.ietf.org/doc/html/rfc6749
    - OAuth 2.0 Token Introspection (RFC 7762): https://datatracker.ietf.org/doc/html/rfc7662

Author:
    - Guo Zhang (zhangguo@quanttide.com)
"""

import os

import requests
from rest_framework.authentication import BaseAuthentication
from oauthlib.oauth2 import WebApplicationClient, MobileApplicationClient, LegacyApplicationClient, BackendApplicationClient
from requests_oauthlib import OAuth2Session


# ----- Authorization Grant Flow -----

class WebApplicationAuthentication(BaseAuthentication):
    """
    Authorization code flow
    """
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
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
        token = oauth.fetch_token(token_url=os.environ['OIDC_ENDPOINT'], username=username, password=password,
                                  client_id=client_id, client_secret=client_secret)


# ----- Access Token -----

class AccessTokenAuthentication(BaseAuthentication):
    """
    User access token to authenticate for the resource server.
    [Section 7 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-7) requires
    > The client accesses protected resources by presenting the access token to the resource server.
    > The resource server MUST validate the access token and ensure that it has not expired and
    > that its scope covers the requested resource.

    Find access token from `Authorization` attributes for HTTP request header.
    [Section 7 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-7) requires
    > Typically, it involves using the HTTP "Authorization" request header field [RFC2617]
    > with an authentication scheme defined by the specification of the access oken type used,
    > such as [RFC6750].

    Different subclass with be defined for different types of access tokens.
    [Section 7 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-7) requires
    > The method in which the client utilizes the access token to authenticate with the resource server
    > depends on the type of access token issued by the authorization server.

    Ref:
      - OAuth2: https://datatracker.ietf.org/doc/html/rfc6749#section-7
    """
    def authenticate(self, request):
        pass


# ----- Refresh Token -----

class RefreshTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass
