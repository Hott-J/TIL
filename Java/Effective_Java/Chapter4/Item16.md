## public class에서는 get method를 통해 필드에 접근하라



캡슐화가 유용한 시나리오 케이스

```java
public class ItemInfo {
    public String name;
    public String price;
}
```

최초에는 name과 price를 response할 수 있었음

허나 내부 정책이 바뀌어 내부에선 price 대신 cost라는 용어를 사용하고자 함

밖에는 그대로 price로 노출이 되어야 함

내부에 어떤 데이터로 관리를 하고 있는지 알 수 없게 한다



캡슐화

- 조금 더 strict한 규정을 적용하고 싶다면 name의 set을 없앨 수 있다
  - final과 비슷한 효과
  - final + No set 이중화해놓는게 제일 좋다
- 생성자로만 name을 주입받게끔 한다

```java
public class ItemInfo {
    private final String name;
    private int price;
    public ItemInfo(String name, int price){
        this.name = name;
        this.price = price;
    }
    public String getName(){
        return name;
    }
    public void setPrice(int price){
        this.price = price;
    }
    public int getPrice(){
        return price;
    }
}
```



- 요약
  - 클래스와 멤버의 접근 권한을 최소화
  - public class에서는 get method를 통해 필드에 접근



- 생각해볼만한 점
  - 캡슐화는 꼭 한번 다시 점검
  - 접근제어자는 습관적으로 항상 최소로 사용