package com.zp.xc.common.date;

import java.math.BigDecimal;

public class PriceCalculator {
    public static void main(String[] args) {
        BigDecimal originalPrice = new BigDecimal("100");
        BigDecimal vipPrice = MemberType.VIP.applyDiscount(originalPrice);
        System.out.println("VIP会员价格：" + vipPrice);
    }
}
