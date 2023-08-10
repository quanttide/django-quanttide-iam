# 分层设计

遵循领域驱动设计的分层设计实践。

基于领域驱动设计（Domain-Driven Design, DDD）的思想，我们把本服务内的Django应用从顶层至底层分为两层：

- 应用层，基于不同的鉴权协议划分，目前是OpenID Connect。
- 领域层，以业务逻辑需求划分为用户（users）、用户信息（profiles）、密钥（secretkey）、员工（staff）、团队（teams）、协作者（collaborators）、会员（vip）等身份。

应用层对外暴露API，需要调用本应用和其他数据模型应用的Django类。其中：

- 鉴权应用需要调用几乎所有数据模型层的数据，从而为外界提供统一的鉴权API。
- 用户信息应用需要调用本应用的基本用户信息，以及除了用户应用（users）以外的各个应用内的补充信息。

领域层分领域建模，每个应用划分了自建身份和第三方身份为不同的模块，通过建立他们的关联关系来匹配同一个用户的不同账号。 比如，在用户应用（users），自建用户（user）和微信用户（wechatuser）被划分为不同的模块，微信用户通过外键关联自建用户来匹配。 关联关系是业务逻辑的目标，独立的模块是为了方便独立迭代的工程管理。

## 应用层

计划使用OpenID Connect协议，所以需要一个OpenID Connect Provider。

计划对外暴露以下API：

- 登录：login和logout。
- 鉴权（auth）：verify和refresh接口。
- 用户信息（profile）：根据OpenID的userinfo标准。
- 辅助API：比如vcode等。

## 领域层

以关键领域模型为单位分离服务内Django应用。包括

- 基本用户应用
- 员工应用
- 合作者应用
- 密钥应用
