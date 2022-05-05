# oAuth 흐름

![image](https://user-images.githubusercontent.com/47052106/166877152-0af7d251-1566-468e-ab9f-89b53ae142dd.png)

1. 카카오 로그인 요청
2. 카카오 아이디/패스워드 입력창
3. 카카오 동의창
4. 카카오 API 서버 (인증서버)에서 인증처리가 완료되면 callback으로 code 값을 클라이언트에게 전달
5. code 값 (ABCD)을 갖고 인증서버에게 자원서버 (내 정보가 들어있는 곳)로 부터 리소스를 갖고 올 수 있는 권한 (access token) 요청
6. access token을 인증서버가 클라이언트에게 전달
7. 이후, 해당 access token을 갖고 리소스 서버로부터 리소스들을 갖고 올 수 있음



```
구글 로그인 완료후에, 코드를 받는게 아니라, 액세스 토큰 + 사용자 프로필 정보를 한번에 받는다.
```



# 스프링 시큐리티

![image](https://user-images.githubusercontent.com/47052106/166898901-85d4004f-7f1a-448e-93fc-72efabbba513.png)

- 서버 세션 안에 시큐리티 세션이 존재
- 시큐리티 세션에는 Authenticaton Object가 들어감
  - userDetails: 일반 로그인하면 해당 객체가 들어감
  - oAuth2User: oAuth 로그인하면 해당 객체가 들어감



```java
// oAuth
@GetMapping("/user")
public @ResponseBdy String user(@AuthenticationPrincipal OAuth2User oauth){
    return "user";
}

// 일반
@GetMapping("/user")
public @ResponseBdy String user(@AuthenticationPrincipal UserDetails userDetails){
    return "user";
}
```

- oAuth로 로그인할시에 컨트롤러 파라미터에 `@AuthenticationPrincipal OAuth2User oauth`

- 일반 로그인하실에 컨트롤러 파라미터에 `@AuthenticationPrincipal UserDetails userDetails`



**도대체 무엇을 사용?** *로그인 하는 방식에 따라 컨트롤러를 분리해야할까?*



### OAuth2User, UserDetails 두개를 상속하는 X객체를 만들어서 Authentication 객체안에 넣자!

```java
public class PrincipalDetails implements UserDetails, OAuth2User {
    //
}

@GetMapping("/user")
public @ResponseBdy String user(@AuthenticationPrincipal PrincipalDetails userDetails){
    return "user";
}
```