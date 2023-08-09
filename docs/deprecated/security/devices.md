---
author: 张果
created_date: 2022-02-09
note: 本文是21年初的旧稿整理，很多情况已经发生了比较大的变化，需要重新讨论制定。
---

# 设备安全

多设备登录为必须特性，我们可能需要量潮课堂的用户可以同时使用两三个设备无缝学习，甚至可能需要两三个设备同时使用以实现一边看视频一边写代码的效果。

由于设计的认证机制为JWT，以计算而非缓存形式处理，因此**比较难在不增加其他机制的前提下，让如下约束机制发挥作用**。换句话说，基于JWT机制的设备数量约束比较难实现。

但我们无法放弃JWT机制，也不应当缓存JWT来实现类似于Session的效果。一方面，这会影响多设备登录实现机制；另一方面，云原生应用应当是无状态的，JWT机制可以很好地保证服务端的无状态，以方便未来可能的不停机迁移（如果缓存了状态，缓存则无法清空时不影响用户使用）。

## 安全规则

**需要大量收集用户数据迭代优化安全算法。**

- 约束同类型设备最多一个。服务端可以约束同类型设备（mobile/tablet/desktop/web）只能存在一个。
- 限制最大设备登录数量。遵循云点播Key防盗链最多3 or N 个设备的限制，防止付费用户登录多个用户设备使用。
- 通过IP验证是否为同一用户。服务端还可以通过检验设备IP来查看是否被多个人使用，通过验证码防止风险访问。

## 基于设备唯一的JWT验证机制

核心机制是，通过存储的设备信息来进行验证，实现一个安全算法即可。由于安全算法被解耦，所以**可以迭代**。
安全算法可通过以下分块拆分，每个算法之间都是and的关系，即必须全部通过才可验证成功。

- 对于同类设备验证，增加一个**last_login**字段即可，只允许last_login最靠后的设备可通过验证；
- 同类设备约束已经可以隐含实现设备数量限制；
- IP约束同样也包含在上述约束里。