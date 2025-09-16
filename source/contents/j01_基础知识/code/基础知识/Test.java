class MyThread extends Thread {
  @Override
  public void run() {
    System.out.println("线程运行中：" + Thread.currentThread().getName());
  }
}

public class Main {
  public static void main(String[] args) {
    MyThread t1 = new MyThread();
    t1.start(); // 启动线程
  }
}