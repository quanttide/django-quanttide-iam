"""

"""

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from authlib.oidc.core.claims import UserInfo
from authlib.oidc.core.grants.util import generate_id_token
from authlib.jose import jwt

from drf_remote_auth.settings import drf_remote_auth_settings


# ----- 基本类 -----

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


# ----- IDToken序列化 -----

class IDTokenSerializer(UserSerializer):
    def __init__(self, instance, data, aud, iss=None):
        super().__init__(instance, data)
        self.iss = iss or drf_remote_auth_settings.IDTOKEN_ISS
        self.aud = aud

    def to_representation(self, instance) -> str:
        user_info = super().to_representation(instance)
        id_token = generate_id_token({}, user_info, drf_remote_auth_settings.IDTOKEN_KEY, self.iss, self.aud)
        return id_token

    def to_internal_value(self, id_token: str):
        data = UserInfo(**jwt.decode(id_token))
        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)
