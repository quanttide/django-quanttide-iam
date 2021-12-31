# -*- coding: utf-8 -*-

from django.db import models


class AbstractAuthUser(models.Model):
    """
    鉴权用户的抽象类

    用法：
    - 资源服务直接使用此抽象类的继承。
    - 鉴权服务继承此抽象类实现自定义鉴权用户类。
    """
    # -- 用户唯一性标记 --
    user_id = models.UUIDField(primary_key=True)

    # -- 用户权限标记 --
    # 是否匿名
    is_anonymous = models.BooleanField(default=True)
    # 是否激活
    is_active = models.BooleanField(default=False)
    # 是否认证
    is_authenticated = models.BooleanField(default=False)
    # 是否员工
    is_staff = models.BooleanField(default=False)
    # 是否系统管理员
    is_superuser = models.BooleanField(default=False)

    # AuthUserModel必须设置
    USERNAME_FILED = 'user_id'
    REQUIRED_FIELDS = ['user_id', 'is_anonymous', 'is_active', 'is_authenticated', 'is_staff', 'is_superuser']

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 字段验证
        # TODO: `assert`用法不符合Google Style规范。
        if self.is_anonymous:
            assert not self.is_active and not self.is_authenticated, "匿名用户等同于未认证用户"
        if self.is_authenticated:
            assert not self.is_anonymous and self.is_active, "未激活账号不可以通过认证"
        if self.is_staff:
            assert self.is_authenticated, "员工账号必须是激活的认证用户"
        if self.is_superuser:
            assert self.is_staff, "超级管理员必须是员工账号"


class AuthUser(AbstractAuthUser):
    """
    鉴权用户。用于鉴权客户端（即资源服务）。
    """
    class Meta:
        # 不存到数据库
        managed = False
