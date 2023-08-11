"""
用户序列化类
"""

from django.contrib.auth import get_user_model
from django_quanttide_idam.models import AuthUser
from rest_framework import serializers

from authlib.oidc.core.claims import UserInfo
from authlib.oidc.core.grants.util import generate_id_token
from authlib.jose import jwt


class AuthUserSerializer(serializers.ModelSerializer):
    """
    鉴权用户序列化类

    匿名用户序列化
    -----
    >>> from django_quanttide_idam.models import AuthUser
    >>> from django_quanttide_idam.users import AuthUserSerializer
    >>> anonymous_user = AuthUser()
    >>> serializer = AuthUserSerializer()
    >>> serializer.data
    {'user_id': 'e32ac5834bc64bc3b24853f4a3f2802f',, 'is_active': True, 'is_authenticated': False, 'is_staff': False}

    认证用户序列化
    -----
    >>> import uuid
    >>> from django_quanttide_idam.models import AuthUser
    >>> from django_quanttide_idam.users import AuthUserSerializer
    >>> user = AuthUser(id=uuid.uuid4(), is_authenticated=True)
    >>> serializer = AuthUserSerializer(user)
    >>> serializer.data
    {'user_id': 'e32ac5834bc64bc3b24853f4a3f2802f', 'is_active': True, 'is_authenticated': True, 'is_staff': False}
    """

    class Meta:
        model = AuthUser
        fields = ['id', 'is_active', 'is_authenticated', 'is_staff', 'is_superuser']
        extra_kwargs = {
            # 开发者笔记：
            #  - 模型层字段editable=True时，空序列化过滤此字段，因此必须关闭此选项。暂未找到具体源码位置。
            #  - format=hex可以以32位字符串格式显示数据。
            # 'id': {'format': 'hex'},
            #  DRF官方文档：Django 2.1起BooleanField的default=False，users.BooleanField同样设置default=True无效，设置initial=True对空序列化有效。
            #  实测结果：initial参数对于空序列化（相当于空表单）有效，default对于序列化且partial_update = False时字段无参数有效。
            #  分析源码：空序列化调用Serializer的get_initial方法，其调用Field的get_initial方法读取设置的initial参数。
            #  由于这里使用空序列化为匿名用户、序列化为认证用户，请开发者遵守上述方式设置。
            'is_active': {'default': True, 'initial': True},
            'is_authenticated': {'default': False, 'initial': False},
            'is_staff': {'default': False, 'initial': False},
            'is_superuser': {'default': False, 'initial': False},
        }


class JWTSerializer(AuthUserSerializer):
    """
    JWT序列化类
    """
    pass


class AccessTokenSerializer(AuthUserSerializer):
    """
    AccessToken序列化类
    """
    def __init__(self, instance, data, aud, iss=None):
        super().__init__(instance, data)
        self.iss = iss
        self.aud = aud

    def to_representation(self, instance) -> str:
        user_info = super().to_representation(instance)
        access_token = generate_id_token({}, user_info, 'IDTOKEN_KEY', self.iss, self.aud)
        return access_token

    def to_internal_value(self, access_token: str):
        data = UserInfo(**jwt.decode(access_token))
        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)


class IDTokenSerializer(AuthUserSerializer):
    """
    IDToken序列化类

    TODO: 设计UserProfile字段加入的方案。
    """
    def __init__(self, instance, data, aud, iss=None):
        super().__init__(instance, data)
        self.iss = iss
        self.aud = aud

    def to_representation(self, instance) -> str:
        user_info = super().to_representation(instance)
        id_token = generate_id_token({}, user_info, 'idtoken_key', self.iss, self.aud)
        return id_token

    def to_internal_value(self, id_token: str):
        data = UserInfo(**jwt.decode(id_token))
        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)
