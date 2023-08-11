from django.test import TestCase

from django_quanttide_idam.permissions.permissions import *


class IsAdminUserOrReadOnlyTestCase(TestCase):
    permission_class = IsAdminUserOrReadOnly

    def test_admin_user(self):
        pass

    def test_authenticated_user(self):
        pass

    def test_anonymous_user(self):
        pass


class IsAdminUserOrIsAuthenticatedReadOnly(TestCase):
    permission_class = IsAdminUserOrIsAuthenticatedReadOnly

    def test_admin_user(self):
        pass

    def test_authenticated_user(self):
        pass

    def test_anonymous_user(self):
        pass
