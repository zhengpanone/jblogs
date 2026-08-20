===================
RabbitMQ
===================

RabbitMQ 是一个开源的消息队列系统，用于在应用程序之间传递消息。以下是 RabbitMQ 的基本概念和使用场景：

1. **消息队列**：RabbitMQ 使用队列来存储消息，生产者将消息发送到队列，消费者从队列中获取消息进行处理。

2. **生产者（Producer）**：负责生成消息并将其发送到 RabbitMQ 队列。

3. **消费者（Consumer）**：负责从 RabbitMQ 队列中获取消息并进行处理。

4. **交换机（Exchange）**：用于路由消息到不同的队列。RabbitMQ 支持多种交换机类型，如 direct、fanout、topic 等。

5. **绑定（Binding）**：定义交换机和队列之间的关系，指定消息如何路由。

6. **持久化**：确保消息在服务器重启后仍然存在，通过设置队列和消息的持久化属性实现。

7. **确认机制**：确保消息被成功处理，通过消息确认机制实现。

RabbitMQ 的主要应用场景包括：

- **异步处理**：将耗时操作异步化，提高系统响应速度。
- **解耦**：将不同服务之间的耦合度降低，提高系统的可维护性。
- **流量削峰**：在高并发场景下，通过消息队列缓冲请求，防止系统过载。
- **分布式系统**：支持分布式环境下的消息传递和处理。

RabbitMQ 的安装和配置相对简单，可以通过包管理器或源码编译进行安装。配置文件通常位于 `/etc/rabbitmq/` 目录下。


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
-------------------------------------

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
----------------------------------------

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
-----------------------------------------

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