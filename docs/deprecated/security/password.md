# 密码安全

使用Django默认的加盐hash的方式存储hash以后的密码。

在这样的机制下，服务端也不知道用户设置的密码是什么，仅仅可以验证密码是否正确，可以保护用户隐私。

此方案不使用Django项目的SECRET_KEY，因此可以保证不会因为更换SECRET_KEY导致密码数据不可用。

具体可以参考Django文档密码相关资料。