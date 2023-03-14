=========================
23. 函数式接口&Stream流
=========================


函数式接口
==============

函数式接口: 有且仅有一个抽象方法的接口

Java中函数式编程体现就是Lambda表达式, 所有函数式接口就是可以适用于Lambda使用的接口,只用确保接口中有且仅有一个抽象方法,Jav中的Lambda才能顺利进行推导

定义函数式接口
>>>>>>>>>>>>>>>>>>>>>>

在接口上添加 `@FunctionalInterface` 标识这个接口是 **函数式接口** 

.. literalinclude:: ./code/23函数式接口和Stream流/functionInterface/MyInterface.java
    :encoding: utf-8
    :language: java
    :linenos:

.. literalinclude:: ./code/23函数式接口和Stream流/functionInterface/MyInterfaceDemo.java
    :encoding: utf-8
    :language: java
    :linenos:

函数式接口作为方法的参数
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/23函数式接口和Stream流/functionInterface/RunnableDemo.java
    :encoding: utf-8
    :language: java
    :linenos:

函数式接口作为方法的返回值
>>>>>>>>>>>>>>>>>>>>>>>>>>>






