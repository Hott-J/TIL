package com.example.springmockspybean.domain.member;

import lombok.*;
import org.hibernate.annotations.CreationTimestamp;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "Member")
@Getter
@ToString
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Member {

    @Id
    @GeneratedValue
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "age")
    private Integer age;

    @Column(name = "status")
    private MemberStatus status;

    @Column(name = "reg_dt")
    @CreationTimestamp
    private LocalDateTime regDt;

    public enum MemberStatus{
        NORMAL, DORMANENT, DROP
    }

    @Builder
    public Member(String name, Integer age, MemberStatus status, LocalDateTime regDt) {
        this.name = name;
        this.age = age;
        this.status = status;
        this.regDt = regDt;
    }
}