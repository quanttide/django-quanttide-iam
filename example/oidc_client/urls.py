# -*- coding: utf-8 -*-

from django.urls import path

from .views import oidc_discover_view


app_name = 'oidc_client'

urlpatterns = [
    path('oidc_config/', oidc_discover_view, name='oidc_config'),
]
