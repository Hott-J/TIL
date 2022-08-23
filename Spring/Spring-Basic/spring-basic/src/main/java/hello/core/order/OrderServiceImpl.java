package hello.core.order;

import hello.core.annotation.MainDiscountPolicy;
import hello.core.discount.DiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
//@RequiredArgsConstructor // final이 붙은애를 인자로 생성자 만들어줌
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository; // final 쓰면 생성자에서만 값을 넣어줄 수 있음!!!
    // 생성자에서 memberRepository를 누락한 것도 알 수 있게 자바 컴파일에서 오류메시지를 알려준다
    private final DiscountPolicy discountPolicy;

//    @Autowired -> 필드 주입
//    private MemberRepository memberRepository;

//    @Autowired(required = false) // 선택적으로 동작 -> 수정자 주입
//    public void setMemberRepository(MemberRepository memberRepository){
//        this.memberRepository = memberRepository;
//    }

    @Autowired //생성자가 1개면 생략 가능 -> 생성자 주입, bean이름을 반환타입이 아닌 필드명까지해서 이름 명명해줌. 똑같은 타입 여러개 빈을 구분해줌
    public OrderServiceImpl(MemberRepository memberRepository, @MainDiscountPolicy DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }

    // 테스트 용도
    public MemberRepository getMemberRepository(){
        return memberRepository;
    }
}
