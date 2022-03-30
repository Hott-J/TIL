package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain {

    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello"); // 애플리케이션 로딩 시점에 하나 생성
        EntityManager em = emf.createEntityManager(); // 엔티티 매니저 꺼냄. 트랜잭션 한 단위마다 만들어줘야한다
        // code
        EntityTransaction tx = em.getTransaction(); // JPA는 트랜잭션 안에서 데이터변경이 일어나야한다.
        tx.begin(); // 트랜잭션 시작

        try {
            Team team = new Team();
            team.setName("TeamA");
            //team.getMembers().add(member); // 팀은 mapped by로 매핑이므로 읽기 전용. 이는 member의 teamId를 add해주지않는다.
            em.persist(team); // 영속성 컨텍스트가 되면 무조건 id는 알게 됨

            Member member = new Member();
            member.setName("member1");
            member.changeTeam(team); // 연관관계의 주인에 값을 set 해줘야한다.

//            team.getMembers().add(member); // 양쪽에 값을 넣어준다.

            em.persist(member);
            
 //           team.addMember(member); // Team에서 addMember 할지 Member에서 changeTeam 할지 결정. 둘 중 하나만 사용해야지 둘다 쓰면 안됨

//            em.flush(); // 영속성 컨텍스트에 있는걸 DB에 날림
//            em.clear(); // 영속성 컨텍스트 초기화

            Team findTeam = em.find(Team.class, team.getId()); // flush 없으면 1차 캐시.
            List<Member>members=findTeam.getMembers(); // Member 테이블을 참조하여 쿼리 날라감. 1차 캐시에 있으면 쿼리 날라가지 않음

            for(Member m : members){
                System.out.println("m="+m.getName());
            }


            tx.commit(); // 잘되면  커밋
        } catch(Exception e){
            tx.rollback(); // 문제시 롤백
        } finally {
            em.close(); // 작업 끝나면 엔티티매니저 닫아줌
        }
        emf.close();
    }
}
