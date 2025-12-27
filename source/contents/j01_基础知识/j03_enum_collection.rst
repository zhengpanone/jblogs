======================
枚举、集合
======================

枚举
==========================

枚举使用技巧
--------------------------

枚举可以有自己的方法

.. literalinclude:: ./code/j03_enum_collection/enum_demo/MemberType1.java
    :language: java

.. literalinclude:: ./code/j03_enum_collection/enum_demo/PriceCalculator.java
    :language: java

优化版

- 字段 + 统一实现
- 枚举只描述“数据”，行为一致
- 去掉匿名类

.. literalinclude:: ./code/j03_enum_collection/enum_demo/MemberType2.java
    :language: java

枚举 + 策略接口

.. literalinclude:: ./code/j03_enum_collection/enum_demo/DiscountStrategy.java
    :language: java

.. literalinclude:: ./code/j03_enum_collection/enum_demo/MemberType3.java
    :language: java


集合
==========================


.. note::

 - 栈: 先进先出

  - 存储局部变量

  局部变量：定义在方法声明上和方法中的变量

 - 堆

  - 存储new 出来的数组会对象

 - 方法区

  - 面向对象部分

 - 本地方法区

  - 和系统相关

 - 寄出器

  - 给CPU使用

包装类型和基本类型的使用

.. note::

 包装类型和基本类型在使用过程中是可以互相转换，但是两者所产生的内存区域是完全不同，基本类型数据产生和处理都在栈中处理，包装类型是对象，是在堆中产生实例。在集合类对象，有对象方面的处理适用包装类型，其他处理适用基本类型

.. note::

 - 多线程在未发生线程安全前提下应尽量使用HashMap、ArrayList
   HashTable、Vector等使用了同步机制，降低了性能。

