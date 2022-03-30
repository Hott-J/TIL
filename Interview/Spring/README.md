# Spring

## Table of Contents
* [MSA](#msa)
* [스프링의 버전별 차이](#스프링의-버전별-차이)
* [스프링과 스프링 부트 차이](#스프링과-스프링-부트-차이)
* [IoC](#ioc)
* [DI](#di)
* [AOP](#aop)
* [스프링 MVC 구조](#스프링-mvc-구조)
* [스프링 MVC 처리 과정](#스프링-mvc-처리-과정)
* [MVC 1과 MVC 2의 차이](#mvc-1과-mvc-2의-차이) *
* [Servlet](#servlet) *
* [디스패처 서블릿](#디스패처-서블릿)
* [디스패처 서블릿으로 인한 web.xml 역할 축소](#디스패처-서블릿으로-인한-webxml-역할-축소)
* [필터와 인터셉트 차이](#필터와-인터셉트-차이)
* [스프링 어노테이션](#스프링-어노테이션) *
* [DAO](#dao)
* [DTO](#dtp)
* [ORM](#orm)
* [JPA](#jpa)
* [Hibernate](#hibernate)
* [ORM, JPA, Hybernate 장단점](#orm-jpa-hybernate-장단점) *
* [Mybatis](#mybatis)
* [Mybatis, JPA 차이](#mybatis-jpa-차이) *
* [Spring JDBC](#spring-jdbc)

## MSA
* Microservice Architecture
* 모든 시스템의 구성요소가 한 프로젝트에 통합되어 있는 Monolithic Architecture(모놀리식 아키텍쳐)의 한계점을 극복하고자 등장
* 1개의 시스템을 독립적으로 배포 가능한 각각의 서비스로 분할한 것
* 각각의 서비스는 RESTful API를 통해 데이터를 주고받으며 1개의 큰 서비스를 구성

## 웹 서비스 동작 원리
* 헬로 월드가 출력하는 방법
* 클라이언트와 서버의 요청과 응답
* 브라우저가 클라이언트, 스프링 부트가 서버
* 로컬호스트의 8080포트에 톰캣이 수행

## 스프링의 버전별 차이

## 스프링과 스프링 부트 차이
* 스프링: 자바 플랫폼을 위한 오픈소스 애플리케이션 프레임워크. 엔터프라이즈 애플리케이션을 보다 쉽게 만들 수 있다
  * DI, IOC를 이용해서 객체간의 결합도를 낮게
  * 엔터프라이즈 애플리케이션 : 트랜잭션 처리, 대규모 데이터 처리 -> 스프링에서 제공해주는 모듈을 이용해서 개발자는 비지니스 로직에 집중
  * 배포
    * 프로젝트를 WAR 파일로 빌드
    * Web 서버(Tomcat, Weblogic, Apache) 설치
    * Web 서버에 WAR 파일 배포
* 스프링 부트: 스프링 기반의 애플리케이션을 쉽게 만들 수 있게 해줌. 최소한의 설정으로 스프링 플랫폼과 서드파티 라이브러리들을 사용.
  * 내장 서버: 스프링 부트는 `Embeded Tomcat` 사용(스프링 부트는 Tomcat이 내부에 포함)
    * 내장 서버는 애플리케이션 배포시 복잡함을 피할 수 있게 함
    * 스프링은 톰캣에 대한 설정을 다 해줘야함
  * 자동 설정: starter를 통한 Dependency 자동화 -> `@SpringBootApplication`
    * `@Component`를 통해 필요한 빈 객체들을 자동으로 만들어줌 -> spring.factories에서 확인 가능
  * 쉬운 의존성 관리
    * 호환성에 맞게 버전관리
  * 배포
    * 프로젝트를 JAR 파일로 빌드
    * JAR 파일 실행

## IoC
* Inversion of Control
* 제어의 역전: 객체 간의 결합도를 줄임, 유연한 코드 작성, 유지보수 향상
* 메소드나 객체의 호출을 개발자가 결정하는 것이 아니라, 외부에서 결정
* 객체의 생성부터 소멸까지 개발자가 아닌 컨테이너가 관리하는 것

## DI
* Dependency Injection
* 객체들의 `의존성(결합도)을 줄이기 위해` 사용되는 스프링의 IOC 컨테이너의 구체적인 구현 방식
* 개발 코드에서 객체를 생성하는 것이 아니라, 데이터 주입만 담당하는 별도의 공간에서 객체를 생성하고 데이터간의 의존성을 주입해 개발 코드에서 가져다 씀
* 재사용성 향상, 팩토리 패턴과 유사 
* 방법 3가지: 생성자에 `@Autowired` 추가, 필드 주입, setter 주입(setter에 `@Autowired` 추가)

## AOP
* Aspect Oriented Programming, 관점 지향 프로그래밍
* `공통 관심 사항(Cross-Cutting Concern)`과 핵심 관심 사항(Core Concern)을 분리하는 것
* 특정 로직(로그, 성능테스트 등)을 모든 메소드에 적용하고 싶을 때, 모든 메소드에 일일이 로직을 추가하는 것이 아니라, 로직을 만들어서 모든 메소드에 적용
* 비지니스 로직의 앞/뒤에 공통 관심 사항을 수행해 `중복 코드를 줄이는 것`

## 스프링 MVC 구조
* Model: 핵심적인 비지니스 로직 담당, 데이터베이스 관리
* View: 사용자에게 보여주는 화면 구성
* Controller: 모델과 뷰 사이의 정보 교환

## 스프링 MVC 처리 과정
1. 클라이언트가 서버에 요청을 보내면 Servlet Container가 `DispatcherServlet`에게 요청을 전달<br>
  *  DispatcherServlet: Front Controller
2. `DispatcherServlet`은 요청된 `URL`을 `HandlerMapping`에게 넘겨 호출해야 할 `Controller` 정보를 얻음<br>
  * `@Controller`로 선언되었거나 HttpRequestHandler 인터페이스를 구현한 클래스를 찾음
3. DispatcherServlet이 `HandlerAdapter` 객체에게 요청을 위임하고 `HandlerAdapter`는 `컨트롤러의 메소드를 실행`하여 `ModelAndView` 객체로 반환<br>
  *  ModelAndView: 응답할 View 이름과 view에 전달할 데이터
4. DispatcherServlet은 `ViewResolver`를 이용해 `View` 객체를 얻음<br>
5. DispatcherServlet은 ViewResolver가 리턴한 View객체를 이용해 사용자에게 화면 표시(응답 결과 표시)

## MVC 1과 MVC 2의 차이
### MVC 1
* `JSP` 페이지 안에서 로직 처리를 위해 자바 코드가 함께 사용
* 구조가 단순하다는 장점이 있지만, JSP 내에서 html과 자바 코드가 함께 사용되어 복잡하고 유지보수가 어려움
### MVC 2
* `JSP와 서블릿`이 역할을 분담
* JSP: 요청 결과를 출력하는 VIEW 처리 + 서블릿: 흐름제어, 컨트롤러 역할
* 구조가 복잡하나 유지보수가 용이함

## Servlet
* HTTP 응답에 요청하는 기술, 웹 페이지를 동적으로 생성하기 위한 서버측 프로그램
* 생명 주기: init, service, destroy

## 디스패처 서블릿
* 서버로 들어오는 요청을 처리하는 Front Controller
* 웹 요청의 진입점, 요청을 처리하여 결과를 응답

## 디스패처 서블릿으로 인한 web.xml 역할 축소
* 기존에는 모든 서블릿에 대해 URL 매핑을 활용하기 위해 web.xml에 등록이 필수
* 디스패처 서블릿이 요청을 처리하면서 작업이 편리

## 필터와 인터셉트 차이
* 실행되는 시점의 차이
* 필터: 웹 애플리케이션에 등록
* 인터셉터: 스프링 Context에 등록

## 스프링 어노테이션

## DAO
* Data Access Object
* `DB의 데이터에 접근`하기 위한 객체
* 단일 데이터의 접근 및 갱신을 의미 -> Service: 하나 이상의 DAO를 이용해 비지니스 로직을 처리, 트랜잭션의 단위
* 데이터베이스에 접근하는 로직과 비지니스 로직을 분리하기 위해 사용
* 데이터 조회 및 조작을 담당

## DTO
* Data Transfer Object
* 다른 말로 VO(Value Object)
* 계층(컨트롤러, 뷰, 비즈니스 계층 등)간 `데이터 교환(전송)`을 위한 자바 빈
* 로직을 가지지 않음: 속성과 속성에 접근하기 위한 getter, setter가 있고 추가적으로 toString(), equals() 가능

## ORM
* Object Relational Mapping
* 객체는 객체대로 설계하고, 관계형 데이터베이스는 관계형 데이터베이스대로 설계

## JPA
* Java Persistence API
* 자바 ORM 기술에 다한 API 표준 명세
* 자바 애플리케이션에서 `관계형 DB`를 사용하는 방식을 정의한 `인터페이스`
* `EntityManager를` 통해 `CRUD` 처리

## Hibernate
* JPA의 구현체, 인터페이스를 직접 구현한 라이브러리
* 생산성, 유지보수, 비종속성

## ORM, JPA, Hybernate 장단점

## Mybatis
### 정의
* 자바의 관계형 데이터베이스 프로그래밍을 쉽게 할 수 있도록 도와주는 개발 프레임워크
* JDBC를 통해 DB에 접근하는 작업을 캡슐화, SQL 쿼리 매핑
### 사용 이유
* 프로그램의 SQL 쿼리를 한 파일로 구성하여 코드와 SQL을 분리할 수 있어 사용

## Mybatis, JPA 차이

## Spring JDBC
* 자바에서 데이터베이스에 접속할 수 있도록 해주는 자바 API
* DB에서 자료를 쿼리하거나 업데이트에 사용