package com.example.springmockspybean.domain.product;

import com.example.springmockspybean.domain.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * Created by jojoldu@gmail.com on 2017. 9. 19.
 * Blog : http://jojoldu.tistory.com
 * Github : https://github.com/jojoldu
 */

public interface ProductRepository extends JpaRepository<Product, Long>{
}