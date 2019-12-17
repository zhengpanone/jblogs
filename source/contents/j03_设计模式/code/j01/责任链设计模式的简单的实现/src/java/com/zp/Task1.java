package com.zp;

public class Task1 implements Task {
    private Task task;

    public Task1() {
    }

    public Task1(Task task) {
        this.task = task;
    }

    @Override
    public void run() {
        System.out.println("task1 is run");
        if (task != null) {
            task.run();
        }
    }
}
