"""
Ref:
  - https://github.com/pycasbin/django-casbin/tree/master/casbin_middleware
"""
from rest_framework.permissions import BasePermission
import casbin


class IsOrganizationAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        enforcer = casbin.Enforcer('./organization_model.conf', './organization_policy.csv')
        return enforcer.enforce(request.user, obj, request.method)
