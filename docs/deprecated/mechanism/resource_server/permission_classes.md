---
title: 用户权限类
author: 张果
date: 2021-08-09
---

# 用户权限类

## 可选权限类

DRF官方权限类模块`rest_framework.permissions`实现的Permission类都可用，详见https://www.django-rest-framework.org/api-guide/permissions/。


## 默认权限类

### 前中台应用

`rest_framework.permissions.IsAuthenticationed`即可，部分公开API需要设置为`rest_framework.permissions.AnyAllowed`。

### 后台应用

默认`rest_framework.permissions.IsAdminUser`即可。

此外，默认管理层（T5+）拥有系统管理员权限（is_superuser=True），各个部门拥有其所属子应用的分级管理员权限（is_<app>_superuser=True）。
