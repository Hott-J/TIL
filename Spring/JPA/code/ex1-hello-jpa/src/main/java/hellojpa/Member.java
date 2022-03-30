package hellojpa;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

@Entity // JPA가 처음 로딩될때 JPA가 사용되겠구나라고 인식

public class Member {

    @Id // pk
    @GeneratedValue
    @Column(name="MEMBER_ID")
    private Long id;

    @Column(name = "USERNAME")
    private String name;

    @ManyToOne // 다대일. 멤버입장 다, 팀입장 일
    @JoinColumn(name="TEAM_ID") // TEAM의 FK인 TEAM_ID와 매핑
    private Team team; // 객체 지향스럽게 짠다.

    @OneToOne
    @JoinColumn(name="LOCKER_ID")
    private Locker locker;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }

    public void changeTeam(Team team) {
        this.team = team;
        team.getMembers().add(this); // 양쪽 매핑위함
    }

    public Member() {
    }
}