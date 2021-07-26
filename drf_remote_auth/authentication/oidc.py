# -*- coding: utf-8 -*-
"""
About `AccessTokenAuthentication` class:

    Validate the access token by the coordination with the authentication server.
    [Section 5.3 of OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) requires that
    > The Access Token obtained from an OpenID Connect Authentication Request MUST be sent as a Bearer Token.
    > It is RECOMMENDED that the request use the HTTP GET method and the Access Token be sent using the Authorization header field.

    Ref:
      - OpenID Connect: https://openid.net/specs/openid-connect-core-1_0.html#UserInfo
"""