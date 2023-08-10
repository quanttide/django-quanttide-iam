# -*- coding: utf-8 -*-
"""
微信用户模型
"""

import uuid

from django.db import models
from django.conf import settings

from .user import User


class WeChatUserManager(models.Manager):
    def get_by_unionid(self, unionid):
        """
        根据unionid查找用户
        :param unionid:
        :return:
        """
        return self.get(unionid=unionid)

    def get_by_openid(self, openid, client_label):
        """
        根据openid查找用户，需要指定client_label参数
        :param openid:
        :param client_label:
        :return:
        """
        return self.get(**{'openid_{client_label}'.format(client_label=client_label): openid})


class WeChatUser(models.Model):
    """
    绑定微信账号
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='微信用户ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='基本用户')
    unionid = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='微信UnionID')
    # 量潮科技
    openid_wxopen_quanttide = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='微信开放平台OpenID')
    openid_wxaccount_quanttide = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='量潮科技微信订阅号OpenID')
    # 量潮课堂
    openid_wxaccount_qtclass = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='量潮课堂服务号OpenID')
    openid_wxmp_qtclass = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='量潮课堂小程序OpenID')
    # 量潮数据服务
    openid_wxaccount_qtservices = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='量潮数据服务服务号OpenID')
    openid_wxmp_qtservices = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='量潮数据服务小程序OpenID')
    # 企业微信
    wecom_external_userid_quanttide = models.CharField(max_length=48, unique=True, blank=True, null=True, verbose_name='企业微信外部联系人UserID')

    objects = WeChatUserManager()

    class Meta:
        verbose_name = '微信账号'

    def get_unionid(self):
        """
        获取用户的unionid
        :return:
        """
        return self.unionid

    def get_openid(self, client_label):
        """
        获取用户的openid
        :param client_label:
        :return:
        """
        return getattr(self, 'openid_{client_label}'.format(client_label=client_label))

    def get_wecom_external_userid(self):
        """
        获取用户的企业微信外部联系人ID
        :return:
        """
        return self.wecom_external_userid_quanttide



