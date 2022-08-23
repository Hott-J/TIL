package hello.core;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;

@Configuration
@ComponentScan(
//        basePackages = "hello.core.member", // 멤버만 컴포넌트 스캔
        // 디폴트 값은 AutoAppConfig가 위치한 클래스의 패키지가 시작 위치
        // 권장법은 패키지 위치를 지정하지 않고, 설정 정보를 프로젝트 최상단에 두는 것
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION,
                classes = Configuration.class) // AppConfig를 적용하지 않기 위함
)
public class AutoAppConfig {
//    @Bean(name = "memoryMemberRepository")
//    MemberRepository memberRepository(){
//        return new MemoryMemberRepository();
//    }
//
//    @Bean(name = "orderService")
//    public OrderServiceImpl orderService(){
//        System.out.println("call AppConfig.orderService");
//        return new OrderServiceImpl(memberRepository(), discountPolicy());
//        //return null; ////필드주입
//    }
//
//    @Bean(name = "discountPolicy")
//    public DiscountPolicy discountPolicy(){
//        return new RateDiscountPolicy();
//    }

}
