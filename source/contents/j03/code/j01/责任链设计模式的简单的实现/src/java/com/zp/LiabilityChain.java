package com.zp;

public class LiabilityChain {
    public void runChain() {
        Task task3 = new Task1();
        Task2 task2 = new Task2(task3);
        Task3 task1 = new Task3(task2);
        task1.run();
    }
}
