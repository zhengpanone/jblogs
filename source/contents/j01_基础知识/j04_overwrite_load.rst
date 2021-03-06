===========================================
Java 重写（OverWride）与重载（OverLoad）
===========================================


重写
======

    重写是子类对父类的允许访问的方法的实现过程进行编写！，返回值和形参都不能改变。即外壳不变，核心重写！
    重写好处：子类可以根据需要，定义特定于自己的行为，即子类能够根据需要实现父类的方法

.. code:: java

 class Animal{
    public viod move(){
        System.out.println("Animal can move!");
    }
 }

 class Dog extends Animal{
    public viod move(){
        System.out.println("Dog can run and walk!");
    }
 }

 public class TestDog{
    public static void main(String args[]){
        Animal a = new Animal();
        Animal b = new Dog();
        a.move;
        b.move();
    }
 }

在编译阶段，只是检查参数的引用类型，然而在运行时，JVM指定对象的类型并且运行该对象的方法。因此在上面的例子中，之所以能编译成功，是因为Animal类中存在move方法，然而运行时，运行的是特定对象的方法。

重载
======================

方法名相同，参数列表不同，与返回值无关



Java中2*（i*i）比2*i*i快
===========================

.. code:: java 

 public static viod main(String[] args){
    long startTime = System.nannoTime();
    int n = 0;
    for (int i =0;i<1000000000;i++){
        n+ = 2*i*i
    }
    System.out.println((double)(System.nannoTime()-startTime)/1000000000+"S");
    System.out.println("n="+n);
 }

2*i*i 进行了大量的堆栈操作，因此，需要保存大量的中间结果；而 2*(i*i) 只有少量的堆栈操作。显而易见，2*(i*i) 比 2*i*i 快是由于 JIT 优化的结果。






