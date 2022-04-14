

### Resource를 직접 명시하지 말고, DI를 사용하라

@Configuration

- @Configuration은 @Component를 포함하고 있고, 
- @Component가 Singleton이기에 자연스럽게 @Configuration 또한 Singleton!

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component
public @interface Configuration {
}
```



Config class 내부에 직접 정의하여 사용은 이제 그만!

- 여러 자원을 활용해야 할 경우 적합X
- 이 상황에선 환경 (live, dev, local) 별로 다른 값들이 들어가야 할 때 적절하지 않다

```java
// 잘못된 예제
@Configuration
public class TmaxConfig {
    private static final String ADDRESS = "성남시 분당구"; // 서버별로 변경된다면 적절하지 않음
    private static final zipcode;
    public TmaxConfig() {
        this.ADDRESS = "성남시 분당구";
    }
}
```

```yml
# application.yml
tmax:
	address: '성남시 분당구'
```

```java
@Configuration
public class TmaxConfig {
    @Value("${tmax.address}")
    private String address;
}
```



Constructor Injection의 경우 Test, flexibility를 높일 수 있다

- 고정해 놓은 값에 비해 훨씬 유연해진 class (pattern Injection 가능)
- Test code 작성 시 injection 하기도 편리

```java
public class PhonePatternChecker {
    private final String pattern;
    
    public PhonePatternChecker(String pattern) {
        this.pattern = pattern;
    }
   
    public boolean isValid(String phone) {}
}
```



- 생각해 봐야 할 것
  -  Config Class를 생각없이 사용하고 있지는 않았는지?
  - Singleton을 이해하고 있는지?
  - DI를 잘 이해하고 있는지?