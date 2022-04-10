## MicroService와 Spring Cloud 소개

IT 역사

- 하드웨어 -> 분산 -> 탄력, 클라우드

  

Antifragile

- Auto scaling

- Microservices

- Chaos engineering

- Continuous deployments

  

Cloud Native Architecture

- 확장 가능한 아키텍처
- 탄력적 아키텍처
- 장애 격리



Cloud Native Application

- MicroServices
- CI/CD
  - 지속적인 통합 CI
    - 통합 서버, 소스 관리, 빌드 도구, 테스트 도구 (Jenkins, Team CI, Travis CI)
  - 지속적인 배포 CD
- DevOps
- Containers



Monolithic vs MSA

모놀리식

- 모든 업무 로직이 하나의 애플리케이션 형태로 패키지 되어 서비스
- 애플리케이션에서 사용하는 데이터가 한곳에 모여 참조되어 서비스 되는 형태

MSA

- 작은 규모의 여러 서비스들의 묶음
- 서비스 인터페이스로만 통신 (외부에 공개)

모든 것이 MSA?

- X
- 어느정도 변화가 생길 것인가?
- 독립된 라이프 사이클 (서비스 경계가 명확한가)
- 확장성이 독립적인가
- 격리된 오류
- 외부 종속성이 최소화되어있는가
- 여러가지 프로그래밍, 여러가지 기술이 지원되는가

