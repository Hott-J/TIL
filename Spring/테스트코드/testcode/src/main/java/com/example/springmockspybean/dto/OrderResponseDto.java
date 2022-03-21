package com.example.springmockspybean.dto;

import com.example.springmockspybean.domain.product.Product;
import lombok.Getter;

import java.util.List;
import java.util.stream.Collectors;

@Getter
public class OrderResponseDto {

    private String customerName;
    private List<ProductDto> products;

    public OrderResponseDto(String customerName, List<Product> products) {
        this.customerName = customerName;
        this.products = products.stream()
                .map(ProductDto::new)
                .collect(Collectors.toList());
    }

    @Getter
    public static class ProductDto {

        private String name;
        private long price;

        public ProductDto(Product product) {
            this.name = product.getName();
            this.price = product.getPrice();
        }
    }

}
