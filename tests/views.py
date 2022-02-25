# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from drf_remote_auth.authentication import IDTokenAuthentication


@api_view(['GET'])
@authentication_classes([IDTokenAuthentication])
def id_token_authentication_view(request):
    return Response(data='success')
