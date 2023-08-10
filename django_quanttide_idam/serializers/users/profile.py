# -*- coding: utf-8 -*-

from rest_framework import serializers

from users.models.user import User
from models.models import UserProfile


class UserSimpleSerializer(serializers.ModelSerializer):
    """
    用户模型序列化类简化版，可用于大部分基本逻辑认证和数据分析的可公开字段。
    """
    class Meta:
        model = User
        fields = ['qtid', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户信息序列化类，用于业务数据分析。
    """
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    用户模型的完整序列化类，用于管理后台。
    """
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
