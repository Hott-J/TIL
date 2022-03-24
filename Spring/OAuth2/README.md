## OAuth2



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
- `Authorized Redirect URIs`: 유저가 성공적으로 애플리케이션에 인증을 마친 후, Authorization Severs는 해당 경로로 리디렉션한다
- 구글 OAuth2 로그인 한다고 가정
  - 구글에 등록된 `Client ID`, `Client Secret`, `Redirect URL`과 우리가 만든 APP에 등록된 `Client ID`, `Client Secret`, `Redirect URL`이 서로 일치해야함. 하나라도 불일치하면 로그인 실패



### OAuth2 동작 원리

![image](https://user-images.githubusercontent.com/47052106/159877277-13abbfca-9210-4ae3-b2be-ecafb3e5f6c5.png)

**1**

- User가 클라이언트의 로그인이 필요한 자원에 접근**

**2~3**

- `client_id`,  `redirect_url`, `response_type`, `scope`를 포함하여 사용자의 브라우저를 `Authorization Server`에 리다이렉션 시킵니다
- 이때, `Authorization Server`는 파라미터로 받은 `client_id`와 `redirect_url`이 사전에 등록된 정보와 일치하는지 검증
- 민감한 정보가 포함되니 일치하지 않는다면 (검증 실패) 요청이 거절됨

**4~5**

- 로그인 페이지를 열고 User에게 Client가 등록한 scope에 대한 정보 제공 동의 허용 여부를 나타냄
  - ex) ~에서 사용자의 프로필 이미지, 사용자 이름에 접근하려고 함

**6~12**

- User가 동의하고 로그인에 성공하면 `Authorization Server`는 Client에게 `Authorization Code`를 발급합니다
- 클라이언트는 Authorization code, client_id, secret을 Authorization Server에 다시 전송
- Authorization Server는 전달받은 데이터를 검증하고 `Access Token`을 Client에게 발급함
- 이후, Access Token을 이용해서 Resource Server에 데이터를 요청하고 검증이 완료되면 Resource 서버는 Client에게 scope 범위의 데이터를 응답합니다



#### Refresh Token

![image](https://user-images.githubusercontent.com/47052106/159878060-ee952057-0cb0-41cb-8328-a1996508c4ff.png)

`Access Token`은 수명 시간이 존재합니다. 그렇기 때문에 Access Token이 만료될 경우 데이터에 접근할 수 없는데, 위와 같은 과정을 매번 반복하는 것은 비효율적일 수도 있습니다



**A~E**

- 위의 과정과 동일

**F**

- Access Token이 만료되어 데이터 액세스가 거부됨
- 구현 방식마다 다르지만 그림처럼 B 상황에서 Authorization Server는 Client에게 Access Token을 발급할 때,  Refresh Token을 함께 부여하기도 함

**G**

- Client는 Authorization Server에게 Refresh Token을 사용하여 새로운 Access Token을 요청

**H**

- 클라이언트, Refresh Token의 검증이 성공할 경우 새로운 Access Token을 부여함
- refresh token도 갱신될 수 있다. 서버마다 상이함

