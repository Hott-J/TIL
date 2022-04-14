## Comparable을 구현할지 고려하라



compareTo의 규약 (equals와 비슷)

- 객체와 주어진 객체의 순서를 비교한다
- 이 객체가 주어진 객체보다 작으면 음의 정수, 같으면 0, 크면 양의 정수를 반환. (-1,0,1) 비교할 수 없을 땐 ClassCastException

```java
sgn(x.compareTo(y)) == - sgn(y.compareTo(x));
x.compareTo(y) > 0 && y.compareTo(z) > 0 then x.compareTo(z) > 0;
x.compareTo(y) == 0 then sgn(x.compareTo(z)) == sgn(y.compareTo(z));
// 권고는 아니지만 Recommend
x.compareTo(y) == 0 then x.equals(y) == true;
```

복잡해 보이지만 하나씩 뜯어보면 상식적인 이야기이다



Java7 이후의 compare

```java
// 이전
1<2;
Double.compare(1.2,3.4);
Float.compare(1.2f,3.4f);

// 이후
Integer one = 1;
one.compareTo(2);
```



정렬 예제

```java
public class Person {
    private int age;
    private String name;
    private double height;
}

// 조건: 1순위: 나이 순, 2순위: 키, 3순위: 이름
```

- compareTo의 구현

```java
// factory
// autoBoxing이 일어날 일이 없음
public int compareTo(Person p) {
    int result = Integer.compare(age, p.age);
    if(result == 0) {
        result = Double.compare(height, p.height);
    }
    if(result == 0) {
        result = name.compareTo(p.name);
    }
    return result;
}
```

- compareTo의 또다른 구현 (Comparator 생성 method)

```java
private static final Comparator<Person> COMPARATOR =
    Comparator.comparingInt(Person::getAge)
    .thenComparingDouble(Person::getHeight)
    .thenComparing(person -> person.getName());
public int compareTo(Person p) {
    return COMPARATOR.compare(this, p);
}
```



- 요약
  - 필요하다면 적절하게 Comparable를 구현하여 compareTo의 이점을 누릴 수 있다
  - 하지만 정렬의 기준이 고정적이 아니라면, 다른 방식(method, service를 통한 조건 별 ordering)을 고려해볼 수 있다