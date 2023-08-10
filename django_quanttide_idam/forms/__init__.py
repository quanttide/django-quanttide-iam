"""
Django Forms for IdAM

Ref:
  - https://docs.djangoproject.com/en/4.1/topics/forms/
  - https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#modelform
"""

from django_quanttide_idam.forms.identification.signup import PasswordSignUpForm
from django_quanttide_idam.forms.identification.login import PasswordLoginForm
from django_quanttide_idam.forms.identification.vcode import VCodeLoginForm


__all__ = [
    "PasswordSignUpForm",
    "PasswordLoginForm",
    "VCodeLoginForm",
]
