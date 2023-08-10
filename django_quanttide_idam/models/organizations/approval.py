"""
审批模型

TODO：设计审批流权限方案。主要围绕审批者和抄送者、审批规则等设计。
"""

import uuid

from django.db import models


class ApprovalFlow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='审批流ID')
    name = models.SlugField(max_length=64, verbose_name='审批流标识')
    verbose_name = models.CharField(max_length=256, verbose_name='审批流名称')

    class Meta:
        verbose_name = '审批流'


class Approval(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='审批单ID')
    applicant = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='申请者')
    flow = models.ForeignKey(ApprovalFlow, on_delete=models.CASCADE, verbose_name='审批流')

    class Meta:
        verbose_name = '审批单'
