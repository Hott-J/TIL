### 다 쓴 객체 참조를 해제하라

Array를 극단적으로 낭비한 예제 (극단적)

- Array[0], Array[1], Array[2]에서 size를 줄여 Array[2]를 없앤다하더라도 참조가 그대로이기 때문에Array[2]가 참조하고 있던 Object또한 살아있다.

우아하게 참조를 해제하는 법

- 유효 스콮 밖으로 넘어가면 자동으로 GC의 대상이 된다 (Reachable -> Unreachable)
- Unreachable Object가 되었을 때 (스택 영역과 연결 해지, 메서드 종료하여 더 이상 사용 X)



생각해봐야 할 것

- Array를 잘 쓰고 있었는지?
- 메모리 구조에 대해 이해?
  - 힙, 스택, 메서드 영역 등
- GC가 동작하는 원리?
- JVM?