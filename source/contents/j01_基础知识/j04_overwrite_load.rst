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

匿名内部类
======================

Java匿名内部类访问外部变量，外部变量需被标志为final

二、解释
>>>>>>>>>>>>>>>>>>>>

这要从闭包说起，匿名内部类和外部方法形成了一个闭包，因此，匿名内部类能够访问外部方法的变量，看起来是一种“天经地义”的事情，Java语言当然也需要实现这种特性，但是这里遇到了一个问题。

匿名内部类的生命周期可能比外部的类要长，因此访问外部局部变量有可能是访问不到的。

那怎么办呢？Java语言为了实现这种特性， 只好将外部的局部变量偷偷的赋值了一份给匿名内部类。那这样匿名内部类就可以肆无忌惮的访问外部局部变量了。

问题又来了，这种通过赋值的形式有一个缺陷，匿名内部类不可以修改“原来的局部变量”，因为是一份“复制品”，修改复制品对原变量没什么影响啊。

那怎么办？ Java语言干脆强制要求被匿名内部类访问的外部局部变量必须是final的，什么意思呢？就是“一刀切”，不让修改了。

作者：Mr云台
链接：https://www.jianshu.com/p/609ca1c584ac
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




