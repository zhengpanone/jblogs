============================
SpringBoot热部署
============================

SpringBoot热部署的两种方式


SpringLoader插件
=========================

方式一
>>>>>>>>>>>>>>>>>>

以Maven插件方式使用SpringLoader

修改pom.xml

.. code-block:: xml
    

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <dependencies>
                    <dependency>
                        <groupId>org.springframework</groupId>
                        <artifactId>springloaded</artifactId>
                        <version>1.2.5.RELEASE</version>
                    </dependency>
                </dependencies>
            </plugin>
        </plugins>
    </build>

不能直接通过启动类进行启动项目,需要使用maven命令来启动项目 **spring-boot:run**

SpringLoader只能对java代码做热部署处理,对前端页面不能热部署进行处理

方式二
>>>>>>>>>>>>>>>>>>>

使用jar包进行热部署 **-javaagent: .\lib\springloaded-1.2.5.RELEASE.jar -noverify**


DevTools工具
========================

SpringLoader在部署项目时使用的是热部署的方式

DevTools在不是项目时时重新部署的方式

修改pom.xml添加devtools的坐标

.. code-block:: xml
    

    <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
             <optional>true</optional>
    </dependency>
