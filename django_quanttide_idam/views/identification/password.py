from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django_quanttide_idam.serializers import AccessTokenSerializer
from django_quanttide_idam.forms import PasswordLoginForm, PasswordSignUpForm


class PasswordLoginView(APIView):
    """
    用户名密码登录视图。

    ```
    {
        'mobile': '18888888888',
        'password': 'hashed_password',
    }
    ```
    """

    def post(self, request):
        form = PasswordLoginForm(request.data)
        if form.is_valid():
            serializer = AccessTokenSerializer(form.instance)
            return Response(data=serializer.data)
        else:
            return Response(data=form.errors, status=status.HTTP_401_UNAUTHORIZED)


class PasswordSignUpView(APIView):
    """
    用户名密码注册视图。

    ```
    {
        'mobile': '18888888888',
        'password': 'hashed_password',
        'password2': 'hashed_password',
        'verification_code': '123456',
    }
    ```
    """
    def post(self, request):
        form = PasswordSignUpForm(request.data)
        if form.is_valid():
            form.save()
            serializer = AccessTokenSerializer(form.instance)
            return Response(data=serializer.data)
        else:
            return Response(data=form.errors, status=status.HTTP_401_UNAUTHORIZED)
