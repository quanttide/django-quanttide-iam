"""
用户模型类

重新定义激活用户和匿名用户。
Django官方的匿名用户为`is_active=False`、`is_anonymous=True`。
我们重新定义为`is_active=True`，并把`is_active`定义为失效用户。

默认创建一个匿名用户。
"""
import uuid

from django.db import models


class AbstractAuthUser(models.Model):
    """
    用户模型抽象类
    """
    # -- 用户唯一性标记 --
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # -- 用户权限标记 --
    # 是否激活
    is_active = models.BooleanField(default=True)
    # 是否认证
    is_authenticated = models.BooleanField(default=False)
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
        if self.is_staff:
            assert self.is_authenticated, "员工必须是认证用户"
        if self.is_superuser:
            assert self.is_staff, "系统管理员必须是员工"

    @property
    def is_anonymous(self):
        """
        是否匿名

        匿名用户定义为未通过鉴权的激活用户
        """
        return self.is_active and not self.is_authenticated


class AuthUser(AbstractAuthUser):
    """
    用户模型类
    """
    class Meta:
        # TODO: 允许设置
        managed = True
