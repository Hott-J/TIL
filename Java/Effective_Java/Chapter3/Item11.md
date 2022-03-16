### equals를 재정의하려거든 hashCode도 함께 재정의하라

- ==
  - value compare
  - primitive type일 때는 value compare
  - Reference type일 때는 주소가 같은지 비교
- equals()
  - 메서드의 의도: 같은 객체인지
  - Default : ==과 동일
  - Override하여 사용
- hashCode()
  - 논리적으로 같은 객체라면 같은 hashCode 값 반환



잘못된 예

Example: 안내방송을 위한 TTS (text to speak) 예약 Map

```java
Speaker speaker1 = new Speaker("수업 시작 시간입니다");
Map<Speaker, LocalTime> localTimeMap = new HashMap<>();
localTimeMap.put(speaker1, LocalTime.of(9,0));
// 수업 시작 시간을 10분 당기기로 하였다.

Speaker speaker2 = new Speaker("수업 시작 시간입니다.");
localTimeMap.put(speaker2, LocalTime.of(8,50));
```

실제로는 안내 방송이 8시 50분, 9시에 두번 울리게 된다



간단한 방식의 hash

```java
// 가장 심플하게 적용한다면
@Override
public int hashCOde() {
    int result = message.hashCode();
    return result;
}

// 속도를 고려 (Objects의 경우 속도가 아쉽다)
@Override
public int hashCode() {
    return Objects.hash(modelName, company);
}
```

속도가 많이 느려지면 lazy init, or caching을 고려하자! 또한 핵심 필드를 누락하지 말 것!



Objects.hash() (내부에서 Arrays.hash 출력)

```java
public static int hashCode (Object a[]) {
    if (a == null)
        return 0;
    
    int result = 1;
    
    for(Object element : a) 
        result = 31 * result +
        (element == null ? 0 : element.hashCode());
    
    return result;
}
```



Lombok을 사용하는 방법도 있다

```java
@EqualsAndHashCode
public class EqualsAndHashCodeExample {
    private transient int trasientVar = 10;
    private String name;
    private double score;
    private String[] tags;
    @EqualsAndHashCode.Exclude private int id; // 제외할 필드
}
```

전체 코드와 변환 되는 것은 Google에 Lombok EqualsAndHashCode를 검색해 Projectlombok 공식사이트의 링크를 확인할 것

특히나 @Data를 사용하고 있다면, Data는 다음과 같은 것들을 포함

- @Getter
- @Setter
- @RequiredArgsContructor
- @ToString
- @EqualsAndHashCode

불필요한 것들이 포함될 수 있으므로 제대로 알고 쓰자!!!



요약

- equals는 필요할 때 적재 적소에 활용
- equals를 재정의한다면 hashCode의 재정의 옵션이 아닌 필수다
- Lombok을 사용한다면 @Data, @EqualsAndHashCode는 반드시 동작 원리를 이해하자