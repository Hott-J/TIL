package hellojpa;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Team {

    @Id @GeneratedValue
    @Column(name="TEAM_ID")
    private Long id;

    private String name;

    @OneToMany(mappedBy = "team") // 일대다. mappedBy. 뭐랑 연결되어있지? Team 클래스 변수인 private Team team과 걸려있다.
    private List<Member> members = new ArrayList<>(); // add 할 때 nullPoint가 안뜨므로 ArrayList로 초기화하는게 관례. 팀의 멤버를 저장해두는 역할

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


    public List<Member> getMembers() {
        return members;
    }

    public void setMembers(List<Member> members) {
        this.members = members;
    }

//    public void addMember(Member member) {
//        member.setTeam(this);
//        members.add(member);
//    }
}