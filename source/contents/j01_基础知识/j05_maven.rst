================
Maven
================

常用命令
==============

clean 、compile 、test、 package、 install 、deploy;整个流程是一个默认生命周期

加快Maven项目创建
======================

每次创建项目时， IDEA 要使用插件进行创建，这些插件当你创建新的项目时，它每次都会去中央仓库下载，这样
使得创建比较慢。应该创建时，让它找本地仓库中的插件进行创建项目。
在 IDEA 的 Settings 窗口的 Build, Execution, Deployment > Build Tools > Maven > Runner 中对 VM Option 设置
为 **-DarchetypeCatalog=internal**

idea 添加Live Templates
=============================

Settings>Editor>Live Templates
配置templates 选值应用

解决jar包冲突
===================

1、第一声明优先原则: 那个jar包的坐标在前面,这个jar包就是先声明,先声明的jar包可以优先进入项目
2、路径近者优先原则: 直接依赖路径比传递依赖路径近,最终项目进入的jar包会是路径近的直接依赖包
3、直接排除法: 当我们要排除某个jar包下的依赖包,在配置excusions标签的时候,内部可以不写版本号
4、统一管理jar包版本

**dependencyManagement标签可以锁定jar版本,为了防止传递依赖jar被直接依赖jar覆盖,可以锁定传递依赖jar版本**

