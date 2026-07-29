============
Spring
============

.. contents:: 目录
   :depth: 1
   :local:

单例Bean、单例模式、单例池
================================

- 单例模式：表示JVM中某个类的对象只会存在唯一一个。
- 单例Bean：并不表示JVM中只能存在唯一的某个类的Bean对象，如Spring单例是指一个Spring Bean容器(ApplicationContext)中仅有一个实例。
- 单例池：Spring单例是指一个Spring Bean容器(ApplicationContext)中仅有一个实例。

Spring事务传播机制
====================

https://mp.weixin.qq.com/s/S8RXcISJA0TdJuBsOXWPcQ

Spring在 `TransactionDefinition` 接口中规定了7种类型的事务传播行为。事务传播行为是Spring框架独有的事务增强特性，他不属于的事务实际提供方数据库行为。这是Spring为我们提供的强大的工具箱，使用事务传播行可以为我们的开发工作提供许多便利。
多个事务方法相互调用时，事务如何在这些方法间传播，方法A是一个事务的方法，方法A执行过程中调用了方法B，那么方法B有无事务以及方法B对事务的要求不同都会对方法A的事务具体执行造成影响，同时方法A的事务对方法B的事务执行也有影响，这种影响具体是什么就由两个方法所定义的事务传播类型所决定。

1. ``REQUIRED`` (Spring默认的事务传播类型) 如果当前没有事务，则自己新建一个事务，如果当前存在事务，则加入这个事务
2. ``SUPPORTS`` 当前存在事务，则加入当前事务，如果当前没有事务，就以非事务方法执行
#. ``MANDATORY`` 当前存在事务，则加入当前事务，如果当前事务不存在，则抛出异常。
#. ``REQUIRES_NEW`` 创建一个新事务，如果存在当前事务，则挂起该事务。
#. ``NOT_SUPPORTED`` 以非事务方式执行,如果当前存在事务，则挂起当前事务
#. ``NEVER`` 不使用事务，如果当前事务存在，则抛出异常
#. ``NESTED`` 如果当前事务存在，则在嵌套事务中执行，否则 ``REQUIRED`` 的操作一样（开启一个事务）


Bean作用域
====================

Spring中的Bean一般有以下几种作用域：

1. 单例(``Singleton``)作用域：每个Spring容器中只存在一个Bean实例，所有的请求都共享同一个实例。
2. 原型(``Prototype``)作用域：每次请求都会创建一个新的Bean实例。
#. 会话(``Session``)作用域：在Web环境中，每个会话(``Session``)都对应一个Bean实例，不同的会话之间共享不同的Bean实例。
#. 请求(``Request``)作用域：在Web环境中，每个请求(``Request``)都对应一个Bean实例，不同的请求之间共享不同的Bean实例。
#. 全局会话(``Global Session``)作用域：在 ``Portlet`` 环境中，每个全局会话(``Global Session``)都对应一个Bean实例，不同的全局会话之间共享不同的Bean实例。


ApplicationContext和BeanFactory有什么区别
======================================================

- ``BeanFactory`` 是Spring中非常核心的组件，表示Bean工厂，可以创建Bean、管理Bean。
- ``ApplicationContext`` 继承了 ``BeanFactory``，所以 ``ApplicationContext`` 拥有 ``BeanFactory`` 所有的特点，也是一个Bean工厂，但是 ``ApplicationContext`` 除开继承了 ``BeanFactory`` 之外，还继承了诸如 ``EnvironmentCapable``、 ``MessageSource``、 ``ApplicationEventPublisher`` 等接口，从而 ``ApplicationContext`` 还有获取系统环境变量、国际化、事件发布等功能，这是 ``BeanFactory`` 所不具备的