"""
登录注册视图。
"""

from rest_framework.views import APIView


class IDTokenProviderView(APIView):
    def post(self, request):
        pass


class RegisterView(IDTokenProviderView):
    pass


class PasswordRegisterView(RegisterView):
    """
    用户名密码注册视图。
    """
    pass


class LoginView(IDTokenProviderView):
    pass


class PasswordLoginView(LoginView):
    """
    用户名密码登录视图。
    """
    pass


class LoginOrRegisterView(IDTokenProviderView):
    pass


class VCodeLoginOrRegisterView(LoginOrRegisterView):
    """
    验证码登录或注册视图。
    """
    pass


class VLinkLoginOrRegisterView(LoginOrRegisterView):
    """
    验证链接登录或注册视图。
    """
    pass
