from rest_framework.permissions import BasePermission


class IsTenantAdmin(BasePermission):
    def has_permission(self, request, view):
        pass

