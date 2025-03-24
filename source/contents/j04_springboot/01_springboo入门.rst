===============================
SpringBoot入门
===============================

编写HelloWorld
========================

1. 创建一个Maven项目

#. 编写pom.xml

 1. 添加springBoot启动父依赖,并指定SpringBoot版本

    .. code-block:: xml
        :linenos:

        <!--Spring Boot启动父依赖,并指定spingboot版本-->
        <parent>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-parent</artifactId>
                <version>2.1.2.RELEASE</version>
                <relativePath/>
        </parent>

 #. 修改jdk版本

    .. code-block:: xml
        :linenos:

        <!--指定jdk版本-->
        <properties>
                <java.version>1.8</java.version>
        </properties>

 #. 添加springboot启动器

    .. code-block:: xml
        :linenos:

        <!--在dependenices中添加springboot的启动器-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

    SpringBoot启动器就是一些jar包的集合,SpringBoot一共提供了44个启动器。支持全栈式web开发,包括了tomcat和SpringMVC等jar.

    - spring-boot-starter-jdbc支持spring以jdbc方式操作数据库的jar包集合

    - spring-boot-starter-redis 支持redis数据库操作

3. 编写controller
 
    添加package com.zp.controller,新建文件HelloWorldController.java

    .. code-block:: java
        :linenos:

        package com.zp.controll;

        import org.springframework.web.bind.annotation.RequestMapping;
        import org.springframework.web.bind.annotation.RestController;

        import java.util.HashMap;
        import java.util.Map;

        /**
        * RestController和RequestMapping注解来自SpringMVC的注解
        * RestController：提供实现了REST API，可以服务JSON,XML或者其他。这里是以String的形式渲染出结果。
        * RequestMapping：提供路由信息，"/“路径的HTTP Request都会被映射到sayHello方法进行处理。
        */

        @RestController
        public class HelloWorldController {
            @RequestMapping("/")
            public Map<String, Object> sayHello() {
                Map<String, Object> map = new HashMap<>();
                map.put("msg", "HelloWorld");
                return map;

            }
        }

#. 编写启动类

    在package下新建文件App.java

    .. code-block:: java
        :linenos:

        package com.zp;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;

        @SpringBootApplication
        public class App {

            public static void main(String[] args) {
                SpringApplication.run(App.class, args);
            }
        }

    启动器存放位置,启动器可以和controller位于同一个package下,或者位于controller的上一级包中,但是不能放到controller的平级以及子包下。

整合Servlet
========================

1. 通过注解扫描完成Servlet组件的注册

 1. 编写servlet

     创建com.zp.servlet的package,新建FirstServlet

    .. code-block:: java
        :linenos:

        package com.zp.servlet;

        import javax.servlet.ServletException;
        import javax.servlet.annotation.WebServlet;
        import javax.servlet.http.HttpServlet;
        import javax.servlet.http.HttpServletRequest;
        import javax.servlet.http.HttpServletResponse;
        import java.io.IOException;

        /**
        * SpringBoot整合Servlet方式一
        * <servlet>
        *     <servlet-name>FirstServlet</servlet-name>
        *     <servlet-class>com.zp.servlet.FirstServlet</servlet-class>
        * </servlet>
        * <servlet-mapping>
        *     <servlet-name>FirstServlet</servlet-name>
        *     <url-pattern>/first</url-pattern>
        * </servlet-mapping>
        */
        @WebServlet(name= "FirstServlet", urlPatterns = "/first")
        public class FirstServlet extends HttpServlet {
            @Override
            protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                super.doGet(req, resp);

            }

        }

 #. 编写启动类

     在com.zp的package下新建App.java 

    .. code-block:: java
        :linenos:

        package com.zp;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.ServletComponentScan;

        /**
        * SpringBoot整合Servlet方式一
        */
        @SpringBootApplication
        @ServletComponentScan //在springBoot启动时回扫描 @WebServlet,并将该类实例化
        public class App {
            public static void main(String[] args) {
                SpringApplication.run(App.class, args);

            }
        }

