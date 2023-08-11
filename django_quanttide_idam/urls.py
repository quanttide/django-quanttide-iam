"""
Endpoint配置

开发者笔记：
  - 根据领域驱动设计的要求，把他们定义为"Service"，对鉴权这个无状态的"动作"建模。

参考资料：
  - OAuth2协议文档：https://datatracker.ietf.org/doc/html/rfc6749#section-3
  - 《领域驱动设计：软件核心复杂性应对之道》
"""

from django.urls import path

from django_quanttide_idam.views import PasswordSignUpView, PasswordLoginView, VCodeLoginView
# from django_quanttide_idam.views import PublicKeyView


app_name = 'django_quanttide_idam'

urlpatterns = [
    path('signup/', PasswordSignUpView.as_view(), name='password-sign-up'),
    path('login/', PasswordLoginView.as_view(), name='password-login'),
    path('login-verification_code/', VCodeLoginView.as_view(), name='verification_code-login'),
    # path('public-key/', PublicKeyView.as_view(), name='public-key'),
]
