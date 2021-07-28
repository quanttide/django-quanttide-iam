# -*- coding: utf-8 -*-
"""
Test validators for model fields.

Author: Guo Zhang(zhangguo@quanttide.com)
Contributors:
    -
"""

from django.test import SimpleTestCase
from drf_remote_auth.validators import DRFIntrospectTokenValidator


class DRFIntrospectTokenValidatorTestCase(SimpleTestCase):
    """
    TestCase for DRFIntrospectTokenValidator.
    """
    def test_introspect_token(self):
        pass
        # validator = DRFIntrospectTokenValidator()
        # validator.introspect_token()
