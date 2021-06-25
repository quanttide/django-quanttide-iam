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
    员工身份认证，允许非员工访问safe methods。类似DRF官方的IsAdminUser。即所有人只读、员工可读写。

    TODO：完善测试
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (request.user and request.user.is_staff)


class IsAdminUserOrIsAuthenticatedReadOnly(BasePermission):
    """
    员工身份认证，允许认证用户访问safe methods。即用户只读、员工可读写。

    TODO：完善测试
    """
    def has_permission(self, request, view):
        return request.user and request.is_authenticated and (request.method in SAFE_METHODS or request.is_staff)
