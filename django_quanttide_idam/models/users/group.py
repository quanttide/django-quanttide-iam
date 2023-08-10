"""
用户组
"""

import uuid

from django.db import models

from users.models import User


class UserGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='用户组ID')
    name = models.CharField(max_length=64, unique=True, db_index=True, verbose_name='用户组名称')
    verbose_name = models.CharField(max_length=128, default=None, blank=True, null=True, verbose_name='用户组详细名称')
    users = models.ManyToManyField(User, verbose_name='用户')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = '用户组'
