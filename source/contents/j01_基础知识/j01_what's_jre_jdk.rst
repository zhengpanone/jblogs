===========================================
JRE and JDK
===========================================

JRE
=================

Java Runtime Environment Java运行环境

- 包括Java虚拟机(JVM Java Virtual Machine)和Java程序所需要的核心类库。如果想要运行一个开发好的Java程序,计算机中只需要安装JRE

- JVM + 类库

JDK
======================

Java Development Kit Java开发工具包

- JDK 是提供给Java开发人员使用的,其中包含了Java开发工具,也包括了JRE。所以安装了JDK,就不用单独安装JRE
- 其中开发工具: 编译工具(javac.exe), 打包工具(jar.exe)
- JDK开发完成的java程序,交给JRE运行
- JRE + JAVA的开发工具

JDK安装路径下目录
======================

- bin目录: 存放一些可执行程序
 
   - 如 javac.exe(java编译器)、java.exe(运行工具)、jar.exe(打包工具)、javadoc.exe(文档生成工具)等

- db目录: db目录是一个小型的数据库。从JDK6.0开始,Java中引用了一个新成员JavaDB,是一个纯Java实现、开源的数据库管理系统。这个数据库不仅轻便,而且支持JDBC 4.0所有规范,在学校JDBC时,不再需要额外安装一个数据库软件,直接使用JavaDB即可。

- jre目录: jre是 Java Runtime Environment的缩写,此目录是java运行时的环境的根目录,包括Java虚拟机,运行时的类库,Java应用启动器及一个bin目录,不包含开发环境中的开发工具包

- include目录: JDK是通过C和C++ 实现,在启动时需要引入一些C语言的头文件,该目录存放这些头文件

- lib目录: lib时library的缩写,意为Java类库或类文件,是开发工具使用的归档包文件

- src.zip文件: src.zip 为src文件夹的压缩文件,src中存放的是JDK核心类的源代码,通过查看该文件可以查看Java基础类的源代码

Java代码运行
====================

javac 先编译源代码 javac HelloWorld.java 

java 运行字节码文件 java HelloWorld 

