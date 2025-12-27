package com.zp.xc.common.date;

import java.math.BigDecimal;

public enum MemberType {
    // 普通会员
       REGULAR(new BigDecimal("0.9")),
       // VIP 会员
    VIP(new BigDecimal("0.8")),
     // 高级会员
    PREMIUM(new BigDecimal("0.7"));

    private final BigDecimal discountRate;

    MemberType(BigDecimal discountRate) {
        this.discountRate = discountRate;
    }

    public BigDecimal applyDiscount(BigDecimal price) {
        return price.multiply(discountRate);
    }
    
    
}