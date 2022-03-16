## clone 재정의는 주의해서 사용하라



배열 copy

```java
int[] a = {1,2,3,4};
int[] b = a; // shallow copy
b = a.clone(); // deep copy
```



copy시 주의사항

```java
Laptop[] a = {new Laptop("그램 16인치", "삼성")};
Laptop[] b = a.clone();
b[0].setCompany("LG"); // a의 회사명도 삼성에서 LG로 변경됨
```

Object의 reference value를 참조했기 때문에 a[0] == b[0] 즉 둘이 같은 객체를 가리키고 있음



Why not use clone

- 객체의 복사본을 생성해 반환한다. 복사의 정확한 뜻은 클래스에 따라 다를 수 있고, 일반적인 의도는 다음과 같다

```java
x.clone() != x // 참
x.clone().getClass() == x.getClass() // 참
x.clone().equals(x) // 일반적으로 참
```



B extends A

- b.clone() 실행 -> super.clone() -> a.clone()을 실행한 결과를 가져옴 -> b는 b객체를 반환해야하는데 super의 결과는 A 객체임



쉬운 길이 있는데 돌아가지 말자

- conversion Constructor

```java
Public Yum(Yum yum) {...};
```

- conversion Factory

```java
Public static Yum newInstance(Yum yum) {...};
```



- 요약
  - Primitive type의 배열이 아니면 쓰지 말자
  - Copy Constructor or Copy Factory method를 활용하라
  - Cloneable을 확장하지 마라