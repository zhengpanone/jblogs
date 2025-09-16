================
Maven
================

常用命令
==============

``clean`` ``compile``  ``test``  ``package``  ``install``  ``deploy`` 整个流程是一个默认生命周期

加快Maven项目创建
======================

每次创建项目时， IDEA 要使用插件进行创建，这些插件当你创建新的项目时，它每次都会去中央仓库下载，这样
使得创建比较慢。应该创建时，让它找本地仓库中的插件进行创建项目。
在 IDEA 的 Settings 窗口的 ``Build, Execution, Deployment > Build Tools > Maven > Runner`` 中对 ``VM Option`` 设置
为 ``-DarchetypeCatalog=internal``

idea 添加Live Templates
=============================

Settings>Editor>Live Templates
配置templates 选值应用

解决jar包冲突
===================

1. 第一声明优先原则: 那个jar包的坐标在前面,这个jar包就是先声明,先声明的jar包可以优先进入项目

#. 路径近者优先原则: 直接依赖路径比传递依赖路径近,最终项目进入的jar包会是路径近的直接依赖包

#. 直接排除法: 当我们要排除某个jar包下的依赖包,在配置excusions标签的时候,内部可以不写版本号

#. 统一管理jar包版本

**dependencyManagement标签可以锁定jar版本,为了防止传递依赖jar被直接依赖jar覆盖,可以锁定传递依赖jar版本**


Maven打包跳过测试的4种方式
=================================

1、命令行方式跳过测试
>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

    mvn package -DskipTests=true

``-DskipTests=true`` ，不执行测试用例，但编译测试用例类生成相应的class文件至 ``target/test-classes`` 下。

.. code-block:: shell

    mvn package -Dmaven.test.skip=true

``-Dmaven.test.skip=true`` ，不执行测试用例，也不编译测试用例类。

- ``-DskipTests=true`` 和 ``-Dmaven.test.skip=true`` ，这两个参数的主要区别是：

使用 ``-Dmaven.test.skip=true`` ，不但跳过单元测试的运行，也跳过测试代码的编译；
使用 ``-DskipTests=true`` 跳过单元测试，但是会继续编译。


2、pom.xml中配置跳过测试
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: xml
   

   <build>
        <plugins>
            <!-- maven 打包时跳过测试 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <configuration>
                    <skip>true</skip>
                </configuration>
            </plugin>
        </plugins>
   </build>


3、添加Maven配置参数
>>>>>>>>>>>>>>>>>>>>>>>>>>

打开配置，找到 ``Build,Exxcution,Deployment –> Maven Tools –> Maven –> Runner``，在 VM option 中添加 ``-Dmaven.test.skip=true`` 或者 ``-DskipTests=true``，就能在打包是跳过测试。

4、通过更改设置
>>>>>>>>>>>>>>>>>>>>>>>>>>

打开配置，找到 ``Build,Exxcution,Deployment –> Maven Tools –> Maven –> Runner``，在 ``Properties`` 中勾选 ``Skip Test`` 选项。