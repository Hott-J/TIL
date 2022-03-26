package com.example.springmockspybean.domain.customer;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

/**
 * Created by jojoldu@gmail.com on 2017. 9. 18.
 * Blog : http://jojoldu.tistory.com
 * Github : https://github.com/jojoldu
 */

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long>{

    Optional<Customer> findCustomerByName(String name);
}
