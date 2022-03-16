package hellojpa.jpql;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import javax.persistence.*;
import java.util.List;

@SpringBootApplication
public class JpqlApplication {

	public static void main(String[] args) {
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello"); // 한번만 생성. 애플리케이션 전체 공유
		EntityManager em = emf.createEntityManager(); // 자바 컬렉션이라 생각. 쓰레드간에 공유하면 안됨.
		EntityTransaction tx = em.getTransaction();

		tx.begin(); // jpa의 모든 변경은 트랜잭션 안에서 실행해야함!!!

		try {
			Member member = new Member();
			member.setUsername("member1");
			em.persist(member);

			TypedQuery<Member> query1 = em.createQuery("select m from Member m", Member.class);
			List<Member> resultList = query1.getResultList();
			Member singleResult = query1.getSingleResult();// 값이 하나인경우

			TypedQuery<String> query = em.createQuery("select m.username from Member m", String.class);
			Query query2 = em.createQuery("select m.username, m.age from Member m"); // 반환 타입이 2개인 경우

			tx.commit(); // 해당 시점에 쿼리가 날라감
		} catch (Exception e) {
			tx.rollback();
		} finally {
			em.close(); // em은 커넥션을 물고 있어서 꼭 완료되면 닫아줘야한다
		}
		emf.close();
	}
}
