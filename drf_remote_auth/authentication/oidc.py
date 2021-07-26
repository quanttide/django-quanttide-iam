# -*- coding: utf-8 -*-
"""
Authentication class for Django REST Framework for resource server by OpenID Connect Protocol.

`AccessTokenAuthentication` and its subclass are used to authenticate for the resource server
following [Section 7 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-7).

Ref:
    - RFC6749(The OAuth 2.0 Authorization Framework): https://datatracker.ietf.org/doc/html/rfc6749

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

    Validate the access token by the coordination with the authentication server.
    [Section 5.3 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) requires that
    > The Access Token obtained from an OpenID Connect Authentication Request MUST be sent as a Bearer Token.
    > It is RECOMMENDED that the request use the HTTP GET method and the Access Token be sent using the Authorization header field.

    Ref:
      - OAuth2: https://datatracker.ietf.org/doc/html/rfc6749#section-7
      - OpenID Connect: https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
    """
    def authenticate(self, request):
        # request userinfo as recommended in [Section 5.3.1 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfoRequest)
        response = requests.get('/userinfo', headers={
            'HOST': '',  # TODO
            'Authorization': request.headers.get('Authorization'),
        })
        # suppose userinfo response as recommended in [Section 5.3.2 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse)
        if response.status_code == 200:
            # validate userinfo response following [Section 5,3,4 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponseValidation)
            pass
        # suppose error response as recommended by in [Section 5.3.3 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfoError)
        elif response.status_code == 401:
            pass
        else:
            # Developer's Note:
            #   I am not sure whether this exception class is appropriate for this situation.
            raise ValueError('Status code {status_code} is not a appropriate one for this API.'.format(status_code=response.status_code))


# ----- Refresh Token -----

class RefreshTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass
