# -*- coding: utf-8 -*-
"""
用户信息模型
"""
import uuid

from django.db import models

from users.models.user import User


class Gender(models.TextChoices):
    """
    性别选项

    代码风格：
      - 不使用bool类型是考虑到None（未知性别）和False（不是某一个性别）的情况意义完全不同，明确分类有利于数据分析。
    """
    # unknown = None, '未定义'
    male = 'male', '男'
    female = 'female', '女'


class UserProfile(models.Model):
    """
    用户信息

    TODO：
      - 接入头像字段，需要先接入COS作为Storage，详见：https://quanttide.coding.net/p/qtapp/requirements/issues/270/detail。
      - 接入地理位置字段。由于实现比较复杂，如无必要则不急接入。详见https://quanttide.coding.net/p/qtapp/requirements/issues/267/detail：
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='用户信息ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nick_name = models.CharField(max_length=64, default=None, verbose_name='昵称')
    birth_date = models.DateTimeField(default=None, verbose_name='生日')
    gender = models.IntegerField(default=None, choices=Gender.choices, verbose_name='性别')

    class Meta:
        verbose_name = "用户信息"

    @property
    def age(self):
        """
        年龄，通过生日和当前时间的差计算。
        :return:
        """
        pass
