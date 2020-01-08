public class Demo02DataType {
    /**
     * 强制类型转换 特点: 代码需要进行特使格式处理,不能自动 格式: 范围小的类型 变量名 = (范围小的类型) 范围大的数据;
     * 
     * 注意: 强制类型转换一般不推荐使用, 有可能发生精度损失,数据溢出
     */

    public static void main(String[] args) {
        int num = (int) 100L;
        System.out.println(num);

        int num2 = (int) 600000000000000L;
        System.out.println(num2);
        /**
         * byte/short/char这三种类型都可以发生数学运算 byte/short/char这三种类型在运算时,都会被首先提升为int类型,然后在计算
         */
        byte num3 = 40;
        byte num4 = 50;
        int result1 = num3 + num4;
        System.out.println(result1);
    }
}