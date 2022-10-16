# 鉴权模式

三步（Auth Code Grant）：

1. 客户端发请求，服务端重定向到login，加一个临时key。
2. 发登录请求。
3. authorization code和鉴权服务器换aceess token

Google Identity Platform提供，但不清楚怎么登录注册。

两步（Implict Grant）：

2和3合并。

Google Identity Platform也提供，同样不清楚怎么登录注册。

一步（Password Grant）：

直接拿IDToken。

Firebase/Google Identify Platform的用户密码登录像这种，可是OIDC协议不支持Password Grant。
十分疑惑他们是放弃或者拓展了标准协议，还是我对他们SDK的解析不够透彻。
