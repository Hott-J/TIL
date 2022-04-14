## 생성자 대신 정적 팩토리 메소드를 고려하라

```java
public class Laptop {
    private String modelName;
    private String company;
}

// constructor
public Laptop(String modelName, String company) {
	this.modelName = modelName;
    this.company = company;
}

// Static Factory Method
// 만든 것의 재료를 볼 수 없으면 from, 만든 것의 재료를 볼 수 있으면 of
// 객체를 파라미터로 받으면, 객체의 내부를 볼 수 없으므로 from Naming
// 모델명과 회사명을 명시적으로 파라미터를 받으므로 of naming 사용
public static Laptop ofModelNameAndCompany(String modelName, String company) {
    Laptop laptop = new Laptop();
    laptop.company = company;
    laptop.modelName = modelName;
    return laptop;
}
```

## 

### 생성자 사용 이유?

Form to Entity Class (API request parameter)

API request with LaptopForm

```java
// input의 경우는 Form으로 명시
public class LaptopForm {
    private String name;
    private String corp;
}

// response를 DTO로 명시
@PostMapping(value = "/add")
public LaptopDto addLapTop(@RequestBody LaptopForm laptopForm) {}

// Laptop으로 convert
@Entity
public class Laptop {
    private Long id;
    private String modelName;
    private String company;
    
    public static Laptop from(LaptopForm laptopForm) {
        Laptop laptop = new Laptop();
        laptop.modelName = laptopForm.getModelName();
        laptop.company = laptopForm.getCompany();
        return laptop;
    }
}
```



Entity to Dto Class (API response parameter)

```java
public class LaptopDto {
    private String modelName;
    private String companyName;
    
    // 자연스럽게 id 필드가 사라짐
    // 필요하지 않은 엔티티 요소를 제거
    public static LaptopDto from(Laptop laptop) {
        LaptopDto laptopDto = new LaptopDto();
        laptopDto.company = laptop.getCompany();
        laptopDto.modelName = laptop.getModelName();
        return laptopDto;
    }
}
```



생성자 대신 Static Factory Method를 고려하라 (항상 말고, 컨버팅할때 주로 사용, 단순 주입은 생성자를 사용하는데, 개인이 알아서 잘 판단해라)

- 장점
  - 이름을 가질 수 있다.
  - Simple하고 명확하게 사용
  - 인스턴스를 매번 생성할 필요는 없다
    - Flyweight pattern - Collection Object
    - Singleton pattern - Single Object
    - Singleton의 경우 한 객체, Flyweight의 경우 multiple한 객체를 다룬다

- 단점
  - Static Factory method만 제공하면 생성자가 없을 수 있어 상속받은 Class를 만들 수 없다
  - 프로그래머에게 인지가 잘 되지 않을 수 있다 (생성자가 익숙하므로)