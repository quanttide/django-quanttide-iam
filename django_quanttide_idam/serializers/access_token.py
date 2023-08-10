from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import empty

from authlib.oidc.core.claims import UserInfo
from authlib.oidc.core.grants.util import generate_id_token
from authlib.jose import jwt

from .base import AuthUserSerializer


class AccessTokenSerializer(AuthUserSerializer):
    """
    AccessToken序列化类
    """
    class Meta(AuthUserSerializer.Meta):
        pass

    def __init__(self, instance=None, data=empty, aud=None, iss=None):
        super().__init__(instance=instance, data=data)
        self.iss = iss or settings.AUTH_ISS
        self.aud = aud or settings.AUTH_AUD

    def to_representation(self, instance):
        user_info = super().to_representation(instance)
        # TODO: 重构为RFC9068
        access_token = generate_id_token({}, user_info, settings.AUTH_PRIVATE_KEY, self.iss, self.aud)
        return {'access_token': access_token}

    def to_internal_value(self, data):
        data = UserInfo(**jwt.decode(data['access_token'], settings.AUTH_PUBLIC_KEY))
        return super().to_internal_value(data)

    def validate(self, attrs):
        # 校验用户ID
        if self.instance and attrs['sub'] != self.instance.id:
            raise serializers.ValidationError('用户ID验证不通过')
        return super().validate(attrs)

