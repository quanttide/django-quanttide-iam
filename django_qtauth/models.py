# -*- coding: utf-8 -*-

from django.db import models


class User(models.Model):
    """
    用户数据统一存储在用户服务，此处只是为了在Django服务内方便标记用户身份。
    """
    user_id = None
