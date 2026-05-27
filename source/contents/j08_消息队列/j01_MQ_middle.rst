===========
消息队列
===========

消息队列中间件是分布式系统中重要的组件，主要解决应用耦合，异步消息，流量削锋等问题。实现高性能，高可用，可伸缩和最终一致性架构。是大型分布式系统不可缺少的中间件。

使用较多的消息队列有ActiveMQ，RabbitMQ，ZeroMQ，Kafka，MetaMQ，RocketMQ等。


交换机
=================

主流消息队列的交换机对比
----------------------------

.. list-table:: RabbitMQ 与其他消息队列路由机制对比
   :header-rows: 1
   :widths: 20 30 25 25
   
   * - 消息队列
     - 对应概念
     - 核心路由逻辑
     - 与 RabbitMQ 的差异
   * - **RabbitMQ**
     - **Exchange**
     - 严格的路由键（Routing Key）匹配、通配符、广播
     - 标准，功能最丰富，支持四种明确模式
   * - **Kafka**
     - **Topic** (分区)
     - 基于 Key 的哈希路由（到分区）或广播
     - 无直接交换机，Topic 本身就是逻辑分类，路由逻辑更简单
   * - **RocketMQ**
     - **Topic** + Tag
     - 主题 + 标签（二级过滤）
     - 类似 Direct/Topic 的混合体，Tag 类似 Routing Key
   * - **ActiveMQ**
     - **Virtual Topic / Composite Queue**
     - 通配符订阅
     - 功能与 RabbitMQ 的 Topic Exchange 最接近
   * - **Pulsar**
     - **Topic (分层)**
     - 多租户命名空间下的路由
     - 设计理念更接近 Kafka，但增加了灵活的路由策略
   * - **Redis Pub/Sub**
     - **Channel**
     - 纯广播（无路由键）
     - 仅相当于 RabbitMQ 的 **Fanout Exchange**

各消息队列实现细节
----------------------------

1. Kafka：Topic **即路由**

Kafka 没有显式的“交换机”组件。**Topic** 承担了消息分类的角色，生产者直接指定 Topic 名称发送消息。

**路由方式**：主要通过消息的 Key进行哈希计算，决定消息进入 Topic 的哪个 Partition（分区），从而实现消息的顺序性和负载均衡。

**对比** RabbitMQ：Kafka 的 Topic 更像是一个“存储流”，其路由逻辑（分区策略）比 RabbitMQ 的 Exchange 更底层、更固定。

2. RocketMQ：Topic + Tag 二级过滤

RocketMQ 使用 Topic 作为一级分类，Tag 作为二级过滤条件。

**路由方式**：生产者发送消息时指定 Topic和 Tag，消费者通过订阅 Topic:Tag（支持通配符 \*）来过滤消息。

**类比** RabbitMQ：Topic类似一个 Direct Exchange，而 Tag类似 Routing Key 的进一步细化，非常灵活。

3. ActiveMQ：Virtual Topic 与 Composite Destinations

ActiveMQ 提供了更接近 RabbitMQ 的灵活路由能力。

Virtual Topic：允许消费者队列以通配符形式订阅主题（如 Consumer.A.VirtualTopic.>），实现类似 Topic Exchange 的发布/订阅模式。

Composite Destinations：可以将多个物理队列组合成一个逻辑队列，实现消息的复制和分发（类似 Fanout）。

4. Redis Pub/Sub：极简的 Channel

Redis 的发布订阅（Pub/Sub）模型非常简单，Channel 就是其路由单元。

**路由方式**：纯广播。生产者发布到 Channel，所有订阅该 Channel 的消费者都会收到消息。

**局限性**：它没有持久化、没有队列、没有路由键，功能上仅相当于 RabbitMQ 的 Fanout Exchange，且消息若无人订阅则直接丢失。


结论
-------------------

RabbitMQ 的 Exchange 是其 AMQP 协议实现中最具特色的设计，提供了最精细的路由控制。而其他消息队列（如 Kafka、RocketMQ）更侧重于高吞吐和流式处理，它们的“交换机”逻辑通常被简化为 Topic 这一层抽象，路由策略相对固定（如哈希分区）。


RabbitMQ 交换机（Exchange）模式
===============================

交换机是 RabbitMQ 的核心组件，负责接收生产者发送的消息，并根据特定规则（绑定规则）将消息投递到一个或多个队列中。

交换机核心模式概览
----------------------

