

### toString을 항상 재정의하라



toString의 default value

- className@16진수 hashcode



toString의 알반 규약

- 간결하고 사람이 읽기 쉬운 형태의 유익한 정보



Lombok의 @ToString

```java
@AllArgsConstructor
@ToString
public class Laptop {
    private String modelName;
    private String company;
}

sout.println(new Laptop("그램 16인치", "삼성"));

// output: Laptop(modelName=그램 16인치, company=삼성)
```



불필요한 변수가 있을 경우(1)

```java
@AllArgsConstructor
@ToString(exclude = {"modelName"})
public class Laptop {
    private String modelName;
    private String company;
}

sout.println(new Laptop("그램 16인치", "삼성"));

// output: Laptop(company=삼성)
```



불필요한 변수가 있을 경우(2) - better

```java
@ToString
public class Laptop {
    @ToString.Exclude private String modelName; // 변수명에 명시
    private string company;
}
```

유지보수 측면에서 명시적으로 눈으로 바로 확인 가능해서 더 명료하다고 생각함



StringBuilder를 사용하는 방법

```java
@Override
public String toString() {
  StringBuilder builder = new StringBuilder();
  builder.append("modelName=");
  builder.append(modelName);
  builder.append(", company=");
  builder.append(company);
  return builder.toString();
}
```



StringBuilder를 메서드 체인 형식으로 사용하는 방법

```java
@Override
public String toString() {
  StringBuilder builder = new StringBuilder();
  builder.append("modelName=").append(modelName).append(", company=").append(company);
  return builder.toString();
}
```



Apache Commons의 Commons Lang Library

```java
@Override
public String toString() {
  return toStringBuilder.reflectionToString(this);
}
```



JPA 양방향 연관관계시 toString 사용 주의

```java
@Entity
@ToString
public class Member {
    @ManyToOne
    @JoinColumn(name = "TEAM_ID")
    private Team team;
}

@Entity
@ToString
public class Team {
    @OneToMany(mappedBy = "team")
    private List<Member> members = new ArrayList<>() ; 
}
```

member.toString() -> team.toString() -> member.toString() ... 무한 루프

- toStringBuilder 클래스로 해결

```java
@Entity
public class Member {
    @ManyToOne
    @JoinColumn(name = "TEAM_ID")
    private Team team;
  
    @Override
    public String toString() {
        return ToStringBuilder
            .reflectionToString(this, ToStringStyle.MULTI_LINE_STYLE);
    }
}

@Entity
public class Team {
    @OneToMany(mappedBy = "team")
    private List<Member> members = new ArrayList<>(); 
  
    @Override
    public String toString() {
        return ToStringBuilder
            .reflectionToString(this, ToStringStyle.MULTI_LINE_STYLE);
    }
}
```



요약

- 로그를 찍을 일이 있을 것 같으면 귀찮아하지 말고 toString을 overriding 하자
- 전부 다 toString으로 찍지 말고, 필요한 것 위주로 작성
- Lombok은 toString을 만들기 귀찮은 개발자들이 성실하게 toString 구현하도록 유인할 수 있다

- Lombok 사용시 주요 옵션을 공식 홈페이지에서 확인할 것 (ex: exclude)