#. 通过方法完成Servlet组件的注册

 1. 编写servlet

    .. code-block:: java
        :linenos:

        package com.zp.servlet;

        import javax.servlet.ServletException;
        import javax.servlet.http.HttpServlet;
        import javax.servlet.http.HttpServletRequest;
        import javax.servlet.http.HttpServletResponse;
        import java.io.IOException;

        public class SecondServlet extends HttpServlet {
            @Override
            protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                System.out.println("SecondServlet................");
                super.doGet(req, resp);
            }
        }


 #. 编写启动类

    .. code-block:: java
        :linenos:
        
        package com.zp;

        import com.zp.servlet.SecondServlet;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.ServletRegistrationBean;
        import org.springframework.context.annotation.Bean;

        /**
        * SpringBoot整合Servlet方式二
        */
        @SpringBootApplication
        public class App2 {
            public static void main(String[] args) {
                SpringApplication.run(App2.class, args);

            }

            @Bean
            public ServletRegistrationBean getServletRegistrationBean() {
                ServletRegistrationBean bean = new ServletRegistrationBean(new SecondServlet());
                bean.addUrlMappings("/second");
                return bean;
            }
        }


整合Filter
==========================

1. 通过注解扫描完成Filter组件注册

 #. 编写Filter

    .. code-block:: java
        :linenos:

        package com.zp.filter;


        import javax.servlet.*;
        import javax.servlet.annotation.WebFilter;
        import java.io.IOException;

        /**
        * SpringBoot整合Filter方式一
        * <filter>
        *     <filter-name>FirstFilter</filter-name>
        *     <filter-class>com.zp.filter.FirstFilter</filter-class>
        * </filter>
        * <filter-mapping>
        *     <filter-name>FirstFilter</filter-name>
        *     <url-pattern>/first</url-pattern>
        * </filter-mapping>
        */
        //@WebFilter(filterName = "FirstFilter", urlPatterns = {"*.do", "*.jsp"})
        @WebFilter(filterName = "FirstFilter", urlPatterns = "/first")
        public class FirstFilter implements Filter {
            @Override
            public void init(FilterConfig filterConfig)
                    throws ServletException {

            }

            @Override
            public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
                    throws IOException, ServletException {
                System.out.println("进入Filter.....................");
                filterChain.doFilter(servletRequest,servletResponse);
                System.out.println("离开Filter......................");
            }

            @Override
            public void destroy() {

            }
        }

 #. 编写启动类

    .. code-block:: java
        :linenos:

        package com.zp;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.ServletComponentScan;

        /**
        * SpringBoot整合Filter方式一
        */
        @SpringBootApplication
        @ServletComponentScan //在springBoot启动时回扫描 @WebServlet,并将该类实例化
        public class App {
            public static void main(String[] args) {
                SpringApplication.run(App.class, args);
            }
        }

2. 通过方法完成Filter组件的注册

 #. 编写servlet

    .. code-block:: java
        :linenos:

        package com.zp.filter;

        import javax.servlet.*;
        import java.io.IOException;

        /**
        * SpringBoot整合Filter方式二
        */
        public class SecondFilter implements Filter {

            @Override
            public void init(FilterConfig filterConfig) throws ServletException {

            }

            @Override
            public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
                    throws IOException, ServletException {
                System.out.println("进入SecondFilter.....................");
                filterChain.doFilter(servletRequest, servletResponse);
                System.out.println("离开SecondFilter......................");
            }

            @Override
            public void destroy() {

            }
        }




 #. 编写启动类

    .. code-block:: java
        :linenos:

        package com.zp;

        import com.zp.filter.SecondFilter;
        import com.zp.servlet.SecondServlet;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.FilterRegistrationBean;
        import org.springframework.boot.web.servlet.ServletComponentScan;
        import org.springframework.boot.web.servlet.ServletRegistrationBean;
        import org.springframework.context.annotation.Bean;

        /**
        * SpringBoot整合Filter方式一
        */
        @SpringBootApplication
        public class App2 {
            public static void main(String[] args) {
                SpringApplication.run(App2.class, args);
            }

            @Bean
            public ServletRegistrationBean getServletRegistrationBean() {
                ServletRegistrationBean bean = new ServletRegistrationBean(new SecondServlet());
                bean.addUrlMappings("/second");
                return bean;
            }

            @Bean
            public FilterRegistrationBean getFilterRegistrationBean() {
                FilterRegistrationBean bean = new FilterRegistrationBean(new SecondFilter());
                bean.addUrlPatterns("/first");
                return bean;
            }
        }


