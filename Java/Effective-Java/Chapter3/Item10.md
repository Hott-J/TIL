### equals의 일반 규약을 지켜 재정의하라

```java
public boolean equals(Object o) {
    return this == o;
}
```



Intellij를 통해 생성한 equals의 override

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    LaptopDto laptopDto = (LaptopDto) o;
    return Object.equals(modelName, laptopDto.modelName) &&
        Object.equals(company, laptopDto.company);
}

@Override
public int hashCode() {
    return Objects.hash(modelName, company);
}
```



Equals가 만족해야하는 것

- [reflexivity] e.equals(x) => true
- [symmetry] x.equals(y) => true then y.equals(x) => true
- [transitivity] x.equals(y) => true, y.equals(z) => true then x.equals(z) => true
- [consistency] x.equals(y)를 여러번 호출해도 항상 결과 같게
- [not null] if x is not null, then x.equals(null) => false



Equals를 override하지 않는 것이 최선일 때

- 각 인스턴스가 본질적으로 고유
- 인스턴스의 논리적으로 같음을 사용할 일이 없을 때
- 상위 클래스에서 재정의한 equals가 하위 클래스에서도 동일하게 맞을 때
- private Class (equals를 부를 일이 없음)

```java
public class ClassScore {
    private List<Score> scoreList;
}

public class Score {
    private String subjectName;
    private int score;
}
```



Equals의 전형적인 검사 패턴

- ==를 통해 input이 자기 자신의 참조인지
- Instance of를 통해 input의 타입이 명확한지 (getClass)
- 위를 통해 검사한 객체를 올바른 타입으로 형변환
- 핵심 필드들이 모두 일치하는지
- [not null] if x is not null, then x.equals(null) => false

```java
@Override
public boolean equals(Object o) { // input은 무조건 Object
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    LaptopDto laptopDto = (LaptopDto) o;
    return Object.equals(modelName, laptopDto.modelName) &&
        Object.equals(company, laptopDto.company);
}
```



재정의 주의사항

- 만족해야 하는 조건을 만족시켰는가
- Equals를 재정의 할 때 hashCode도 재정의하였는가
- Equals의 input이 Object인가 (Overriding 하였는가)
- 핵심 필드들이 모두 일치하는지
- [not null] if x is not null, then x.equals(null) => false