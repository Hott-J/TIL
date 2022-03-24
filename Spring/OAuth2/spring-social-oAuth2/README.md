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


### AppProperties Binding

```java
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private final Auth auth = new Auth();
    private final OAuth2 oauth2 = new OAuth2();

    public static class Auth {
        private String tokenSecret;
        private long tokenExpirationMsec;

        public String getTokenSecret() {
            return tokenSecret;
        }

        public void setTokenSecret(String tokenSecret) {
            this.tokenSecret = tokenSecret;
        }

        public long getTokenExpirationMsec() {
            return tokenExpirationMsec;
        }

        public void setTokenExpirationMsec(long tokenExpirationMsec) {
            this.tokenExpirationMsec = tokenExpirationMsec;
        }
    }

    public static final class OAuth2 {
        private List<String> authorizedRedirectUris = new ArrayList<>();

        public List<String> getAuthorizedRedirectUris() {
            return authorizedRedirectUris;
        }

        public OAuth2 authorizedRedirectUris(List<String> authorizedRedirectUris) {
            this.authorizedRedirectUris = authorizedRedirectUris;
            return this;
        }
    }

    public Auth getAuth() {
        return auth;
    }

    public OAuth2 getOauth2() {
        return oauth2;
    }
}
```



### Enable AppProperties

```java
@SpringBootApplication
@EnableConfigurationProperties(AppProperties.class)
public class SpringSocialApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringSocialApplication.class, args);
	}
}
```



### Enable CORS

```java
@Configuration
public class WebMvcConfig implements WebMvcConfigurer {

    private final long MAX_AGE_SECS = 3600;

    @Value("${app.cors.allowedOrigins}")
    private String[] allowedOrigins;

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
        .allowedOrigins(allowedOrigins)
        .allowedMethods("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
        .allowedHeaders("*")
        .allowCredentials(true)
        .maxAge(MAX_AGE_SECS);
    }
}
```



### DB Entity

```java
@Entity
@Table(name = "users", uniqueConstraints = {
        @UniqueConstraint(columnNames = "email")
})

@Getter
@Setter
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Email
    @Column(nullable = false)
    private String email;

    private String imageUrl;

    @Column(nullable = false)
    private Boolean emailVerified = false;

    @JsonIgnore
    private String password;

    @NotNull
    @Enumerated(EnumType.STRING)
    private AuthProvider provider;

    private String providerId;
}
```

```java
public enum  AuthProvider {
    local,
    google
}
```



