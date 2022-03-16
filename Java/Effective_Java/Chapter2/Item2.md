## 많은 파라미터가 있는 생성자는 빌더를 고려하라

```java
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int solium;
    private final int carbohydrate;
}
```

Pattern 1 : 여러 개의 생성자를 둔다

- 4개, 5개, 6개 파라미터를 갖는 생성자가 있다고 가정
- 필수요소 파라미터가 하나 추가됨 (int형으로 타입 동일)
  - 4개짜리 생성자가 5개짜리 생성자로 됨 (필수 생성자) NutritionFacts(10,10,10,10,10)
  - 기존에 5개 파라미터를 갖는 생성자가 있었기 때문에, 추가된 파라미터로 이루어진 생성자인지 기존의 5개짜리 생성자인지 인지할 수 없음

Pattern 2 : Java beans Pattern (Setter)

- 코드가 루즈해져서 사용X 
- set이 너무 많이 호출되면 너무 길어지고 읽기 어려워짐



Builder를 직접 만들었을 때 (Lombok 사용 X)

- 꼭 한번 직접 만들어봐라!

```java
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    
    public static class Builder {
        private final int servingSize;
        private final int servings;
        private final int calories = 0;
        public Builder(int servingSize, int servings) { // 필수 요소를 생성자를 통해 주입
            this.servingSize = servingSize;
            this.servings = servings;
        }
        public Builder calories(int val) { // 빌더 체인으로 칼로리 추가, 앞으로 필수 요소 아닌것을 점점 더 추가
            calories = val;
            return this;
        }
        public NutritionFacts build() {
            return new NutritionFacts(this);
        }
    }
}

// client Code
NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8)
    .calories(100).build();
```



Lombok을 통하면 훨씬 더 Simple

- 실전성이 더 좋다고 생각

```java
@Data
@Builder(builderMethodName = "hiddenBuilder")
public class NutrionFacts {
    private final int servingSize;
    private final int servings;
    @Builder.Default private final int calories = 0;
    @Builder.Default private final int fat = 0;
    @Builder.Default private final int solium = 0;
    @Builder.Default private final int carbohydrate = 0;
    
    public static NutritionFactsBuilder builder(int servingSize, int servings) {
        return hiddenBuilder()
            .servingSize(servingSize)
            .servings(servings);
    }
}
```



- 장점
  - 상속받은 클래스의 빌더가 정의한 빌드 메서드가 상위 메서드의 타입을 return 하는 것이 아닌 자신의 타입을 return 한다
- 단점
  - 빌더를 항상 만들어야하기 때문에 생성 비용이 무조건 발생
  - 점층적 생성자 패턴 (Argument를 여러 개 가진 생성자) 보다 장황하여 적은 갯수의 파라미터일 경우 오히려 좋지 않을 수 있다
    - 3~4개정도는 인간이 식별하기 크게 불편하지 않아 생성자를 사용하는 편
    - 빌더 만들고 빌더 메서드가 들어가야하므로 생성자 대비해서 라인이 하나 이상 추가될 수 밖에 없으므로, 판단해서 코드가 지저분해질지 고려하고 사용