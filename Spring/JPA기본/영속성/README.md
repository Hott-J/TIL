### why JPA?

- SQL 중심적인 개발 ->  객체 중심적인 개발
- 생산성
- 유지보수
- 패러다임의 불일치 해결
  - 상속
  - 연관관계
  - 객체 그래프 탐색과 엔티티 신뢰 문제
  - 객체 비교
- 성능
  - 1차 캐시와 동일성 보장
  - 트랜잭션을 지원하는 쓰기 지연
  - 즉시 로딩과 지연 로딩
- 데이터 접근 추상화 벤더 독립성



### 구동방식?

- 먼저 `persistence.xml` 파일을 조회해서 설정에 맞게 DB를 구성합니다.
- DB에 접근할 때 매번 커넥션을 생성해주는 `EntityManagerFactory`를 생성합니다. 이는 각 DB당 하나만 생성해서 Application 전체에서 공유해야 합니다.
- 각 커넥션(액세스) 때마다 `EntityManager`가 생성되어 트랜잭션을 처리한 후 소멸됩니다. 이는 쓰레드 간에 공유하면 안되며 각각의 커녁션마다 생성하고 다 사용했다면 버려야 합니다.

```java
public static void main(String[] args) {
    // persistence.xml의 persistence-unit name 속성과 일치해야 한다.
    EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
    
    // 각 액세스마다 생성한다.
    EntityManager em = emf.createEntityManager();

    // JPA의 모든 데이터 변경은 트랜잭션 안에서 실행되어야 한다.
    EntityTransaction tx = em.getTransaction();
    tx.begin();

    try {
        /*
         * create new member
         */
        Member newMember = new Member();
        newMember.setId(1L);
        newMember.setName("memberA");
        em.persist(newMember);

        /*
         * read member
         */
        Member findMember = em.find(Member.class, 1L);
        System.out.println("findMember = " + findMember.getId() + ": " + findMember.getName());

        /*
         * update member
         */
        Member updateMember = em.find(Member.class, 1L);
        updateMember.setName("memberX");

        /*
         * delete member
         */
        Member deleteMember = em.find(Member.class, 1L);
        em.remove(deleteMember);

        /*
         * read all members by JPQL
         * SQL은 DB 테이블을 대상으로 쿼리를 작성하지만
         * JPQL은 객체를 대상으로 검색하는 객체 지향 쿼리이다.
         */
        List<Member> members = em.createQuery("select m from Member as m", Member.class)
                .getResultList();
        for (Member member: members) {
            System.out.println("member = " + member.getId() + ": " + member.getName());
        }

        // SQL을 모와서 한번에 보낸다.
        tx.commit();
    } catch (Exception e) {
        // error가 발생한다면 DB를 롤백한다.
        tx.rollback();
    } finally {
        // DB 커넥션을 닫는다.
        em.close();
    }

    emf.close();
}
```



### 영속성?

Entity를 영구 저장하는 환경이라는 의미로, 눈에 보이지 않는 논리적인 개념입니다. `EntityManage`를 통해서 `영속성 Context`에 접근합니다.



### 영속성 생명주기?

- `비영속(new/transient)`

  영속성 Context와 전혀 관계가 없는 새로운 상태를 의미합니다.

- `영속(managed)`

  JPA를 통해 객체가 영구 저장(DB에서 관리)된 상태를 의미합니다.

- `준영속(detached)`

  영속 상태였던 객체를 영속성 Context에서 분리한 상태를 의미합니다.

- `삭제(removed)`

  객체를 삭제한 상태를 의미합니다.

```java
// 객체를 생성: 비영속
Member member = new Member();
member.setId("membeA");
member.setName("Joon");

EntityManager em = emf.createEntityManager();
em.getTransaction().begin();

// 객체를 저장: 영속
em.persist(member);

// 객체를 분리: 준영속
em.detach(member);

// 객체를 제거: 삭제
em.remove(member);
```



### 장점?

- 1차 캐시

```java
Member member = new Member();
member.setId("memberA");

// 1차 캐시에 저장
em.persist(member);

// 1차 캐시에서 조회 (SELECT query 필요 x)
Member findMember1 = em.find(Member.class, "memberA");

// DB에서 조회 (SELECT query 실행)
Member findMember2 = em.find(Member.class, "memberB");
```

