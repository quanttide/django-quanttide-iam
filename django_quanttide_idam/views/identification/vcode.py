from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django_quanttide_idam.serializers import AccessTokenSerializer
from django_quanttide_idam.forms import VCodeLoginForm


class VCodeLoginView(APIView):
    """
    验证码登录（或注册）视图。

    ```
    {
        'mobile': '1888888888',
        'vcode': '123456',
    }
    ```
    """

    def post(self, request):
        form = VCodeLoginForm(request.data)
        if form.is_valid():
            form.save()
            serializer = AccessTokenSerializer(form.instance)
            return Response(data=serializer.data)
        else:
            return Response(data=form.errors, status=status.HTTP_401_UNAUTHORIZED)
