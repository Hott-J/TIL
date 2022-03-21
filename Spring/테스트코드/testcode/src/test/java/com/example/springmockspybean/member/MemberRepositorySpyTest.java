package com.example.springmockspybean.member;

import com.example.springmockspybean.domain.member.Member;
import com.example.springmockspybean.domain.member.MemberRepository;
import com.example.springmockspybean.domain.member.MemberService;
import org.assertj.core.api.Assertions;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.junit.MockitoJUnitRunner;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class MemberRepositorySpyTest {

//    @Spy
//    private MemberService memberService; // memberRepository가 null이므로 테스트 실패. Spy는 전부 주입받아야함

    @InjectMocks
    private MemberService memberService;

    @Mock
    private MemberRepository memberRepository; // null인 memberRepository를 mockito로 감싸여 주입

    @Test
    public void saveTest() {
        // given
        Member saveMember = Member.builder()
                .name("테스트")
                .age(20)
                .status(Member.MemberStatus.NORMAL)
                .build();
        when(memberService.findOne(any())).thenReturn(saveMember);

        // when
        Member findMember = memberService.findOne(1L);

        // then
        System.out.println("=============================");
        System.out.println("findMember = " + findMember);
        Assertions.assertThat(findMember.getStatus()).isEqualTo(saveMember.getStatus());
        Assertions.assertThat(findMember.getName()).isEqualTo(saveMember.getName());
    }
}