整合Listener
==========================

1. 通过注解扫描完成Listener组件注册

 1. 编写listener

    .. code-block:: java
        :linenos:

        package com.zp.listener;

        import javax.servlet.ServletContextEvent;
        import javax.servlet.ServletContextListener;
        import javax.servlet.annotation.WebListener;

        /**
        * SpringBoot 整合Listener
        * <listener>
        *  <listener-class>com.zp.listener.FirsListener</listener-class>
        * </listener>
        */
        @WebListener
        public class FirstListener implements ServletContextListener {

            public void contextDestroyed(ServletContextEvent sce) {
            }

            public void contextInitialized(ServletContextEvent sce) {
                System.out.println("Listener init...................");
            }

        }
 
 #. 编写启动类

    .. code-block:: java
        :linenos:

        package com.zp;

        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.ServletComponentScan;

        @SpringBootApplication
        @ServletComponentScan
        public class App {
            public static void main(String[] args) {
                SpringApplication.run(App.class, args);

            }
        }




#. 通过方法完成Listener组件注册

 1. 编写listener

    .. code-block:: java
        :linenos:

        package com.zp.listener;

        import javax.servlet.ServletContextEvent;
        import javax.servlet.ServletContextListener;

        public class SecondListener implements ServletContextListener {
            public void contextDestroyed(ServletContextEvent sce) {
            }

            public void contextInitialized(ServletContextEvent sce) {
                System.out.println("Second Listener init...................");
            }
        }



 #. 编写启动类

    .. code-block:: java
        :linenos:

        package com.zp;

        import com.zp.listener.SecondListener;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.boot.web.servlet.ServletComponentScan;
        import org.springframework.boot.web.servlet.ServletListenerRegistrationBean;
        import org.springframework.context.annotation.Bean;

        @SpringBootApplication
        public class App2 {
            public static void main(String[] args) {
                SpringApplication.run(App2.class, args);

            }

            @Bean
            public ServletListenerRegistrationBean getServletListenerRegisterBean() {
                ServletListenerRegistrationBean<SecondListener> bean =
                        new ServletListenerRegistrationBean<SecondListener>(new SecondListener());
                return bean;
            }
        }

访问静态资源
========================

1. SpringBoot从classpath/static的目录下查找

    目录名称必须为static

    classpath 即WEB-INF下面的classes目录

#. ServletContext根目录下查找

    在src/main 下创建文件夹 webapp ,文件夹名称必须为webapp

修改springboot访问静态资源访问路径,在 properties文件里面设置  spring.resources.static-locations 就ok了

spring.resources.static-locations 的默认值是：classpath:/META-INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/

.. code-block:: xml
    :linenos:

    server.port=8081
    spring.resources.static-locations=classpath:static/images/


文件上传
========================

1. 编写Controller 

.. code-block:: java
    :linenos:

    package com.zp.controller;

    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;
    import org.springframework.web.multipart.MultipartFile;

    import java.io.File;
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;

    @RestController// @Controller + @ResponseBody
    public class FileUploadController {
        @RequestMapping("/fileUploadController")
        public Map<String, Object> fileUpload(MultipartFile filename) throws IOException {
            System.out.println(filename.getOriginalFilename());
            filename.transferTo(new File("./" + filename.getOriginalFilename()));
            Map<String, Object> map = new HashMap<>();
            map.put("msg", "ok");
            return map;
        }

    }

#. 编写application.properties配置上传文件大小

.. code-block:: properties
    :linenos:

    # 文件上传大小为200M
    spring.servlet.multipart.max-file-size=200MB
    # 请求大小为200M
    spring.servlet.multipart.max-request-size=200MB

#. 编写前端页面

.. code-block:: html
    :linenos:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>文件上传</title>
    </head>
    <body>
    <form action="fileUploadController" method="post" enctype="multipart/form-data">
        上传文件:<input type="file" name="filename"><br>
        <input type="submit">

    </form>
    </body>
    </html>

