package jpabook.jpashop;

import jpabook.jpashop.domain.Order;
import jpabook.jpashop.domain.OrderItem;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class JpaMain {

    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello"); // 애플리케이션 로딩 시점에 하나 생성
        EntityManager em = emf.createEntityManager(); // 엔티티 매니저 꺼냄. 트랜잭션 한 단위마다 만들어줘야한다
        // code
        EntityTransaction tx = em.getTransaction(); // JPA는 트랜잭션 안에서 데이터변경이 일어나야한다.
        tx.begin(); // 트랜잭션 시작

        try {
            Order order = new Order();
            order.addOrderItem(new OrderItem());
            tx.commit(); // 잘되면  커밋
        } catch(Exception e){
            tx.rollback(); // 문제시 롤백
        } finally {
            em.close(); // 작업 끝나면 엔티티매니저 닫아줌
        }
        emf.close();
    }
}
