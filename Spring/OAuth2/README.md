# Spring Boot OAuth2 Social Login with Google + JWT + React



### Prerequisites

- Spring Framework
- Spring Security
- MySQL
- React




#### Spring package settings

![image](https://user-images.githubusercontent.com/47052106/159847190-25a2a5aa-92f0-4203-bb97-3341b1890e30.png)



#### Package tree

![image](https://user-images.githubusercontent.com/47052106/159848540-bba58263-7950-4f24-bd19-045ba2007cda.png)



### OAuth2 용어 정리

#### Client

- `client`는 `resource owner`의 `protected resource`에 접근을 시도하는 애플리케이션이다
- `protected resource`에 접근하려면 `client`는 `resource Owner`의 허가 즉 `access token`이 필요하다

####  Resource Server

- `resource owner`의 `protected resource`를 가지고 있는`API서버`
- `resource owner`의 `protected resource`를 접근하려면 `access token`이 필요하다

#### Authorization Server

- `client`에게 `access token`을 발급하는 서버
- `resource server`와 통합되어 있을 수 있다

#### Resource Owner

- `protected resource`의 접근 권한을 줄 수 있는 사람
- `end-user`라 불린다

#### Access Token

- `protected resource`를 접근할 때 사용되는 자격 인증서

#### Authorization Endpoint

- `client`가 `user-agent` 리디렉션을 통해 `resource owner`로 부터 권한을 얻는데 사용하는 `endpoint`

#### Token Endpoint

- `client`가 `resource server`에게서 `access token`을 얻기 위해 사용되는 `endpoint`

#### Redirection Endpoint

- `authorization server`가 `resource owner`의 `user-agent`를 리디렉션 하는 `endpoint`



### OAuth2 사용 이유

- 회원가입 시 이메일 인증, 로그인 시 보안, 비밀번호 찾기/변경, 회원정보 수정 등을 구글,페이스북등에 위임하므로 서비스 개발에 집중



### OAuth2 사전 준비

- `Client ID`: public key
- `Client Secret`: secret key. 비공개. 환경변수에 담아둔다
- `Authorized Redirect URIs`: Client ID와 Clinet Secret을 확인한 후 redirect할 url 주소
- 구글 OAuth2 로그인 한다고 가정
  - 구글에 등록된 `Client ID`, `Client Secret`, `Redirect URL`과 우리가 만든 APP에 등록된 `Client ID`, `Client Secret`, `Redirect URL`이 서로 일치해야함. 하나라도 불일치하면 로그인 실패



### OAuth2 동작 원리

- **전제조건**
  - Client가 Auth Server로 부터 `Client ID`, `Client Secret`, `Redirect URL`을 모두 등록/발급 받은 상태
- **Resource Owner의 승인**
  - `Resource Owner`가 `Auth Server`에게 승인 요청을 보냄
  - `Auth Server`가 `Resource Owner`에게 `Authorization Code`를 보냄
  - `Resource Owne`r가 `Client`에
  - 게 `Authorization Code`를 보낸다.
  - `Client`는 **`Client ID, Client Secret, Redirect URL, Authorization Code`** 네 가지를 모두 갖고 있는 상태이다.

- **Auth Server의 승인**
  - 위 네 가지 정보를 Auth Server에 보낸다. (`Redirect URL`은 optional)
    - `redirect_url`을 보내는 건 선택이다
    - 하지만 **`Client ID, Client Secret, Authorization Code 세 가지는 꼭 보내야 한다`**
  - Resource Server는 네 가지 정보가 모두 일치하는지 확인한다.
  - 하나라도 불일치 할 경우 OAuth 로그인은 실패한다.
  - 모두 일치하면 `Access Token`을 발급한다
    - `Authorization Code` 값은 더 이상 필요없기 때문에 삭제한다
- **Access Token 발급**
  - 발급 받은 `Access Token`을 통해서 `Resource Server`의 기능을 이용할 수 있다
- **Refresh Token**
  - `Access Token`은 cookie처럼 만료 기한이 있다
  - 따라서 만료가 되면 재발급 받아야한다
  - 이 때 사용하는 게 `Refresh Token` 이다
  - 서비스마다 `Refresh Token`을 발급하지 않는 경우도 있고 쓰는 방식도 다르다
  - `Access Token`은 주로 **세션에 저장**한다
    - 만료 기한이 짧다
  - `Refresh Token`은 중요하기 때문에 **DB에 저장**한다
    - 만료 기한이 길다
  - `Refresh Token`이 동작하는 대략적인 원리 아래 그림과 같다
  - ![image](https://user-images.githubusercontent.com/47052106/159862173-a54618cb-5833-4808-9ae1-b73b4def8ea0.png)



### Access Token을 받기까지의 과정

여기서 `Resource Owner`는 웹 사용자라면 브라우저, 모바일 사용자라면 iOS/Android 휴대폰이라고 생각하면 편하다



#### 1. App(Client)가 User(Resource Owner)에게 OAuth 로그인 버튼을 보여준다

- 해당 로그인 버튼에는 `clientId`, `scope`(가져올 회원 정보 범위), `redirect_url` 정보가 들어있다
- ![image](https://user-images.githubusercontent.com/47052106/159862470-d00ead4d-8ad0-48a3-8538-b80dca3a49af.png)



#### 로그인 버튼을 누르면 Resource Server는 Resource Owner에게 로그인 화면을 보여준다.

![image](https://user-images.githubusercontent.com/47052106/159862572-d939acfd-dfa6-4521-8c50-21a38506f0de.png)

#### 로그인 과정에서 scope에 정의된 정보 공개 범위에 대한 동의를 구한다.

- 로그인 과정에서, `clientId`와 `redirect_url`이 일치하는지 확인하고 하나라도 일치하지 않으면 더이상 진행하지 않는다.

![image](https://user-images.githubusercontent.com/47052106/159862653-75c826e4-7104-41c3-9a28-3694de617f45.png)

#### 사용자로부터 동의를 얻게되면 Resource Server는 사용자 아이디와 제공할 scope를 알게 된다

![image](https://user-images.githubusercontent.com/47052106/159862949-5a91e91d-e6f6-4744-9d79-c04754142fd5.png)



#### 로그인 인증이 끝나면 Resource Server는 Resource Owner에게 `Authorization Code`를 전달한다.

![image](https://user-images.githubusercontent.com/47052106/159863256-02e68cf2-b4cf-4f77-b9e8-eb8f0bf2602e.png)

#### 이 때 redirect_url로 전환되면서 `authorization_code`가 전달되며 이 과정에서 App(Client)가 `authorization_code`를 알게 된다.

![image](https://user-images.githubusercontent.com/47052106/159863359-4340f5d2-365f-4a69-b704-626d69b32f4b.png)

#### App(Client)는 Resouce Server에게 `Client ID, Client Secret, Redirect URL, Authorization Code` 를 모두 보낸다.

![image](https://user-images.githubusercontent.com/47052106/159863417-1dfbb352-4c81-482e-9a89-ec70dbe98d4c.png)



#### 위 네 가지 정보가 모두 일치하면 Resource Server는 Client에게 `AccessToken`을 발급한다.

- `Authorization Code` 값은 더 이상 필요없기 때문에 삭제한다. (Resource Server, Client 모두)

![image](https://user-images.githubusercontent.com/47052106/159863475-13bbfe1c-477c-4a7b-88d1-9008640256fa.png)

이렇게 발급받은 `Access Token`을 통해서 App(Client)는 Resource Server로부터 사용자 정보를 가져올 수 있다



### 인증 프로세스 요약

![image](https://user-images.githubusercontent.com/47052106/159863538-9460c0f9-cdb2-4d38-93a3-ed4879f1e622.png)



생활코딩 홈페이지에서 깃허브 로그인하는 과정이라고 가정한다

- 사용자가 생활코딩 홈페이지에서 깃허브 로그인 버튼을 누른다

- 브라우저는 생활코딩 서버에 `로그인 URL`을 요청한다

- 생활코딩 서버에서 `로그인 URL`을 브라우저에 전달한다

- 브라우저는 서버에서 받은 `로그인 URL`로 리다이렉트한다

- 브라우저에 깃허브 로그인 화면이 뜬다

- 사용자는 생활코딩이 요청한 정보(scope) 제공 요청을 승인하고, 자신의 깃허브 아이디와 비밀번호를 입력한다

- 깃허브 인증 서버(Auth Server)에서 사용자의 아이디와 비밀번호, 제공할 정보 범위(scope)를 확인한다

- 인증이 완료되면 `Authorization Code`를 `redirect_url`에 붙여 보낸다

  - ```null
    ex) https://redirect_url?code=199b7af5ea11078ee507
    ```

- 생활코딩 서버에서는 `Authorization Code`를 받아 `Client ID, Client Secret, Authorization Code` 를 깃허브 OAuth 서버에 보낸다. (redirect_url은 optional)
- 깃허브 서버는 `Client ID, Client Secret, Authorization Code` 가 모두 일치하는지 확인하고, 모두 일치하면 `AccessToken`을 생활코딩 서버에 보낸다
- 생활코딩 서버는 `AccessToken`을 이용해 깃허브의 Resource Server로부터 사용자 정보를 받아온다



### Spring Boot Application Configuration

- application.properties -> application.yml
  - 계층구조의 명확화

```yml
spring:
    datasource:
        url: jdbc:mysql://localhost:3306/spring_social?useSSL=false&serverTimezone=UTC&useLegacyDatetimeCode=false
        username: USERNAME
        password: PASSWORD

    jpa:
        show-sql: true
        hibernate:
            ddl-auto: update
            naming-strategy: org.hibernate.cfg.ImprovedNamingStrategy
        properties:
            hibernate:
                dialect: org.hibernate.dialect.MySQL5InnoDBDialect
    security:
      oauth2:
        client:
          registration:
            google:
              clientId: CLIENTID
              clientSecret: CLIENTSECRET
              redirectUri: "{baseUrl}/oauth2/callback/{registrationId}"
              scope:
                - email
                - profile
app:
  auth:
    tokenSecret: TOKENSECRET
    tokenExpirationMsec: 864000000
  cors:
    allowedOrigins: http://localhost:3000,http://localhost:8080
  oauth2:
    authorizedRedirectUris:
      - http://localhost:3000/oauth2/redirect
      - myandroidapp://oauth2/redirect
      - myiosapp://oauth2/redirect
```
