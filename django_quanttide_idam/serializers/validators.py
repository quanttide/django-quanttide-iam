# -*- coding: utf-8 -*-

import distutils

import requests
from authlib.oauth2.rfc7662 import IntrospectTokenValidator

from rest_framework.exceptions import ValidationError


class DRFAccessTokenValidator(IntrospectTokenValidator):
    """
    DRF Validator for introspecting access token of OAuth2 Protocol.

    It can alse be registered into `ResourceProtector` instance of `authlib` for Flask apps,
    but maybe useless in Django and DRF projects.
    """
    def __init__(self, token_introspection_api=None):
        self.token_introspection_api = token_introspection_api
        self.client_id = None
        self.client_secret = None
        super().__init__()

    def introspect_token(self, token: str) -> dict:
        """
        Token Introspection by [RFC 7762](https://datatracker.ietf.org/doc/html/rfc7662).

        It requests the token introspection API with HTTP Basic Auth
        (in the form of `Authorization: Basic <credentials>` where credentials is
        the Base64 encoding of ID and password joined by a single colon `:`).
        It will return the active state and meta-information of access token if successful
        according to [Section 2.2 of RFC 7762](https://datatracker.ietf.org/doc/html/rfc7662#section-2.2),
        and HTTP 401 Unauthorized status code if failed according to
        [Section 2.3 of RFC 7762](https://datatracker.ietf.org/doc/html/rfc7662#section-2.3).

        :param token: access token
        :return active state and meta of access token
        """
        data = {'token': token, 'token_type_hint': 'access_token'}
        # Tuple as input is a handy shorthand by `requests` for HTTP Basic Auth .
        # More: https://docs.python-requests.org/en/master/user/authentication/
        auth = (self.client_id, self.client_secret)
        r = requests.get(self.token_introspection_api, data=data, auth=auth)
        # Unauthorized
        if r.status_code == 401:
            raise ValidationError('Access token is invalid')
        # Authorization Server Internal Error or Internet Error
        r.raise_for_status()
        return_data = r.json()
        # Authorization Server Internal Error
        if 'active' not in return_data:
            raise ValidationError('Token Introspection API of Authorization Server has no `active` parameter.')
        # Convert a string representation of truth to true (1) or false (0).
        return_data['active'] = distutils.util.strtobool(return_data['active'])
        # Unauthorized
        if not return_data['active']:
            raise ValidationError('Access token is invalid')
        return return_data

    def __call__(self, value, serializer_field):
        pass
