from django.contrib.auth import get_user_model
from rest_framework import serializers


class AuthUserSerializer(serializers.ModelSerializer):
    """
    认证用户序列化类

    - 空序列化：匿名用户，此时user_id为空、is_anonymous=True。
    - 序列化：认证用户，此时user_id非空，is_authenticated=True。
    - 反序列化：无业务逻辑意义，禁止操作数据库以保证安全。

    匿名用户序列化
    -----
    >>> from django_quanttide_idam.users import AuthUserSerializer
    >>> serializer = AuthUserSerializer()
    >>> serializer.data
    {'sub': None, 'is_anonymous': True, 'is_active': False, 'is_authenticated': False, 'is_staff': False}

    认证用户序列化
    -----
    >>> from drf_remote_auth.models import AuthUser
    >>> from drf_remote_auth.users import AuthUserSerializer
    >>> instance = AuthUser()
    >>> serializer = AuthUserSerializer(instance)
    >>> serializer.data #doctest: +ELLIPSIS
    {'sub': 'e32ac5834bc64bc3b24853f4a3f2802f', 'is_anonymous': False, 'is_active': True, 'is_authenticated': True, 'is_staff': False}
    """
    # 开发者笔记：
    #  DRF官方文档：Django 2.1起BooleanField的default=False，users.BooleanField同样设置default=True无效，设置initial=True对空序列化有效。
    #  实测结果：initial参数对于空序列化（相当于空表单）有效，default对于序列化且partial_update=False时字段无参数有效。
    #  分析源码：空序列化调用Serializer的get_initial方法，其调用Field的get_initial方法读取设置的initial参数。
    #  由于这里使用空序列化为匿名用户、序列化为认证用户，请开发者遵守上述方式设置。
    sub = serializers.UUIDField(default=None, initial=True)
    is_anonymous = serializers.BooleanField(default=True, initial=True)
    is_authenticated = serializers.BooleanField(default=False, initial=False)
    is_staff = serializers.BooleanField(default=False, initial=False)
    is_superuser = serializers.BooleanField(default=False, initial=False)

    class Meta:
        model = get_user_model()
        fields = ['sub', 'is_anonymous', 'is_active', 'is_authenticated', 'is_staff', 'is_superuser']
        extra_kwargs = {
            # 开发者笔记：
            #  - 模型层字段editable=True时，空序列化过滤此字段，因此必须关闭此选项。暂未找到具体源码位置。,
            'is_active': {'default': False, 'initial': False},
        }
