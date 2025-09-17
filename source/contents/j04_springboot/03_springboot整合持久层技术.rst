====================================
SpringBoot整合持久层技术
====================================

SpringBoot+SpringMVC+MyBatis
=====================================

修改pom.xml
----------------------------------------

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>

      <groupId>com.zp</groupId>
      <artifactId>11-springboot-springmvc-mybatis</artifactId>
      <version>1.0-SNAPSHOT</version>

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

          <!--添加thymeleaf包-->
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-thymeleaf</artifactId>
          </dependency>

          <!--MyBatis启动器-->
          <dependency>
              <groupId>org.mybatis.spring.boot</groupId>
              <artifactId>mybatis-spring-boot-starter</artifactId>
              <version>1.1.1</version>
          </dependency>
          <!--mysql数据库驱动-->
          <dependency>
              <groupId>mysql</groupId>
              <artifactId>mysql-connector-java</artifactId>
          </dependency>
          <!--druid数据库连接池-->
          <dependency>
              <groupId>com.alibaba</groupId>
              <artifactId>druid</artifactId>
              <version>1.0.9</version>
          </dependency>

      </dependencies>

  <build>
          <resources>
              <resource>
                  <directory>src/main/java</directory>
                  <includes>
                      <include>**/*.xml</include>
                  </includes>
              </resource>
          </resources>
      </build>

  </project>

添加application.properties全局配置文件
------------------------------------------------

.. code-block:: properties
    
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://localhost:3306/ssm
  spring.datasource.username=root
  spring.datasource.password=root
  spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
  mybatis.type-aliases-package=com.zp.pojo

编写实体类
----------------------------------------

.. code-block:: java

  package com.zp.pojo;

  public class User {
      private Integer id;
      private String name;
      private Integer age;

      public Integer getId() {
          return id;
      }

      public void setId(Integer id) {
          this.id = id;
      }

      public String getName() {
          return name;
      }

      public void setName(String name) {
          this.name = name;
      }

      public Integer getAge() {
          return age;
      }

      public void setAge(Integer age) {
          this.age = age;
      }
  }

编写接口
----------------------------------------

.. code-block:: java

  package com.zp.mapper;

  import com.zp.pojo.User;

  public interface UserMapper {

      void insterUser(User user);
  }

编写xml
----------------------------------------

.. code-block:: xml
    
  <?xml version="1.0" encoding="UTF-8" ?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
          "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
  <mapper namespace="com.zp.mapper.UserMapper">

      <insert id="insterUser" parameterType="user">
          insert into user(name ,age) value(#{name },#{age})
      </insert>
  </mapper>


编写service
----------------------------------------

.. code-block:: java
    
  package com.zp.service;

  import com.zp.pojo.User;

  public interface UserSerivce {

      void addUser(User user);
  }


编写serviceImpl
----------------------------------------

.. code-block:: java
    
  package com.zp.service.impl;

  import com.zp.mapper.UserMapper;
  import com.zp.pojo.User;
  import com.zp.service.UserService;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Service;
  import org.springframework.transaction.annotation.Transactional;

  @Service
  @Transactional
  public class UserServiceImpl implements UserSerivce {
      @Autowired
      private UserMapper userMapper;

      @Override
      public void addUser(User user) {
          this.userMapper.insterUser(user);

      }
  }

编写controller
----------------------------------------

.. code-block:: java
    
  package com.zp.controller;

  import com.zp.pojo.User;
  import com.zp.service.UserSerivce;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Controller;
  import org.springframework.web.bind.annotation.PathVariable;
  import org.springframework.web.bind.annotation.RequestMapping;

  @Controller
  @RequestMapping("/user")
  public class UserController {
      @Autowired
      private UserSerivce userSerivce;

      @RequestMapping("/{page}")
      public String showPage(@PathVariable String page) {
          return page;
      }

      @RequestMapping("/addUser")
      public String addUser(User user) {
          this.userSerivce.addUser(user);
          return "ok";
      }
  }

编写html页面
----------------------------------------

.. code-block:: html
    
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>添加</title>
  </head>
  <body>
  <form th:action="@{/user/addUser}" method="post">
      用户名：<input type="text" name="name"><br>
      年龄：<input type="text" name="age"><br>
      <input type="submit" value="提交">
  </form>
  </body>
  </html>

编写启动器
----------------------------------------

.. code-block:: java
    
  package com.zp;

  import org.mybatis.spring.annotation.MapperScan;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  @MapperScan("com.zp.mapper") //用于扫描MyBatis的Mapper接口
  public class App {

      public static void main(String[] args) {
          SpringApplication.run(App.class, args);
      }
  }

