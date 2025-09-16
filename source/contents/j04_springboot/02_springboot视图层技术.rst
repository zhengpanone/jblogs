===========================
SpringBoot视图层技术
===========================

整合jsp
================

1. 修改pom.xml
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: xml
    :linenos:

    <!--Spring Boot启动父依赖-->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.2.RELEASE</version>
        <relativePath/>
    </parent>
    <!--指定JDK版本-->
    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <!-- 添加springboot启动器-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- 整合jsp-->
        <!-- jstl-->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
        </dependency>
        <!--jasper-->
        <dependency>
            <groupId>org.apache.tomcat.embed</groupId>
            <artifactId>tomcat-embed-jasper</artifactId>
        </dependency>

    </dependencies>

    <!-- 打包方式-->
    <packaging>war</packaging>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
            </resource>
            <resource>
                <directory>src/main/webapp</directory>
            </resource>
        </resources>
    </build>

2. 创建springboot的全局配置文件,application.properties
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: properties
    :linenos:

    spring.mvc.view.prefix=/WEB-INF/jsp
    spring.mvc.view.suffix=.jsp

3. 创建Controller
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: java
    :linenos:

    package com.zp.controller;

    import com.zp.pojo.User;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.RequestMapping;

    import java.util.ArrayList;
    import java.util.List;

    @Controller
    public class UserController {
        @RequestMapping("/showUser")
        public String showUser(Model model) {
            List<User> list = new ArrayList<>();
            list.add(new User(1, "张三", 20));
            list.add(new User(2, "李四", 20));
            //Model对象
            model.addAttribute("list", list);
            // 跳转视图
            return "userList";
        }
    }



4. 创建jsp
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: jsp
    :linenos:

    <%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    <html>
    <head>
        <title>Title</title>
    </head>
    <body>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
        </tr>
        <c:forEach items="${list}" var="user">
            <tr>
                <td>${user.userId}</td>
                <td>${user.userName}</td>
                <td>${user.userAge}</td>
            </tr>
        </c:forEach>

    </table>
    </body>
    </html>

5. 注意事项
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

 **错误**

    springboot + webapp 目录下jsp 打包运行后jsp页面找不到

 **原因**
    
    maven打包成jar的时候webapp目录并没有打包进去，需要改成war的方式

 **解决**

    修改pom.xml


整合freemarker
======================

修改pom.xml,
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. _freemarker_config:

创建spring boot的全局配置文件,application.properties
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: properties
    :linenos:

    spring.freemarker.suffix=.ftlh

编写ftlh模板
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

**SpringBoot要求模板形式的视图层技术的文件必须放到src/main/resources目录下必须要有一个文件夹名为templates**

.. literalinclude:: ./code/02_springboot视图层技术/1.展示用户数据.ftl
    :language: html
  
编写Controller
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: java
    :linenos:

    package com.zp.controller;

    import com.zp.pojo.User;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.RequestMapping;

    import java.util.ArrayList;
    import java.util.List;

    @Controller
    public class UserController {
        @RequestMapping("/showUser")
        public String showUser(Model model) {
            List<User> list = new ArrayList<>();
            list.add(new User(1, "张三", 20));
            list.add(new User(2, "李四", 20));
            //Model对象
            model.addAttribute("list", list);
            // 跳转视图
            return "userList";
        }
    }


整合Thymeleaf
=======================

目录位置: src/main/resources/templates

templates: 该目录是安全的,意味该目录下的内容是不允许外界直接访问的

.. _Thymeleaf_pom.xml:

修改pom.xml
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

与freemarker类似

.. _Thymeleaf_controller:

编写Controller
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

与freemarker类似

编写Thymeleaf模板
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: html
    :linenos:

    <!DOCTYPE html>
    <html lang="en" xmlns:th="http://www.thymeleaf.org">
    <head>
        <meta charset="UTF-8">
        <title>Thymeleaf案例</title>
    </head>
    <body>
        <span th:text="Hello"></span>
        <br>
        <span th:text="${msg}"></span>
    </body>
    </html>


Thymeleaf语法详解
===================================

变量输出与字符串操作
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. 页面中输出值, th:text="${msg}" 

.. code-block:: html
    :linenos:

    <span th:text="${msg}"></span>

2. 将值存放到input标签中显示,th:value 

.. code-block:: html
    :linenos:

    <input type="text" th:value="${msg}">

3. 判断内容是否为空, th:text="${#strings.isEmpty(msg)}" 

.. code-block:: html
    :linenos:

    <span th:text="${#strings.isEmpty(msg)}"></span>
    <span th:text="${#strings.contains(msg,'T')}"></span>

