===========================================
1、手写Spring MVC框架
===========================================

一、了解SpringMVC运行流程及九大组件
==================================================

1、SpringMVC的运行流程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

|image1|

1. 用户发送请求到前端控制器DispatcherServlet
#. DispatcherServlet收到请求调用HandlerMapping处理器。
#. 处理器映射器根据url找到具体处理器，生成处理器对象及处理器拦截器（如果有则生成）一并返回给DIspatcherServlet


参考文档
===========

微信公众号：  好好学java https://mp.weixin.qq.com/s/Nq_-8OFyQfe1ysNa6g3n6g



.. |image1| image:: ./image/19012801.webp