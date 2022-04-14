## 클래스와 멤버의 접근 권한을 최소화하라



Public class의 instance field

- Public 으로 열 경우 Thread-safe 하지 못하다. (Lock 류의 작업을 걸 수 없음)
- 꼭 필요한 상수라면 예외적으로 public static final로 공개할 수 있다
  - ex) TMAX_INVESTMENT_PAGE
- [주의사항] public static final Thing[] Values = {...}는 수정이 가능하다

```java
public class Capsule {
    private String name;
    private int cost;
    public float getDolorCost(){
        return 1050/cost;
    }
    public int getWonCost(){
        return cost;
    }
}
```



배열의 두 가지 해결책

``` java
private static final PAGE[] PAGE_INFO = {...};
public static final List<PAGE> VALUES =
    Collections.unmodifiableList(Arrays.asList(PAGE_INFO));
```

배열을 private으로 만들고, 불변 리스트를 추가

- 읽기 전용으로 response
- 원본이 바뀔 경우 같이 변경됨



```java
public static final PAGE[] values(){
    return PAGE_INFO.clone();
}
```

배열을 private로 두고, 복사본을 반환하는 public method

- 해당 시점으로 clone 됨
- 원본이 바뀔 경우 같이 변경되지 않음