**调用Thymeleaf内置对象一定要有#**

**大部分内置对象都以s结尾 string、numbers、dates**



日期格式化处理
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

格式化日期默认以浏览器默认语言为标准, th:text="#dates.format(key)"

.. code-block:: html
    :linenos:

    <span th:text="${#dates.format(date)}"></span>
    <span th:text="${#dates.format(date,'yyyy/MM/dd')}"></span>
    <span th:text="${#dates.year(date)}"></span>
    <span th:text="${#dates.month(date)}"></span>
    <span th:text="${#dates.day(date)}"></span>

条件判断
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

th:if 
::::::::::::::::::::::::

.. code-block:: html
    :linenos:

    <span th:if="${sex} == '男'"></span>
        性别: <span th:text="${sex}"></span>
    <span th:if="${sex} =='女'">
        性别: <span th:text="${sex}"></span>
    </span>

th:switch
::::::::::::::::::::::::

.. code-block:: html
    :linenos:

    <div th:switch="${id}">
        <span th:case=1>ID为1</span>
        <span th:case=2>ID为2</span>
        <span th:case=3>ID为3</span>
    </div>

迭代遍历
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

th:each 
::::::::::::::::::::::

th:each迭代list
''''''''''''''''''''''

.. code-block:: html
    :linenos:

    <table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Age</th>
        <th>Index</th>
        <th>odd</th>
        <th>size</th>
        <th>even</th>
    </tr>
    <tr th:each="u,var : ${user}">
        <td th:text="${u.userId}"></td>
        <td th:text="${u.userName}"></td>
        <td th:text="${u.userAge}"></td>
        <td th:text="${var.index}"></td>
        <td th:text="${var.odd}"></td>
        <td th:text="${var.size}"></td>
        <td th:text="${var.even}"></td>

    </tr>
    </table>

var 为状态变量属性,该变量可以随意命名

- index 当前迭代器索引,从0开始

- count 当前迭代对象的计数,从1开始

- size 被迭代对象的长度

- even/odd 布尔值,当前循环是否偶/奇,从0开始

- first/last 布尔值,当前循环是否第一/最后一个

th:each迭代Map
''''''''''''''''''''''

.. code-block:: html
    :linenos:

    <table border="1">
        <tr>
            <th>map key</th>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
        </tr>
        <tr th:each="maps : ${map}">
            <td th:each="entry :${maps}" th:text="${entry.key}"></td>
            <td th:each="entry :${maps}" th:text="${entry.value.userId}"></td>
            <td th:each="entry :${maps}" th:text="${entry.value.userName}"></td>
            <td th:each="entry :${maps}" th:text="${entry.value.userAge}"></td>
        </tr>
    </table>

域对象操作
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: java
    :linenos:

    @RequestMapping("/showInfo2")
        public String showInfo2(HttpServletRequest request, Model model) {
            request.setAttribute("req", "HttpServletRequest");
            request.getSession().setAttribute("sess", "HttpSession");
            request.getSession().getServletContext().setAttribute("app", "Application");
            return "index2";
        }

HttpServletRequest
::::::::::::::::::::::::::::::::::::::

.. code-block:: java
    :linenos:

    request.setAttribute("req", "HttpServletRequest");

.. code-block:: html
    :linenos:

    Request:<span th:text="${#httpServletRequest.getAttribute('req')}"></span>


HttpSession
::::::::::::::::::::::::::::::::::::::

.. code-block:: java
    :linenos:

    request.getSession().setAttribute("sess", "HttpSession");

.. code-block:: html
    :linenos:

    Session:<span th:text="${session.sess}"></span>
   
ServletContext
::::::::::::::::::::::::::::::::::::::

.. code-block:: java
    :linenos:

    request.getSession().getServletContext().setAttribute("app", "Application");

.. code-block:: html
    :linenos:

    Application:<span th:text="${application.app}"></span>

URL表达式
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

th:href

th:src

绝对路径

.. code-block:: html
    :linenos:

    <a th:href="@{http://www.baidu.com}">绝对路径</a>

相对路径

    相对于当前项目上下文

    .. code-block:: html
        :linenos:

        <a th:href="@{/show}">相对路径</a>


    相对于服务器路径的根

    .. code-block:: html
        :linenos:

        <a th:href="@{~/project2/resourcename}">相对于服务器的根</a>

url中实现参数传递

.. code-block:: html
    :linenos:

    <a th:href="@{/show(id=1,name=zhangsan)}">相对路径传参</a>


url中restful风格进行参数传递

.. code-block:: html
    :linenos:

    <a th:href="@{/path/{id}/show}">相对路径传参</a>



