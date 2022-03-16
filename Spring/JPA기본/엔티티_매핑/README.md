## Entity 매핑



### 객체와 테이블 매핑

- `@Entity`가 붙은 클래스는 JPA가 관리하며, 이를 Entity라고 합니다. Entity의 경우 기본 생성자가 필수이며 당연하게도 `final`과 같은 field가 있으면 안됩니다.
- `@Table`은 Entity와 매핑할 테이블 지정합니다. `name` 속성으로 매핑할 테이블 이름을 정할 수 있고, 기본값은 Entity 이름입니다. 이외에도 `catalog`, `schema`, `uniqueConstraints` 등의 옵션이 있습니다.



### Field와 Column 매핑

```java
@Entity
@Table(name = "MEMBER")
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "name", nullable = false)
    private String username;

    private Integer age;

    @Enumerated(EnumType.STRING)
    private RoleType roleType;

    @Temporal(TemporalType.TIMESTAMP)
    private Date createdDate;

    private LocalDateTime lastModifiedDate;

    @Lob
    private String description;

    @Transient
    private int temp;
}
```

- @Column

![column](https://user-images.githubusercontent.com/47052106/156873012-6286912a-398d-4545-baa1-408a14e6ecce.PNG)

- @Temporal

![@temporal](https://user-images.githubusercontent.com/47052106/156873022-ba86a647-ff72-4133-8394-242481ecb273.PNG)

- @Enumerated

![@Enumerated](https://user-images.githubusercontent.com/47052106/156873039-5f54109e-dcb1-4d34-bb23-9c8f251f593e.PNG)

자바 `enum` 타입을 매핑할 때 사용합니다. 다만 추후 요소가 추가될 경우를 대비해, DB 공간을 조금 더 차지하더라도 `EnumType.STRING`을 사용해야 합니다.



- @Lob
  - DB의 `BLOB`, `CLOB` 타입과 매핑합니다. 이 annotation에는 별도로 지정할 수 있는 속성이 없습니다. 매핑하는 Field 타입이 문자면 `CLOB`, 나머지는 `BLOB`으로 매핑합니다.



- @Transient
  - 주로 메모리상에서만 임시로 어떤 값을 보관하고 싶은 경우처럼, 매핑하지 않을 Field에 사용합니다.



### 기본 Key 매핑

- 직접 할당

```java
@Entity
public class Member {
    @Id
    private Long id;
}
```

- 자동 생성

  - IDENTITY

  ```java
  @Entity
  public class Member {
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
  }
  
  EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
  
  EntityManager em = emf.createEntityManager();
  EntityTransaction tx = em.getTransaction();
  tx.begin();
  
  Member member = new Member();
  em.persist(member);
  // 원래는 아직은 SQL이 보내지지 않지만, IDENTITY 전략을 사용할 경우 바로 SQL이 실행된다.
  
  tx.commit();
  ```

- 다만 여기서 문제는 해당 Entity를 DB에 저장해야만 기본 Key를 알 수 있다는 점입니다.  JPA는 트랜잭션을 Commit 하기 전까지 1차 캐시에 Entity들을 보관하는데, `IDENTITY` 전략으로 Key가 자동 생성된다면 Commit하기 전까지 Key를 알 수 없게 되어, 1차 캐시 활용을 제대로 못하기 때문입니다. 따라서 예외적으로 이 전략으로 설정된 Entity의 경우, JPA는 `persist()` 메서드 호출되면 바로 SQL을 보내서 Key를 받아옵니다

  

  - SEQUENCE

  ```JAVA
  @Entity
  @SequenceGenerator(
      name = "MEMBER_SEQ_GENERATOR",
      sequenceName = "MEMBER_SEQ",	// 매핑할 DB Sequence 이름
      initialValue = 1, allocationSize = 50)
  public class Member {
      @Id
      @GeneratedValue(
          strategy = GenerationType.SEQUENCE,
          generator = "MEMBER_SEQ_GENERATOR")
      private Long id;
  }
  
  EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
  
  EntityManager em = emf.createEntityManager();
  EntityTransaction tx = em.getTransaction();
  tx.begin();
  
  Member member1 = new Member();
  em.persist(member1);
  // call next value for MEMBER_SEQ: DB Sequence로 부터 정해진 Size만큼 받아온다.
  System.out.println("member = " + member1.getId());
  // print "member = 1": 할당 가능한 범위 내에서 Entity의 Key Field에 값 순서대로 설정
  
  Member member2 = new Member();
  em.persist(member2);
  // call 필요 없음
  System.out.println("member = " + member2.getId());
  // print "member = 2": 할당 가능한 범위 내에서 Entity의 Key Field에 값 순서대로 설정
  
  Member member3 = new Member();
  em.persist(member3);
  // call 필요 없음
  System.out.println("member = " + member3.getId());
  // print "member = 3": 할당 가능한 범위 내에서 Entity의 Key Field에 값 순서대로 설정
  
  tx.commit();
  ```

  

- TABLE

```java
@Entity
@TableGenerator(
    name = "MEMBER_SEQ_GENERATOR",
    table = "MY_SEQUENCES",
    pkColumnValue = "MEMBER_SEQ", allocationSize = 1)
public class Member {
    @Id
    @GeneratedValue(
        strategy = GenerationType.TABLE,
        generator = "MEMBER_SEQ_GENERATOR")
    private Long id;
}
```



- AUTO
  - 기본 전략으로, DB Dialect에 따라 자동 지정됩니다



### 연관관계 매핑 기초

