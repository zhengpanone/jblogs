@FunctionalInterface
public interface DiscountStrategy {
    BigDecimal apply(BigDecimal price);
}
