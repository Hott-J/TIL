### Instance화를 막으려면 private 생성자를 사용하라

Instance를 막는 Util Class



잘못된 예제

```java
public class PatternUtil {
    
    private static final String PATTERN = "/b[A-Z0-9._%+-/";
    private PatternUtil(){}
    
    public static boolean isEmailValid(String email) {
        return email.matches(PATTERN);
    }
    
    // 불행의 시작
    public String getPattern(){
        return PATTERN;
    }
}
```

나와 팀원의 실수를 줄이기 위해 조금 귀찮더라도 생성자를 막자!!!

일반적으로 Util Class 처럼 관용적으로 Instance화를 하지 않을 거라고 모두가 이미 알고 있는 경우는 생략하기도함

