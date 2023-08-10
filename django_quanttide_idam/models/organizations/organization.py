"""
组织

Ref:
  - https://github.com/bennylope/django-organizations/blob/master/src/organizations/abstract.py
"""
import uuid

from django.db import models


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='组织ID')
    name = models.CharField(max_length=128, unique=True, verbose_name='组织标识')
    verbose_name = models.CharField(max_length=256, default=None, null=True, blank=True, verbose_name='组织名称')

    class Meta:
        verbose_name = '组织'


class OrganizationMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='组织成员ID')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                     related_name='members', verbose_name='关联组织')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='organization_members',
                             verbose_name='关联用户')

    class Meta:
        verbose_name = '组织成员'
        ordering = ('organization', 'user')
        unique_together = ('organization', 'user')


class OrganizationOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='组织所有者ID')
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='owner', verbose_name='关联组织')
    member = models.OneToOneField(OrganizationMember, on_delete=models.CASCADE,
                                  related_name='owners', verbose_name='关联组织成员')

    class Meta:
        verbose_name = '组织所有者'


class OrganizationMemberProfile(models.Model):
    """
    TODO: 设计并实现字段。
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='组织成员信息ID')
    member = models.OneToOneField(OrganizationMember, on_delete=models.CASCADE,
                                  related_name='profile', verbose_name='关联组织成员')
