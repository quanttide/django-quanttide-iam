from rest_framework.fields import empty

from authlib.oidc.core.claims import UserInfo
from authlib.oidc.core.grants.util import generate_id_token
from authlib.jose import jwt

from .base import AuthUserSerializer


class IDTokenSerializer(AuthUserSerializer):
    """
    IDToken序列化类
    """
    def __init__(self, instance=None, data=empty, aud=None, iss=None):
        super().__init__(instance=instance, data=data)
        self.iss = iss or 'fake-iss'  # settings.ID_TOKEN_ISS
        self.aud = aud or 'fake-aud'  # settings.ID_TOKEN_AUD

    def to_representation(self, instance):
        user_info = super().to_representation(instance)
        # settings.ID_TOKEN_KEY
        # alg='RS256'
        id_token = generate_id_token({}, user_info, 'fake-key', self.iss, self.aud, alg='HS256')
        return {'id_token': id_token}

    def to_internal_value(self, id_token: str):
        data = UserInfo(**jwt.decode(id_token, 'fake-key'))
        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)