### UserRepository

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    Boolean existsByEmail(String email);
}
```



### Configure Security

```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(
        securedEnabled = true,
        jsr250Enabled = true,
        prePostEnabled = true
)
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private CustomUserDetailsService customUserDetailsService;

    @Autowired
    private CustomOAuth2UserService customOAuth2UserService;

    @Autowired
    private OAuth2AuthenticationSuccessHandler oAuth2AuthenticationSuccessHandler;

    @Autowired
    private OAuth2AuthenticationFailureHandler oAuth2AuthenticationFailureHandler;
    
    @Autowired
    private HttpCookieOAuth2AuthorizationRequestRepository httpCookieOAuth2AuthorizationRequestRepository;

    @Bean
    public TokenAuthenticationFilter tokenAuthenticationFilter() {
        return new TokenAuthenticationFilter();
    }

    /*
      By default, Spring OAuth2 uses HttpSessionOAuth2AuthorizationRequestRepository to save
      the authorization request. But, since our service is stateless, we can't save it in
      the session. We'll save the request in a Base64 encoded cookie instead.
    */
    @Bean
    public HttpCookieOAuth2AuthorizationRequestRepository cookieAuthorizationRequestRepository() {
        return new HttpCookieOAuth2AuthorizationRequestRepository();
    }
    
    @Override
    public void configure(AuthenticationManagerBuilder authenticationManagerBuilder) throws Exception {
        authenticationManagerBuilder
                .userDetailsService(customUserDetailsService)
                .passwordEncoder(passwordEncoder());
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }


    @Bean(BeanIds.AUTHENTICATION_MANAGER)
    @Override
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .cors()
                    .and()
                .sessionManagement()
                    .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                    .and()
                .csrf()
                    .disable()
                .formLogin()
                    .disable()
                .httpBasic()
                    .disable()
                .exceptionHandling()
                    .authenticationEntryPoint(new RestAuthenticationEntryPoint())
                    .and()
                .authorizeRequests()
                    .antMatchers("/",
                        "/error",
                        "/favicon.ico",
                        "/**/*.png",
                        "/**/*.gif",
                        "/**/*.svg",
                        "/**/*.jpg",
                        "/**/*.html",
                        "/**/*.css",
                        "/**/*.js")
                        .permitAll()
                    .antMatchers("/auth/**", "/oauth2/**")
                        .permitAll()
                    .anyRequest()
                        .authenticated()
                    .and()
                .oauth2Login()
                    .authorizationEndpoint()
                        .baseUri("/oauth2/authorize")
                        .authorizationRequestRepository(cookieAuthorizationRequestRepository())
                        .and()
                    .redirectionEndpoint()
                        .baseUri("/oauth2/callback/*")
                        .and()
                    .userInfoEndpoint()
                        .userService(customOAuth2UserService)
                        .and()
                    .successHandler(oAuth2AuthenticationSuccessHandler)
                    .failureHandler(oAuth2AuthenticationFailureHandler);

        http.addFilterBefore(tokenAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- @EnableGloabalMethodSecurity
  - 특정 메서드에 권한 처리를 하는 MethodSecurity 설정 기능 제공. 각 설정값 true로 변경하면 사용 가능 (default: false)
  - securedEnable: @Secured 사용하여 인가처리하는 옵션
  - prePostEnable: @PreAuthorize, @PostAuthorize 사용하여 인가처리 옵션
  - jsr250Enabled: @RolesAllowed 사용하여 인가처리 옵션
- httpBasic().disable()
  - 요청 헤더에 username과 password를 실어 보내면 브라우저 또는 서버가 그 값을 읽어서 인증하는 방식인 Basic 인증을 비활성화한다
- csrf().disable()
  - Jwt token을 사용할 것이므로 비활성화한다
  - 일반 사용자들이 브라우저를 통해 요청을 하는 경우에는 CSRF 방지를 사용하는 것이 좋다
- sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
  - 애플리케이션 내에서 세션을 사용하지 않으므로 세션을 사용하지 않는 전략을 선택
- .exceptionHandling().authenticationEntryPoint(new RestAuthenticationEntryPoint())
  -  인증을 하지 않은 사용자가 인증이 필요한 리소스에 접근했을 때 유저가 인증할 수 있는 authenticationEntryPoint 설정하는 것
- .oauth2.Login().authorizationEndpoint().authorizationRequestRepository(cookieAuthorizationRequestRepository())
  - OAuth2 진행시 state 값을 잠시 저장해야 한다
  - AuthorizationRequest를 쿠키를 통해 저장하겠다는 의미
- userInfoEndpoint().userService(customOAuth2UserService)
  - 유저의 정보를 얻을 수 있는 UserInfo Endpoint로 부터 유저의 정보를 얻어오기 위해 사용될 서비스로 `customOAuth2UserService`를 등록한다



### OAuth2 Login 흐름

- Front end client가 유저를 특정 스프링 서버의 엔드포인트로 보내면서 시작됨
  - 엔드포인트 예시
    - `http://localhost:8080/oauth2/authorize/{provider}?redirect_uri=<redirect_uri_after_login>`
    - `provider` 는 `google`, `facebook` 등이 될 수 있다
    - 여기서의 redirect_uri는 인증이 끝나고 리다이렉트 될 주소이며 앞서 언급한 OAuth2의 `Authorized redirect URIs` 와는 다른 것이다

- 요청을 받은 Spring Security’s OAuth2 client는 유저를`Authorization Server`의 `Authorization Endpoint` 로 리다이렉트 시킨다
  - `authorizationRequestRepository` 를 이용해 `state` 를 저장한다
  - `provider` 의 페이지에서 유저는 앱의 접근 권한을 허가하거나 거부한다
- 유저가 허가하면 `Authorization Server` 는 유저를 앱을 등록할 때 설정한 `Authorized redirect URIs` 로 리다이렉트 시킨다
  - `authorization code` 를 포함하고 있다
- 유저가 거절하면 `error` 를 가지고 `Authorized redirect URIs` 로 리다이렉트 된다
  - OAuth2 callback이 실패하면 스프링 스큐리티는 `oAuth2AuthenticationFailureHandler` 을 호출한다
- OAuth2 callback이 성공하면 스프링 스큐리티는 `authorization code` 를 `Access Token` 으로 교환하고 `customOAuth2UserService` 를 호출한다
- `customOAuth2UserService` 은 `Access Token` 을 이용해 유저의 정보를 가져오고 회원가입을 하거나 로그인을 한다
- 마지막으로 `oAuth2AuthenticationSuccessHandler` 가 호출되고 jwt 인증 토큰을 만들고 유저를 ( `redirect_uri_after_login` + jwt 인증 토큰)로 리다이렉트 시킨다

