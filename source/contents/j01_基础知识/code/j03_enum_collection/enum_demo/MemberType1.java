package com.zp.xc.common.date;

import java.math.BigDecimal;

public enum MemberType {
    // 普通会员
    REGULAR {
        @Override
        public BigDecimal applyDiscount(BigDecimal price) {
            return price.multiply(new BigDecimal("0.9"));
        }
    },
    // VIP 会员
    VIP {
        @Override
        public BigDecimal applyDiscount(BigDecimal price) {
            return price.multiply(new BigDecimal("0.8"));
        }
    },
    // 高级会员
    PREMIUM {
        @Override
        public BigDecimal applyDiscount(BigDecimal price) {
            return price.multiply(new BigDecimal("0.7"));
        }
    };

    public abstract BigDecimal applyDiscount(BigDecimal price);
}