package com.example.springmockspybean.service;

import com.example.springmockspybean.domain.customer.Customer;
import com.example.springmockspybean.domain.customer.CustomerRepository;
import com.example.springmockspybean.domain.order.CustomerOrder;
import com.example.springmockspybean.domain.order.CustomerOrderRepository;
import com.example.springmockspybean.domain.product.Product;
import com.example.springmockspybean.exception.ResourceNotFoundException;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit4.SpringRunner;

import javax.servlet.http.HttpSession;

import java.util.Optional;
import java.util.stream.Stream;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.mockito.BDDMockito.given;

/**
 * Created by jojoldu@gmail.com on 2017. 9. 19.
 * Blog : http://jojoldu.tistory.com
 * Github : https://github.com/jojoldu
 */

@RunWith(SpringRunner.class)
@SpringBootTest
public class CustomerServiceMockTest {

    @Autowired
    private CustomerService customerService;

    @MockBean(name = "httpSession") // mock
    // 객체 생성, 기존에 선언된 Bean 객체를 덮어쓰기 위함으로 문자열 값 등록, 빈의 이름을 강제로 지정하지 않으면 스프링에서 어떤 빈을 가져와야 할지 알 수 없음
    private HttpSession httpSession;

    @MockBean(name = "customerOrderRepository")
    private CustomerOrderRepository customerOrderRepository;

    @MockBean(name = "customerRepository")
    private CustomerRepository customerRepository;

    @Test
    public void findMyOrderPriceSum_로그인사용자의_주문상품금액합계가_반환된다 () throws Exception {
        //given
        Customer customer = new Customer();

        // httpSession.getAttribute를 호출할 때 파라미터가 loginUser라면 customer를 리턴하라
        given(httpSession.getAttribute("loginUser"))
                .willReturn(customer);

        CustomerOrder order = new CustomerOrder();

        order.addProduct(Product.builder()
                .price(10000L)
                .build());

        order.addProduct(Product.builder()
                .price(15000L)
                .build());

        given(customerOrderRepository.findAllByCustomer(customer))
                .willReturn(Stream.of(order));

        //when
        long sum = customerService.findMyOrderPriceSum();

        //then
        assertThat(sum, is(25000L));
    }

    @Test(expected = ResourceNotFoundException.class)
    public void findByName_찾는고객이없으면_ResourceNotFoundException발생 () throws Exception {
        //given
        final String NAME = "jojoldu";
        given(customerRepository.findCustomerByName(NAME))
                .willReturn(Optional.empty());

        //when
        customerService.findByName(NAME);
    }
}
