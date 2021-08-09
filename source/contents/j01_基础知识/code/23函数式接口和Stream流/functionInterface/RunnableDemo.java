package com.zp.java8.lambda;

public class RunnableDemo {
    public static void main(String[] args) {
        startThread(new Runnable() {
            @Override
            public void run() {
                System.out.println("匿名内部类方式" + "\n" + Thread.currentThread().getName() + "线程启动了");
            }
        });

        System.out.println();
        startThread(() -> {
            System.out.println("lambda方式" + "\n" + Thread.currentThread().getName() + "线程启动了");
        });
    }

    public static void startThread(Runnable runnable) {
        Thread thread = new Thread(runnable);
        thread.start();
    }
}
