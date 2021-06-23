# -*- coding: utf-8 -*-
"""
自定义用户权限类。

DRF已经实现：
  - AllowAny: 任何用户
  - IsAuthenticated: 认证用户权限
  - IsAuthenticatedOrReadOnly: 认证用户允许非安全方法
  - IsAdminUser: 员工权限
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """
    员工身份认证，允许非员工访问safe methods。类似DRF官方的IsAdminUser。
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and request.user and request.user.is_staff
