package com.example.springmockspybean.service;

import com.example.springmockspybean.domain.customer.Customer;
import com.example.springmockspybean.domain.order.CustomerOrder;
import com.example.springmockspybean.domain.order.CustomerOrderRepository;
import com.example.springmockspybean.domain.product.Product;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.Optional;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.mockito.BDDMockito.given;

/**
 * Created by jojoldu@gmail.com on 2017. 9. 22.
 * Blog : http://jojoldu.tistory.com
 * Github : https://github.com/jojoldu
 */

@RunWith(SpringRunner.class)
@SpringBootTest
public class CustomerServiceSpyMapperTest {

    @Autowired
    private CustomerService customerService;

    @MockBean(name = "customerOrderRepository") // given에서만 사용 가능하다
    private CustomerOrderRepository customerOrderRepository;

    @SpyBean(name = "objectMapper") // given 외에서는 전부 실체의 것을 사용한다
    private ObjectMapper objectMapper;

    @Test
    public void getCustomerJsonString_JSON문자열반환 () throws Exception {
        //given
        Customer customer = Customer.builder()
                .name("jojoldu")
                .build();

        final String REQUEST_PARAM = objectMapper.writeValueAsString(customer);

        CustomerOrder order = new CustomerOrder();

        order.addProduct(Product.builder()
                .price(10000L)
                .build());

        order.addProduct(Product.builder()
                .price(15000L)
                .build());

        // Mocking
        given(customerOrderRepository.findTopByCustomer(customer))
                .willReturn(Optional.of(order));

        // Spying
        given(objectMapper.readValue(REQUEST_PARAM, Customer.class))
                .willReturn(customer);

        //when
        final String customerJsonString = customerService.getCustomerJsonString(REQUEST_PARAM);

        //then
        assertThat(customerJsonString, is("{\"customerName\":\"jojoldu\",\"products\":[{\"name\":null,\"price\":10000},{\"name\":null,\"price\":15000}]}"));
    }
}
