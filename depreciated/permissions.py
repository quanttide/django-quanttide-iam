# -*- coding: utf-8 -*-
"""
访问权限类
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """
    员工身份认证，允许非员工访问safe methods。类似DRF官方的IsAdminUser。即所有人只读、员工可读写。
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (request.user and request.user.is_staff)


class IsAdminUserOrIsAuthenticatedReadOnly(BasePermission):
    """
    员工身份认证，允许认证用户访问safe methods。即用户只读、员工可读写。
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (request.method in SAFE_METHODS or request.user.is_staff)
