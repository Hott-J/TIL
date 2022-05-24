# Logging



*운영시스템에서는 System.out.println()과 같은 시스템 콘솔을 사용하지 않음*

**System.out.println()은 무조건 전부 출력됨**

**로깅은 로깅레벨을 설정하여 어느 레벨부터 보여지는지 설정 가능**



**로깅 라이브러리**

- spring boot starter embedded
- SLF4J
- Logback
- 이것들을 통합해서 인터페이스로 제공하는 것이 바로 SLF4J, 구현체가 Logback



**로그 선언**

```java
// 코드 기반
private Logger log = LoggerFactory.getLogger(getClass()); 
private static final Logger log = LoggerFactory.getLogger(Xxx.class);

// 애노테이션 기반
@Slf4j
```



**로그가 출력되는 포멧 확인 **

- 시간, 로그 레벨, 프로세스 ID, 쓰레드 명, 클래스명, 



**로그 레벨 설정을 변경**

- Level: `TRACE > DEBUG > INFO > WARN > ERROR`
- 개발 서버는 debug
- 운영 서버는 info

```properties
#전체 로그 레벨 설정(기본 info)
logging.level.root=info
#hello.springmvc 패키지와 그 하위 로그 레벨 설정
logging.level.hello.springmvc=debug
```



**올바른 로그 사용법**

`log.debug("data=" + data)`

- 로그 출력 레벨을 info로 설정해도 해당 코드에 있는 "data="+data가 실제 실행이 되어 버린다. 결과적으로 문자 더하기 연산이 발생한다

`log.debug("data={}, data")`

- 로그 출력 레벨을 info로 설정하면 아무일도 발생하지 않는다. 따라서 앞과 같은 의미없는 연산이 발생하지 않는다.



**로그 사용시 장점**

- 쓰레드 정보, 클래스 이름 같은 부가 정보를 함께 볼 수 있고, 출력 모양을 조정할 수 있다. 
- 로그 레벨에 따라 개발 서버에서는 모든 로그를 출력하고, 운영서버에서는 출력하지 않는 등 로그를 상황에 맞게 조절할 수 있다. 
- 시스템 아웃 콘솔에만 출력하는 것이 아니라, 파일이나 네트워크 등, 로그를 별도의 위치에 남길 수 있다. 특히 파일로 남길 때는 일별, 특정 용량에 따라 로그를 분할하는 것도 가능하다. 
- 성능도 일반 System.out보다 좋다. (내부 버퍼링, 멀티 쓰레드 등등) 그래서 실무에서는 꼭 로그를 사용해야 한다.



**참고**

- SLF4J - http://www.slf4j.org 
- Logback - http://logback.qos.ch
- Spring Boot가 제공하는 로그 기능
  - https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#boot-features-logging