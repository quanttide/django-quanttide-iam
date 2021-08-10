# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from drf_remote_auth.models import AuthUser


class AuthUserSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"
