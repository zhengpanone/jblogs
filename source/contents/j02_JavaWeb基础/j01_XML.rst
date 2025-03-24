==============
XML
==============

- XML全称 EXtensible Markup Language,可扩展标记语言
- 用途:配置描述文件、保存数据、网络传输

XML重点知识
====================

.. csv-table:: XML重点知识
   :widths: 90,100
   :file: table/j01_XML/XML重点知识.csv
   :encoding: utf-8
   :align: left

XML语义约束有两种定义方式:**DTD**与**XML Schema**


DTD
===============

- DTD(Document Type Definition,文档类型定义)是一种简单易用的语义约束方式。
- DTD文件的扩展名为.dtd

.. literalinclude:: ./code/j01_XML/hr.dtd
    :encoding: utf-8
    :language: dtd
    :linenos:

DTD定义节点
>>>>>>>>>>>>>>>>>>>

- 利用DTD中的<!ELEMENT>标签,可以定义XML文档中允许出现的节点及数量

  - 定义hr节点下只允许出现1个employee子节点 
   
    - **<!ELEMENT hr (employee)>** 
  
  - employee节点下必须包含以下四个节点,且按顺序出现 
 
    - **<!ELEMENT employee (name,age,salary,department)>**

  - 定义name标签体只能是文本,#PCDATA代表文本元素
  
    - **<ELEMENT name (#PCDATA)>**

DTD定义节点数量
>>>>>>>>>>>>>>>>>>>

- 如某个子节点需要多次重复出现,则需要在子节点后增加相应的描述符
  
  - hr节点下最少出现一个employee子节点
    
    - **<!ELEMENT hr (employee+)>**
  
  - hr节点下可出现0-n个employee子节点

    - **<!ELEMENT hr (employee*)>**
 

  - hr节点下最多出现1个employee子节点

    - **<!ELEMENT hr (employee?)>**

XML引用DTD文件
>>>>>>>>>>>>>>>>>>

- 在XML中使用<!DOCTYPE> 标签来引用DTD文件

书写格式:
  <!DOCTYPE 根节点 SYSTEM "dtd文件路径">
示例:
  <!DOCTYPE hr SYSTEM "hr.dtd">

创建DTD文件
>>>>>>>>>>>>>>>>>>
