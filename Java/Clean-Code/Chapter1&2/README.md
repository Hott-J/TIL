## 클린 코드와 그 첫걸음 네이밍



### 나쁜 코드

- 성능이 나쁨
- 의미가 모호
- 중복



깨진 유리창 법칙

- 나쁜 코드는 깨진 유리창처럼 계속 나쁜 코드가 만들어지도록 한다



팀 생산성 저하

- 기술 부채를 만들어 수정을 더 어렵게 만듦



새로운 시스템 구축

- 현 시스템을 유지보수하며 대체할 새로운 시스템 개발은 현실적으로 매우 어려움



짜는 이유?

- 촉박한 일정
  - 생산성 저하되므로 오히려 일정을 못 맞춘다

- 영향 범위가 넓어서
  - 건드렸다가 다른 부분에 버그가 발생할까봐
  - but 기술 부채는 부메랑처럼 돌아온다



### 클린 코드

- 의존성을 최대한 줄여야 유지보수가 쉽다
- 깨끗한 코드는 한 가지를 제대로 한다
- 깨끗한 코드는 단순하고 직접적이다
- 깨끗한 코드는 잘 쓴 문장처럼 읽힌다
- 명쾌한 추상화와 단순한 제어문으로 가득하다
- 성능이 좋은 코드
- 가독성이 좋은 코드 (의미 명확)
- 중복이 제거



보이스카우트 룰

- 전보다 더 깨끗한 코드로 만든다



### 의미가 분명한 이름 짓기

- 클래스화
- 루프 속 i j k 사용하지 않기
  - advanced for 문으로 대체
  - stream lambda 사용
  - i, j -> row, col / width, height 처럼 최대한 의미를 찾아보자
- 통일성 있는 단어 사용
  - Member / Customer / User
  - Service / Manager
  - Repository / Dao
  - 팀내 협의
- 변수명에 타입 넣지 않기
- 인터페이스와 구체클래스 네이밍
  - 인터페이스로 어떠한 구현체가 만들어지는지?



### Google Java Naming Guide

Package Naming Guide

- All lower cae, no underscores



Class Naming Guide

- UpperCamelCase

- 클래스는 명사, 명사구
- 인터페이스는 명사, 명사구, (형용사, ex: Readable)



Method Naming Guide

- LowerCamelCase
- 메서드는 동사, 동사구