# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer


class AuthUserSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
