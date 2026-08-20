====================
Spring Cloud
====================

.. contents:: 目录
   :depth: 1
   :local:
   
为什么Feign第一次调用耗时很长
===================================

Feign 第一次调用耗时很长，通常是因为**第一次请求触发了很多“懒加载”和连接初始化操作**，后续调用复用资源，所以明显变快。

常见原因按概率排序：

1. **Feign Client 初始化**

   * 第一次真正调用时，Feign 可能才完成代理对象、Encoder、Decoder、Contract 等组件的初始化。
   * Spring Cloud OpenFeign 场景下尤其常见。

2. **HTTP 连接建立**

   * 第一次请求需要建立 TCP 连接。
   * 如果是 HTTPS，还会增加 TLS/SSL 握手。
   * 后续请求通常复用 HTTP 连接池，因此速度明显提升。

3. **DNS 解析**

   * 第一次访问目标服务时可能发生 DNS 查询。
   * DNS 缓存生效后，后续请求会快很多。

4. **服务发现耗时**
   如果使用了 `Nacos`、`Eureka`、`Consul` 等：

   * 第一次可能需要获取服务实例列表
   * 进行负载均衡
   * 初始化相关缓存

5. **连接池预热**
   如果 HTTP Client 使用连接池，第一次没有可复用连接，需要创建连接；后续直接复用。

6. **目标服务本身冷启动**
   Feign 第一次请求慢，**不一定是 Feign 慢**。可能是被调用服务：

   * JVM 类加载
   * Spring Bean 懒加载
   * 数据库连接池初始化
   * Redis 连接建立
   * JIT 编译
   * 缓存加载

7. **代理 / 网关 / 网络设备**
   如果链路是：

   `服务A → Feign → Gateway/Nginx → 服务B`

   第一次调用可能还会触发连接建立、TLS 握手或网关连接池初始化。


怎么快速定位
---------------------

建议把一次 Feign 请求拆成几个阶段观察：

.. code-block:: text

  Feign 调用开始
      ↓
  服务发现耗时？
      ↓
  DNS 耗时？
      ↓
  TCP/TLS 建连耗时？
      ↓
  HTTP 请求发送
      ↓
  服务B处理耗时？
      ↓
  响应返回


如果你发现：

* **第一次 2 秒，第二次 10ms** → 大概率是连接池 / DNS / TLS / 服务发现
* **每次都 2 秒** → 大概率是服务B处理慢、网络慢或超时重试
* **第一次 10 秒左右，之后很快** → 重点检查 Feign / Ribbon / LoadBalancer / 服务发现 / 连接超时
* **第一次调用偶发几十秒** → 重点检查 DNS、连接超时、IPv6、代理、重试机制

我建议你优先检查
---------------------

.. code-block:: yaml

  logging:
    level:
      your.package.feign: DEBUG


然后配合：

* Feign 日志
* Micrometer / Actuator
* SkyWalking / Zipkin / Jaeger
* Nacos/Eureka 服务发现日志
* HTTP Client 连接池指标