.. list-table:: 交换机模式对比
   :header-rows: 1
   :widths: 20 20 30 30
   
   * - 模式
     - 类型名称
     - 路由逻辑
     - 适用场景
   * - 直连模式
     - Direct
     - 精确匹配 ``routing_key``
     - 精确路由，如订单状态更新、特定任务分发
   * - 扇形模式
     - Fanout
     - **广播**，忽略 ``routing_key``，发送给所有绑定队列
     - 广播通知，如群发消息、系统公告、缓存刷新
   * - 主题模式
     - Topic
     - 模糊匹配 ``routing_key``（支持通配符 ``*`` 和 ``#``）
     - 动态路由，如日志分级（``error.*``）、多维度消息
   * - 头模式
     - Headers
     - 不依赖 ``routing_key``，匹配 ``headers`` 属性（键值对）
     - 复杂条件路由，如基于协议版本、消息格式过滤


Direct Exchange（直连交换机）
----------------------------

**特点**
   完全匹配，消息的 ``routing_key`` 必须与 Binding Key 完全一致

- **一对一**：一个队列绑定一个 key
- **多绑定**：多个队列绑定同一个 key（类似广播给特定组）

**示例代码**

.. code-block:: python

   # 生产者：发送到 key 为 "order.paid" 的队列
   channel.basic_publish(
       exchange='order_exchange', 
       routing_key='order.paid', 
       body=message
   )

   # 消费者：队列绑定 key "order.paid"
   channel.queue_bind(
       queue='payment_queue', 
       exchange='order_exchange', 
       routing_key='order.paid'
   )

Fanout Exchange（扇形交换机）
-----------------------------

**特点**
   **广播**，将消息发送到所有绑定到该交换机的队列，完全忽略 ``routing_key``

**示例代码**

.. code-block:: python

   # 生产者：无需指定 key（即使指定了也会被忽略）
   channel.basic_publish(
       exchange='user_registered_fanout', 
       routing_key='',  # 可为空
       body=message
   )

   # 消费者：队列无需绑定 key
   channel.queue_bind(
       queue='email_queue', 
       exchange='user_registered_fanout'
   )
   channel.queue_bind(
       queue='profile_queue', 
       exchange='user_registered_fanout'
   )

Topic Exchange（主题交换机）
---------------------------

**特点**
   **模式匹配**，使用通配符进行灵活路由

- ``*`` (星号)：匹配**一个**单词（如 ``order.*`` 匹配 ``order.paid``，但不匹配 ``order.paid.email``）
- ``#`` (井号)：匹配**零个或多个**单词（如 ``order.#`` 匹配 ``order.paid`` 和 ``order.paid.email``）

**示例代码**

.. code-block:: python

   # 生产者：发送不同级别的日志
   channel.basic_publish(exchange='logs', routing_key='app.error', body=error_log)
   channel.basic_publish(exchange='logs', routing_key='app.info', body=info_log)

   # 消费者：绑定模式
   # Q1 接收所有错误日志
   channel.queue_bind(queue='error_queue', exchange='logs', routing_key='*.error')
   # Q2 接收所有以 app 开头的日志
   channel.queue_bind(queue='app_queue', exchange='logs', routing_key='app.#')

Headers Exchange（头交换机）
---------------------------

**特点**
   不依赖 ``routing_key``，而是根据消息的 ``headers`` 属性进行匹配

匹配规则分为 ``x-match`` 两种：

- ``all``：必须匹配所有键值对（逻辑与）
- ``any``：匹配任意一个键值对（逻辑或）

**示例代码**

.. code-block:: python

   # 生产者：在 headers 中设置属性
   properties = pika.BasicProperties(headers={'format': 'json', 'version': '1.0'})
   channel.basic_publish(
       exchange='headers_exchange',
       routing_key='',  # 通常为空
       body=message,
       properties=properties
   )

   # 消费者：绑定 headers（x-match 默认为 all）
   args = {'format': 'json', 'version': '1.0', 'x-match': 'all'}
   channel.queue_bind(
       queue='json_v1_queue',
       exchange='headers_exchange',
       arguments=args
   )

默认交换机（AMQP Default）
------------------------------

RabbitMQ 自带一个**无名（Nameless）默认交换机**，类型为 Direct。

- 每个新创建的队列会自动以**队列名**作为 ``routing_key`` 绑定到它
- 使用空字符串作为交换机名表示使用默认交换机

.. code-block:: python

   # 消息会直接进入名为 "my_queue" 的队列
   channel.basic_publish(
       exchange='',  # 空字符串代表默认交换机
       routing_key='my_queue',  # 必须等于队列名
       body=message
   )

选型指南
---------------------

.. list-table:: 交换机选型指南
   :header-rows: 1
   :widths: 60 40
   
   * - 你的需求
     - 推荐模式
   * - "把这个消息发给**那个**特定的队列"
     - **Direct**
   * - "把这个消息发给**所有**感兴趣的队列"
     - **Fanout**
   * - "把这个消息发给符合**某类模式**的队列"（如：``user.*.created``）
     - **Topic**
   * - "根据消息的**复杂属性**（如版本、格式）来路由"
     - **Headers**






