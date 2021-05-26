# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class IsStaffAuthenticated(BasePermission):
    """
    员工身份认证
    """
    pass
