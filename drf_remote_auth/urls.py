"""
Endpoint配置

开发者笔记：
  - 根据领域驱动设计的要求，把他们定义为"Service"，对鉴权这个无状态的"动作"建模。

参考资料：
  - OAuth2协议文档：https://datatracker.ietf.org/doc/html/rfc6749#section-3
  - 《领域驱动设计：软件核心复杂性应对之道》
"""

from django.urls import path

from drf_remote_auth.settings import drf_remote_auth_settings
from docs.depreciated.views.oauth2 import *


urlpatterns = []

# OAuth2协议
if drf_remote_auth_settings.OAUTH2:
    urlpatterns += [
        path('authorize/', AuthorizationView, name='oauth2-authorization')
    ]
