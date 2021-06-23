# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from .models import AuthUser, AuthStaff


class AuthUserSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"
