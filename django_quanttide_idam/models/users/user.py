# -*- coding: utf-8 -*-
"""
基本用户模型
"""
import uuid
from functools import partial, reduce

from django.db import models
from django.db.models import Q
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


# 密码生成函数
set_unusable_password = partial(make_password, None)


class UserManager(models.Manager):
    """
    用户模型的管理类

    注意：
    - 本类的方法按需覆盖父类方法，主要即在调用父类方法之前对password字段加密即可。
    - 由于只有部分方法依赖save，所以不修改save方法以保持本类实例方法风格统一，防止出现对内部机理不够清楚而覆盖两次的误操作。
    - 调用save逻辑进行操作的，使用save方法手写和覆盖父类方法等价；调用QuerySet的方法，加密password的时候小心处理迭代器。

    代码风格：
    - 特别注意create方法和update方法处理password的逻辑不同。
    """
    def create(self, *args, **kwargs):
        """
        创建新用户

        - 若用户没有提供密码，则设置unusable_password

        :param args:
        :param kwargs:
        :return:

        用例：
        ```
        ```
        """
        # 加密用户传入密码，未传入时设置unusable密码
        kwargs['password'] = make_password(kwargs.get('password', None))
        return super().create(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        更新用户信息

        :param args:
        :param kwargs:
        :return:
        """
        # 如果传入password字段则更新，否则不更新
        if 'password' in kwargs:
            make_password(kwargs['password'])
        return super().update(*args, **kwargs)

    def get_by_natural_key(self, natural_key):
        """
        根据Django用户框架要求的USERNAME_FIELD查询，用于DRF-JWT用户认证框架符合规范。

        :param natural_key: USERNAME_FIELD，即user_id
        :return: 用户模型实例

        备忘：
          - self.model可以访问此ModelManager关联的Model实例。
        """
        return self.get(**{self.model.USERNAME_FIELD: natural_key})

    def get_by_username(self, username):
        """
        根据自定义的USERNAME_FIELD_LIST中的任何一个字段查询用户，用于对外暴露API的用户名相关业务逻辑。

        :param username: 合法的username字段，即user_id、mobile或email
        :return: 用户模型实例

        备忘：
          - 这里使用了map-reduce模式处理，map过程处理Q()计算，reduce进行|的逻辑运算。

        Ref:
          - Python的map-reduce：https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
          - Django的Q()：https://docs.djangoproject.com/en/3.1/ref/models/querysets/#q-objects
          - Django的or逻辑： https://docs.djangoproject.com/en/3.1/ref/models/querysets/#or
        """
        return self.get(reduce(lambda q1, q2: q1 | q2, map(lambda username_field: Q(**{username_field: username}), self.model.USERNAME_FIELD_LIST)))

    def get_or_create(self, defaults=None, **kwargs):
        created = False
        try:
            obj = self.get(**kwargs)
        except self.model.DoesNotExist:
            obj = self.create(**kwargs)
            created = True
        return obj, created


class User(models.Model):
    """
    量潮用户基本账号

    代码风格：
      - 优先使用User.objects.create/update，不必要的情况下尽量不使用User.save方法。
      - 尝试过解耦Password字段相关逻辑，似乎无合适思路而放弃解耦。
    """
    # 字段
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='用户ID')
    email = models.EmailField(unique=True, db_index=True, default=None, blank=True, null=True, verbose_name="邮箱")
    phone_number = PhoneNumberField(unique=True, db_index=True, default=None, blank=True, null=True, verbose_name="电话号码")
    # 密码字段为加盐hash后的字符串
    password = models.CharField(default=set_unusable_password, max_length=128, verbose_name='密码')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='注册时间')
    is_active = models.BooleanField(default=True, verbose_name='账号已激活')

    objects = UserManager()

    # Django框架对用户模型的规定
    USERNAME_FIELD: str = 'id'  # 主要用作用户认证
    REQUIRED_FIELDS: list = ['is_active', 'created_at']

    # 可以识别用户的字段
    # 手动配置所有可以做db_index的字段。
    USERNAME_FIELD_ALTERNATIVES: list = ['phone_number', 'email']
    USERNAME_FIELD_LIST: list = [USERNAME_FIELD] + USERNAME_FIELD_ALTERNATIVES

    # 原始密码
    _password = None

    class Meta:
        verbose_name = '用户'
        ordering = ['created_at']

    # ----- 用户认证 -----
    @property
    def sub(self):
        """
        JWT sub claim
        :return:
        """
        return self.id

    @property
    def is_authenticated(self):
        """
        是否认证

        满足：
        - 账户激活。
        :return:
        """
        return self.is_active

    @property
    def is_anonymous(self):
        """
        非匿名用户
        :return:
        """
        return False

    @property
    def is_staff(self):
        """
        满足以下条件:
        1. 用户账户激活，即self.is_active字段为True。
        2. 员工账户存在，即self.staff存在。
        3. 员工账户激活，即self.staff.is_active为True。
        :return:
        """
        return self.is_active and hasattr(self, 'staff') and self.staff.is_active

    @property
    def is_superuser(self):
        """
        满足以下条件：
        1. 员工账户可用。
        2. 授权超级管理员。
        :return:
        """
        return self.is_staff and self.staff.is_superuser

    # ----- 密码 -----
    def set_password(self, raw_password=None):
        """
        密码加盐hash，raw_password=None等价于set_unusable_password方法
        :param raw_password:
        :return:
        """
        self.password = make_password(raw_password)
        self._password = raw_password
        return self.password

    def set_unusable_password(self):
        """
        空密码加盐加密
        :return:
        """
        self.password = set_unusable_password()
        return self.password

    def check_password(self, value) -> bool:
        """
        验证密码是否正确，空密码返回False
        :param value:
        :return: bool
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(value, self.password, setter)

    def has_usable_password(self):
        """
        验证密码是否为空
        :return: bool, True为非空，False为空
        """
        return is_password_usable(self.password)

    def save(self, *args, **kwargs):
        """
        重写save方法，对password机制做加工，但依然需要用户**手动处理set_password逻辑**，以方便用户直接操作底层机制。

        :param args:
        :param kwargs:
        :return:

        用例：
        ```
        >>> data = {...}
        >>> raw_password = data.pop('password', None)
        >>> instance = User(**data)
        >>> instance.set_password(raw_password)
        >>> instance.save()
        ```
        """
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
