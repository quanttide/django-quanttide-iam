---
title: Authentication类
author: 张果
date: 2021-08-09
---

# Authentication类

## 架构设计原则

DRF框架支持多个`Authentication`类同时配置给API，只要有一个验证通过即可通过用户认证（authentication）流程。同时考虑`Authentication`类应当根据开发者接入的需求划分，明白接入目标而不需要关心具体逻辑。基于以上原因，计划对CIAM和EIAM分别根据协议划分`Authentication`类，在类内部实现对不同模式的不同阶段的解析和验证。（PS：如果有必要也可根据协议模式拆分为不同的类。）

## `CiamOidcAuthentication`类

主要用以认证普通用户，可使用账号密码、验证码、QQ、微信等。

## `EiamOidcAuthentication`类

主要用以认证员工用户，可使用账号密码、验证码、企业微信等。

## `EiamOAuth2Authentication`类

主要用于Resource Server模式下通过SecretID和SecretKey验证可信第一方应用（比如CI流水线）。