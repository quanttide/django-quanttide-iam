"""
授权API
"""

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class PublicKeyView(APIView):
    def get(self, request):
        # https://stackoverflow.com/questions/19516617/how-should-an-rsa-public-key-be-exposed-over-http
        return Response(data=settings.AUTH_PUBLIC_KEY, content_type="application/x-pem-file")
