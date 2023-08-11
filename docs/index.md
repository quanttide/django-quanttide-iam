# 简介

## 修改声明式配置

设置`INSTALLED_APPS`增加应用`django_quanttide_idam`。

设置`AUTH_USER_MODEL`为`django_quanttide_idam.User`。

## 修改路由配置

配置登录注册API到项目路由配置文件`<project_name>/urls.py`。

```python
from django.urls import path, include

urlpatterns = [
    # ...,
    path('auth/', include('django_quanttide_idam.urls')),   
    # ...,
]
```
