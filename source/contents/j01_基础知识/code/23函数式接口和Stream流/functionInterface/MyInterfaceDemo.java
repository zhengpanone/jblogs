public class MyInterfaceDemo {
    public static void main(String[] args) {
        MyInterface my = () -> System.out.println("I'm FunctionalInterface");
        my.show();
    }
}
