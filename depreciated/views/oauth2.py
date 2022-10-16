"""
OAuth2协议视图函数

参考资料：
  - OAuth2协议文档：https://datatracker.ietf.org/doc/html/rfc6749#section-3
"""

from rest_framework.views import APIView


class AuthorizationView(APIView):
    """
    重定向到登录或注册。
    """
    def get(self):
        pass


class TokenView(APIView):
    """
    签发AccessToken和RefreshToken。

    对于具体模式：
      - Authorization Code Grant: 输入Authorization Endpoint签发的authorization_code。
      - Resource Owner Password Credentials Grant: 输入用户（OAuth Resource Owner）的username和password。
      - Client Credentials Grant: 输入资源服务（OAuth Client）的client_id和client_secret。
    """
    def post(self, request):
        pass


class RevokeTokenView(APIView):
    def post(self, request):
        pass