객체를 가져오는 방법은 먼저 1차 캐시에서 조회한 후, 캐시에 없다면 DB에 접근해서 조회합니다.



- 같은 `EntityManager`에서 비교하는 경우

```java
Member findMember1 = em.find(Member.class, "memberA");	// DB에서 조회 (SELECT query 실행)
System.out.println("findMember1 = " + findMember1.getId() + ": " + findMember1.getName());
// print "findMember1 = memberA: Joon"

Member findMember2 = em.find(Member.class, "memberA"); // 1차 캐시에서 조회 (SQL 필요 x)
System.out.println("findMembe2r = " + findMember2.getId() + ": " + findMember2.getName());
// print "findMember2 = memberA: Joon"

System.out.println("is Equal ? " + (findMember1 == findMember2));     // true
```



- 다른 `EntityManager`에서 비교하는 경우

```java
Member findMember1 = em1.find(Member.class, "memberA");	// DB에서 조회 (SELECT query 실행)
System.out.println("findMember1 = " + findMember1.getId() + ": " + findMember1.getName());
// print "findMember1 = memberA: Joon"

Member findMember2 = em2.find(Member.class, "memberA");	// DB에서 조회 (SELECT query 실행)
System.out.println("findMember2 = " + findMember2.getId() + ": " + findMember2.getName());
// print "findMember2 = memberA: Joon"

System.out.println("is Equal ? " + (findMember1 == findMember2));   // false
```



- 트랜잭션을 지원하는 쓰기 지연(transcational write-behind)

```java
EntityManager em = enf.createEntityManager();
EntityTransaction tx = em.getTransaction();
tx.begin();		// EntityManager는 데이터 변경 시 트랜잭션을 시작해야 한다.

em.persist(memberA);
em.persist(memberB);	// 여기까지 DB에 SQL을 보내지 않는다.

tx.commit();	// Commit하는 순간 DB에 SQL을 한 번에 보낸다.
```



- 변경 감지(Dirty checking)

```java
EntityManager em = enf.createEntityManager();
EntityTransaction tx = em.getTransaction();
tx.begin();

Member member = em.find(Member.class, "memberA");	// 영속 Entity 조회

member.setName("PSH");	// 영속 Entity 수정
// em.update(member)와 같은 코드가 추가로 필요하지 않다.

member.setName("psh");	// 영속 Entity 수정
// 아직까지는 SQL가 보내지지 않는다.

tx.commit();	// flush
```



![dirty_checking](https://user-images.githubusercontent.com/47052106/156872802-8a85940a-b317-4c44-9699-0564f15bff87.png)



### 영속성 개념 정리 코드

```java
EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");

EntityManager em1 = emf.createEntityManager();
EntityTransaction tx1 = em1.getTransaction();
tx1.begin();

Member member1 = em1.find(Member.class, "memberA");		// SELECT query 실행, em1의 1차 캐시에 저장
System.out.println("member1 = " + member1.getId() + ": " + member1.getName());
// print "member1 = memberA: Joon"

member1.setName("PSH");	// em1의 1차 캐시에 반영, UPDATE query 아직 실행 x
System.out.println("member1 = " + member1.getId() + ": " + member1.getName());
// print "member1 = memberA: PSH"

EntityManager em2 = emf.createEntityManager();
EntityTransaction tx2 = em2.getTransaction();
tx2.begin();

Member member2 = em2.find(Member.class, "memberA");		// SELECT query 실행, em2의 1차 캐시에 저장
System.out.println("member2 = " + member2.getId() + ": " + member2.getName());
// print "member2 = memberA: Joon" (위의 tx는 commmit되지 않았으므로 field가 update되지 않음)

tx1.commit();	// UPDATE query 실행
em1.close();

member2 = em2.merge(member1);	// em2의 1차 캐시에 반영, UPDATE query 아직 실행 x
System.out.println("member2 = " + member2.getId() + ": " + member2.getName());
// print "member2 = memberA: PSH"

tx2.commit();	// UPDATE query 실행 (실제로는 DB와 같은 객체이지만 1차 캐시의 스냅샷과 다르므로 flush)
em2.close();

System.out.println("is Equal ? " + (member1 == member2));
// print "is Equal ? false"

emf.close();
```

