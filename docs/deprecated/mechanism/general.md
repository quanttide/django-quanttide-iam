---
title: 量潮用户鉴权机制
author: 张果
created_at: 2021-08-09
updated_at: 2022-07-15
---

# 量潮用户鉴权机制

本部分文档统一说明系统层面的用户鉴权（Authorization）机制。

## 架构设计原则

使用OAuth2或OpenID Connect（以下简称OIDC协议）标准鉴权协议通信，基于OIDC协议的自定义claims（或OAuth2协议的自定义scope）制定和实现自定义权限验证规则。

## 鉴权服务端

使用腾讯云的数字身份管控平台（IDAM）的公众版（CIAM）和员工版（EIAM）作为鉴权服务端。详见：
- 公众版：https://cloud.tencent.com/document/product/1441
- 员工版：https://cloud.tencent.com/document/product/1442

云平台暴露OAuth2和OIDC鉴权服务端API。在控制台设置自定义鉴权用的claims（或者scope）并和客户端开发者约定使用方式。

## 资源服务端

在DRF框架下包括用户认证（Authentication）和用户权限（Permission）两个部分。鉴权客户端的Django插件分为这两层设计：
- 协议层：`Authentication`类负责根据标准协议鉴权和解析用户权限字段。
- 框架层：`Permission`类按照Django框架规定的`AuthUser`类鉴权字段验证权限。

两层之间的转换通过`AuthUser`类（`Model`类的子类）和`Serializer`类，`Authentication`类调用`Serializer`类解析服务端设置的用于鉴权的claims（或者scope）并转换成Django框架的`AuthUser`类鉴权字段，`Permission`类基于自定义的使用规则验证权限。

## 客户端

暂未设计。