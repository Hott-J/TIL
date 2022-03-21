package com.example.springmockspybean.member;

import com.example.springmockspybean.domain.member.Member;
import com.example.springmockspybean.domain.member.MemberService;
import org.assertj.core.api.Assertions;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class MemberRepositoryMockTest {

    @Mock
    private MemberService memberService;


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
