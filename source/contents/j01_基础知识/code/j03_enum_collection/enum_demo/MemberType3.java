package com.zp.xc.common.date;

import java.math.BigDecimal;

REGULAR(price -> price.multiply(new BigDecimal("0.9"))),
    VIP(price -> price.multiply(new BigDecimal("0.8"))),
    PREMIUM(price -> price.multiply(new BigDecimal("0.7")));

    private final DiscountStrategy discountStrategy;

    MemberType(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
    }

    public BigDecimal applyDiscount(BigDecimal price) {
        return discountStrategy.apply(price);
    }

    public String getDesc() {
        return switch (this) {
            case REGULAR -> "普通会员";
            case VIP -> "VIP会员";
            case PREMIUM -> "高级会员";
        };
    }