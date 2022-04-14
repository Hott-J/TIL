## Immutable class

1. 상태 변경 method (ex. Set method) 제공하지 않는다
2. Class 확장하지 않도록 한다 (ex. Final을 사용)
3. 모든 field를 final로 선언 (thread-safe)
4. 모든 field를 private로 선언 (캡슐화)
5. 자신을 제외하고는 아무도 가변 컴포넌트에 접근할 수 없도록 한다



```java
@Getter
class AddressInfo {
    private String address;
}

@AllArgsConstructor
final class User {
    private final String phone;
    private final List<AddressInfo> addressInfoList;
    
    public List<String> getAddressList() {
        // 내부에 가변 컴포넌트인 주소 정보를 숨겼다
        return addressInfo.stream()
            .map(AddressInfo::getAddress).collect(Collector.toList());
    }
}
```



BigInteger (Immutable class example)

```java
BigInteger bigInteger = new BigInteger("10000");
sout(bigInteger.add(new BigInteger("100"))); // 10100 (새로운 인스턴스 반환: immutable하므로)
sout(bigInteger); // 10000
```

Immutable class의 조건

- Thread-safe
- failure atomicity: 예외가 발생 후에도 유효한 상태
- 값이 다르면 무조건 독립적인 객체로 생성되어야 함

중간 단계 (객체가 완성 중인 상태)를 극복하기 위한 방법

- Static factory method를 통해 new instance를 생성해 response
  - StringBuilder



Immutable Vo

- Person Entity

```java
@Entity
@Setter
@Getter
public class Person {
    @Id
    private Long id;
    private String name;
    private float height;
}
```

- PersonVo (Immutable)

```java
@Getter
public class PersonVo {
    private final String name;
    private final float height;
    
    // 생성자도 막아둔다 -> static final로만 인스턴스 생성하게끔 하기 위함. 생성자를 열어둔다면 setter를 만들어낼 위험이 있다
    private PersonVo(String name, float height) {
        this.name = name;
        this.height = height;
    }
    
    // factory
    public static final PersonVo from(Person p) {
        return new PersonVo(p.getName(), p.getHeight());
    }
}
```

값이 변하지 않는 객체라면 다음과 같이 불변성을 강제하는 것 또한 방법이다



- 주의사항
  - 습관적으로 Setter를 만들지 말자
  - Class는 꼭 필요한 경우가 아니면 불변이어야 한다 (특히 단순한 Value Object는 더 그러함)
  - 모든 클래스가 불변일 수 없지만, 변경할 수 있는 부분을 최대한 줄여보자