# 鉴权协议实现

自顶层到底层为：

- qtuser：实现鉴权API。
- drf-remote-auth：提供鉴权协议和鉴权数据模型等Django和DRF工具。

## drf-remote-auth

视图函数的划分类似于Firebase，分为：

- odic协议
- login/register

由于不知道Firebase怎么做的，所以不清楚他们之间是完全独立还是需要耦合。
