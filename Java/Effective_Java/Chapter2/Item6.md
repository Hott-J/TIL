### 불필요한 객체 생성 금지

Boxing Type 대신 Primitive Type을 권장한다

```java
public static long sum() {
  Long sum = 0L; // Boxing Type (원시타입)
  for(long i = 0; i<=Integer.MAX_VALUE; i++) {
    sum+=i; // 불필요하게 Long 인스턴스가 생성됨
  }
  return sum;
}

// 10배 정도 속도 빠름
public static long sum() {
  long sum = 0L; // Primitive Type
  for(long i = 0; i<=Integer.MAX_VALUE; i++) {
    sum += i;
  }
  return sum;
}
```



Util Class에서 또한 primitive Type을 권장

참 거짓을 response 하는데 Boxing Type을 사용하는 것은 낭비일 수 있다

```java
public class PhonePatternUtil {
  private final String pattern;
  
  public boolean isValid(String phone) {}
}
```



그렇다고 항상 primitive type이 옳은가?

- 아니다

대표적인 Null Case에 대해 살펴보자

- 물건의 가격이라고 생각

```java
int price; // primitive

Integer price; // Boxing

// 0의 의미는 증정품 등의 사유로 0원일 수 있고,
// Null의 경우 가격이 아직 정해지지 않았다 생각될 수 있다
```

적절한 상황에 따라 판단해서 사용해라



주의해야 할 내장 메서드

```java
static boolean isEmailValid(String s) {
  return s.matches("[a-zA-Z0-9.-]\\\.[a-zA-Z]{2,6}$")
}

// String.java
public boolean matches(String expr) {
  return Pattern.matches(expr, this);
}

// Pattern.java
public static boolean matches(String regex, CharSequence input) {
  Pattern p = Pattern.compile(regex); // validation 할 때 마다 패턴 새로 생성
  Matcher m = p.matcher(input);
  return m.matches();
}
```

isEmailValid는 단순 검증비교가 아니라 계속 객체를 생성하고 있었네??

```java
// 최적화 코드
public class EmailUtil {
  private static final Pattern EMAIL = 
    Pattern.compile("[a-zA-Z0-9.-]\\\.[a-zA-Z]{2,6}$");
  static boolean isEmailValid(String s) {
    return EMAIL.matcher(s).matches();
  }
}
```



- 메서드 내부를 보고 어떤식으로 동작하는지 항상 간단하게라도 보는 습관을 곁들이자!!!



생각해봐야 할 것

- 무심결에 인스턴스를 과도하게 생성하지는 않았는지
- Primitive Type과 Boxing Type을 의도하고 사용하였는지