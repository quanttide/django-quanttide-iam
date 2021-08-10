# -*- coding: utf-8 -*-

from django.db import models


class AuthUser(models.Model):
    """

    """
    # --- 字段 ---
    # -- 用户唯一性标记 --
    user_id = models.CharField(max_length=32, primary_key=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    # -- 用户权限标记 --
    # 是否匿名
    is_anonymous = models.BooleanField(default=True)
    # 是否激活
    is_active = models.BooleanField(default=False)
    # 是否认证
    is_authenticated = models.BooleanField(default=False)
    # 是否员工
    is_staff = models.BooleanField(default=False)

    # --- AuthUserModel必须设置 ---
    USERNAME_FILED = 'user_id'
    # TODO：根据业务逻辑调整
    REQUIRED_FIELDS = ['user_id', 'is_authenticated']

    # --- assert语句 ---
    if is_anonymous:
        assert not is_active and not is_authenticated and not is_staff, "匿名用户等同于未认证用户"
    if is_authenticated:
        assert not is_anonymous and is_active, "未激活账号不可以通过认证"
    if is_staff:
        assert not is_anonymous and is_active and is_authenticated, "员工账号必须是激活的认证用户"

    # --- 设置 ---
    class Meta:
        # 不存到数据库
        # TODO：此设置存疑
        migrate = False
