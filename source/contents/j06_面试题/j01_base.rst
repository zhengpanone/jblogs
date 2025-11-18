====================
Java基础面试题
====================

java注解原理
===================

Java 注解（Annotation）的原理是基于反射机制和字节码操作实现的。

1.注解的本质
-------------------

注解本质上是一个特殊的接口，继承自 `java.lang.annotation.Annotation`

.. code-block:: java

  // 注解定义
  public @interface MyAnnotation {
      String value() default "";
  }

  // 编译后相当于
  public interface MyAnnotation extends java.lang.annotation.Annotation {
      String value();
  }

注解的保留策略（Retention Policy）
----------------------------------------

注解有三种保留策略，决定了注解的生命周期：

.. code-block:: java

  @Retention(RetentionPolicy.SOURCE)   // 仅存在于源码，编译后丢弃
  @Retention(RetentionPolicy.CLASS)    // 存在于字节码，但运行时不可见（默认）
  @Retention(RetentionPolicy.RUNTIME)  // 运行时可见，可通过反射读取

注解的工作原理
-------------------

编译期处理（SOURCE 级别）

.. code-block:: java

  // 注解处理器
  @SupportedAnnotationTypes("com.example.MyAnnotation")
  @SupportedSourceVersion(SourceVersion.RELEASE_8)
  public class MyAnnotationProcessor extends AbstractProcessor {
      @Override
      public boolean process(Set<? extends TypeElement> annotations, 
                            RoundEnvironment roundEnv) {
          // 在编译时处理注解，生成代码等
          for (Element element : roundEnv.getElementsAnnotatedWith(MyAnnotation.class)) {
              // 处理被注解的元素
          }
          return true;
      }
  }

运行期处理（RUNTIME 级别）

.. code-block:: java

  // 定义运行时注解
  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.METHOD)
  public @interface Test {
      String name() default "";
  }

  // 使用注解
  public class TestClass {
      @Test(name = "testMethod")
      public void myMethod() {
          // 方法实现
      }
  }

  // 通过反射读取注解
  public class AnnotationProcessor {
      public void processAnnotations(Class<?> clazz) {
          for (Method method : clazz.getDeclaredMethods()) {
              if (method.isAnnotationPresent(Test.class)) {
                  Test testAnnotation = method.getAnnotation(Test.class);
                  System.out.println("Found test: " + testAnnotation.name());
              }
          }
      }
  }

注解的底层实现
-------------------

注解的存储
注解信息存储在 class 文件的属性表（Attribute Table）中：

.. code-block:: text

  ClassFile {
      u4 magic;
      u2 minor_version;
      u2 major_version;
      u2 constant_pool_count;
      cp_info constant_pool[constant_pool_count];
      u2 access_flags;
      u2 this_class;
      u2 super_class;
      // ...
      u2 attributes_count;
      attribute_info attributes[attributes_count];
  }

运行时注解的获取过程

.. code-block:: java

  // 当调用 getAnnotation() 时，JVM 内部：
  // 1. 从类的 RuntimeVisibleAnnotations 属性读取注解信息
  // 2. 动态生成注解代理对象
  // 3. 返回该代理对象

  // 相当于：
  Test annotation = (Test) Proxy.newProxyInstance(
      Test.class.getClassLoader(),
      new Class<?>[] { Test.class },
      new AnnotationInvocationHandler(Test.class, annotationData)
  );

实际应用示例
----------------

自定义 ORM 框架注解

.. code-block:: java

  // 定义实体注解
  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.TYPE)
  public @interface Entity {
      String tableName();
  }

  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.FIELD)
  public @interface Column {
      String name();
      boolean nullable() default true;
  }

  // 使用注解
  @Entity(tableName = "users")
  public class User {
      @Column(name = "id", nullable = false)
      private Long id;
      
      @Column(name = "user_name")
      private String username;
  }

  // 注解处理器
  public class ORMProcessor {
      public String generateCreateTable(Class<?> clazz) {
          if (!clazz.isAnnotationPresent(Entity.class)) {
              throw new IllegalArgumentException("Not an entity class");
          }
          
          Entity entity = clazz.getAnnotation(Entity.class);
          StringBuilder sql = new StringBuilder();
          sql.append("CREATE TABLE ").append(entity.tableName()).append(" (");
          
          for (Field field : clazz.getDeclaredFields()) {
              if (field.isAnnotationPresent(Column.class)) {
                  Column column = field.getAnnotation(Column.class);
                  sql.append(column.name()).append(" ").append(getSqlType(field.getType()));
                  if (!column.nullable()) {
                      sql.append(" NOT NULL");
                  }
                  sql.append(", ");
              }
          }
          
          sql.setLength(sql.length() - 2); // 移除最后的逗号
          sql.append(")");
          return sql.toString();
      }
      
      private String getSqlType(Class<?> type) {
          // 类型映射逻辑
          if (type == Long.class) return "BIGINT";
          if (type == String.class) return "VARCHAR(255)";
          // ...
          return "TEXT";
      }
  }
Spring 风格的事务注解

.. code-block:: java

  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.METHOD)
  public @interface Transactional {
      String value() default "default";
      int timeout() default 30;
  }

  // AOP 处理
  public class TransactionAspect {
      public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
          Method method = ((MethodSignature) joinPoint.getSignature()).getMethod();
          
          if (method.isAnnotationPresent(Transactional.class)) {
              Transactional transactional = method.getAnnotation(Transactional.class);
              String transactionManager = transactional.value();
              int timeout = transactional.timeout();
              
              // 开启事务
              beginTransaction(transactionManager, timeout);
              try {
                  Object result = joinPoint.proceed();
                  commitTransaction();
                  return result;
              } catch (Exception e) {
                  rollbackTransaction();
                  throw e;
              }
          } else {
              return joinPoint.proceed();
          }
      }
  }
  
注解的性能考虑
----------------------

- 编译期注解：无运行时开销

- 运行期注解：反射操作有性能开销，但可通过缓存优化

- 注解解析结果应该缓存，避免重复反射调用

总结
-----------

Java 注解的原理核心是：

- 编译期：通过注解处理器生成代码或进行验证

- 运行期：通过反射机制读取注解信息

- 字节码级别：注解信息存储在 class 文件的属性表中

- 动态代理：运行时注解通过动态代理对象提供访问接口

这种机制使得注解成为 Java 中实现元编程、框架开发、配置简化的重要工具。





