"""
鉴权用户模型。

和Django官方应用分离认证用户和匿名用户不同，本模块使用一个用户模型表达匿名用户和认证用户。
目前暂时无法确定哪种实现方式更好，需要更多用例验证。
"""

from django.db import models


class AbstractAuthUser(models.Model):
    """
    鉴权用户的抽象类。

    默认为匿名用户，id为空。

    用法：
    - 资源服务直接使用此抽象类的继承。
    - 鉴权服务继承此抽象类实现自定义鉴权用户类。
    """
    # -- 用户唯一性标记 --
    id = models.UUIDField(default=None, primary_key=True)

    # -- 用户权限标记 --
    # 是否匿名
    is_anonymous = models.BooleanField(default=True)
    # 是否激活
    is_active = models.BooleanField(default=False)
    # 是否员工
    is_staff = models.BooleanField(default=False)
    # 是否系统管理员
    is_superuser = models.BooleanField(default=False)

    # AuthUserModel必须设置
    USERNAME_FILED = 'id'
    REQUIRED_FIELDS = ['id']

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 字段验证
        # TODO: `assert`用法不符合Google Style规范。
        if self.is_anonymous:
            assert not self.is_active and not self.is_authenticated, "匿名用户等同于未认证用户"
        if self.is_staff:
            assert self.is_authenticated, "员工账号必须是激活的认证用户"
        if self.is_superuser:
            assert self.is_staff, "超级管理员必须是员工账号"

    @property
    def is_authenticated(self):
        return self.is_active


class AuthUser(AbstractAuthUser):
    """
    鉴权用户。用于鉴权客户端（即资源服务）。

    默认为匿名用户。
    """
    class Meta:
        # 不存到数据库
        managed = False


class User(AbstractAuthUser):
    """
    用户。用于鉴权服务端。
    """
    PHONE_NUMBER_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
