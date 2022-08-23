package hello.core.scope;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Scope;
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

public class PrototypeTest {
    @Test
    void prototypeBeanFind() {
        AnnotationConfigApplicationContext ac =
                new AnnotationConfigApplicationContext(PrototypeBean.class); // PrototypeBean 클래스가 컴포넌트로 자동 등록되서 컴포넌트 스캔 대상이 됨
        System.out.println("find prototypeBean1");
        PrototypeBean p1 = ac.getBean(PrototypeBean.class);
        System.out.println("find prototypeBean2");
        PrototypeBean p2 = ac.getBean(PrototypeBean.class);
        System.out.println("p1 = " + p1);
        System.out.println("p2 = " + p2);
        Assertions.assertThat(p1).isNotSameAs(p2);

        ac.close(); // 스프링 컨테이너가 destory 해주지 않는다. close 안됨. 만들고 버림 (이름그대로 프로토타입)

        p1.destroy(); // 이렇게 수작업으로 종료시켜주면 됨
    }

    @Scope("prototype")
 //   @Component // 위에서 자동으로 등록해주므로 필요 없음
    static class PrototypeBean {
        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init");
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }
    }
}
