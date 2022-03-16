## private 생성자나 enum Type으로 Singleton임을 보증하라



### 대표적인 Singleton Pattern



- public static member
  - INSTANCE가 초기화되고 나면 고정이 된다

```java
public class Speaker {
    public static final Speaker INSTANCE = new Speaker(); // 전부 대문자: 변하지 않은 고정 값으로 네이밍 (싱글톤이다)
    private Speaker() {} // 호출하지 못하도록 막음. 의도하지 않은 객체 생성을 막는다.
}
```



- private static final field
  - getInstance를 통해 instance를 가져올 수 있다.
  - 위에보다 장점이 많다고 생각
    - 캡슐화
    - 제너릭한 싱글톤 팩토리를 만들 때 제너릭을 응답으로 줄 수 있음 (변형을 가할 수 있는 점이 많다)

```java
public class Speaker {
    private static final Speaker INSTANCE = new Speaker();
    private Speaker(){}
    
    public static Speaker getInstance(){
        return INSTANCE;
    }
}
```



- 상황에 따라 synchronized나, lazy하게 instance를 생성하는 방법도 있다

```java
public class Speaker {
    private static Speaker instance;
    private Speaker(){}
    public static synchronized Speaker getInstance(){
        // 기타 다른 사항 체크
        if(instance == null){
            instance = new Speaker();
        }
        return instance;
    }
}
```



- Enum Type으로 Singleton Pattern을 사용할 수 있다
  - 책의 권장 방식
  - 직렬화 상황이나 리플렉션 공격에서 완전히 방어할 수 있음!
  - 보기에 부자연스러움
    - Enum의 의도가 이게 맞나?
    - 클래스 상속에는 사용이 불가능함
    - 팀내 합의가 필요하다 (혼란을 줄 수 있음)

```java
public enum Speaker{
    INSTANCE;
    private String message;
    public Speaker getInstance(){
        return INSTANCE;
    }
    public void setMessage(String message){
        this.message = message;
    }
    public String getMessage(){
        return message;
    }
}

// Client Code
Speaker speaker1 = Speaker.INSTANCE.getInstance();
speaker1.setMessage("안내 방송 중입니다");

Speaker speaker2 = Speaker.INSTANCE;
sout(speaker1.getMessage()); // 안내 방송 중입니다
sout(speaker2.getMessage()); // 안내 방송 중입니다
```



Singleton pattern에 대해 알아보았고, 항상 잘 숙지!!! 어떻게 돌아가는지 공부해라!

각 방법의 차이점에 대해 인지해두고 이를 상황에 맞게 선택해 사용할 수 있도록 하자

Enum 방식은 팀원들과 함께 고려해보는걸로 하자~~
