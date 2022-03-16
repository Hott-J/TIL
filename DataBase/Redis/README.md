## Redis Docker StandAlone Simple Example



### Redis?

- 오픈소스
- In-memory DB
- 데이터베이스
- 캐시
- 메시지 브로커



주요 특징

- Maximum memory
  - 64-bit: no memory limit
  - 32-bit: 3GB
  - 많은 데이터는 hit-ratio를 높힘
- 제거 알고리즘
  - LRU, LFU
- 지속성



예제 테스트

- git clone https://github.com/avinash10584/spring-boot-redis-cluster.git



### Step1

- Todo 리스트 앱 간단하게 스프링 부트로 작성

```java
@RestController("/")
public class TodoListController {

	private ToDoList sample = new ToDoList(1, Arrays.asList(new ToDo(1, "Comment", false), new ToDo(2, "Clap", false),
			new ToDo(3, "Follow Author", false)), false);

	@GetMapping
	public ToDoList getList() {
		return sample;
	}

	@GetMapping("/todo/{id}")
	public Optional<ToDo> getToDo(@PathVariable("id") long id) {
		return sample.getTasks().stream().filter(x -> x.getId() == id).findFirst();
	}

	@PutMapping("/todo")
	public ToDoList addToDo(@RequestBody ToDo toDo) {
		sample.getTasks().add(toDo);
		return sample;
	}

	@PostMapping("/todo/{id}")
	public ToDo updateToDo(@PathVariable("id") long id, @RequestBody ToDo toDo) throws Exception {
		Optional<ToDo> item = sample.getTasks().stream().filter(x -> x.getId() == id).findFirst();
		if (item.isPresent()) {
			item.get().setCompleted(toDo.isCompleted());
			return item.get();
		} else {
			throw new Exception("To Do item not found");
		}
	}
}
```



### Step2

- Redis docker image download
- docker pull redis
- docker run --rm -p 4025:6379 -d --name redis-1 redis redis-server
  - standalone



### Step3

- Redis와 spring boot application 통합

```java
@EnableCaching // 캐시 기능을 사용하고 싶은 프로젝트에 사용
@SpringBootApplication
public class Application {
	
	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
```

- `DOCKER_BUILDKIT=1 docker build -t spring-boot-redis-cluster .`
  - 빠른 실행
  - DOCKER_BUILDKIT command 오류시, `docker build -t spring-boot-redis-cluster .` 로 실행한다.
- mvn이 없을 경우 설치해야함
  - 추가적으로, 윈도우에서는 ./mvnw 문제 이슈 발생
  - https://stackoverflow.com/questions/61226664/build-docker-error-bin-sh-1-mvnw-not-found
  - dos2unix 설치 후, 환경변수 설정한 뒤에, `dos2unix mvnw` 명령어 실행
- `docker run --rm -p 4024:4024 --name spring-boot-redis spring-boot-redis-cluster`
- http://localhost:4024/app 접속
  - connection timed out 발생
  - 만약, 위에 git clone을 한 경우, timed out이 발생하지 않을 수도 있지만, 결국 후에 yml 파일 내 redis: host를 변경해야하므로 주의!
  - 원인
    - 단순히 2개의 도커 이미지가 서로 통신하고 기본적으로는 자체 네트워크에 배치되어 서로 분리되어 있기 때문
  - 해결책
    - 도커 네트워크 생성
      - `docker network create spring-redis-network`
        - redis와 spring boot 이미지 네트워크 생성
        - 예제 테스트에서는 해당 해결책을 이용한다
    - docker-compose default network 생성
      - docker-compose file에 docker network create spring-redis-network 추가

- spring-redis-network 생성 후, `docker network connect spring-redis-network redis-1`로 redis-1 컨테이너를 spring-redis-network에 연결

- `docker inspect spring-redis-network` 로 제대로 네트워크 연결됬는지 확인

  - 위의 명령어로 인해 redis-1 컨테이너가 spring-redis-network에 연결됨을 확인할 수 있다
  - 아래 사진에서 redis-1 컨테이너말고 spring-boot-redis도 연결됬다고 보이는데, 제 오류입니다... ㅎㅎ redis-1만  있어야 합니다.

- ![image](https://user-images.githubusercontent.com/47052106/158580099-b1c0d800-ac51-4e59-8670-a77ab50db9f6.png)

- IPv4 주소를 확인합니다

- ```yml
    redis:
          host: 172.20.0.2 # IP4 주소 세팅
          port: 6379
  ```

  - application.yml 수정

- `docker build -t spring-boot-redis-cluster .` 로 다시 빌드

- `docker run --rm --net spring-redis-network -p 4024:4024 --name spring-boot-redis learnings/spring-boot-redis-cluster`로 네트워크 연결

- http://localhost:4024/app/ 접속

- `docker exec -it redis-1 redis-cli --scan `

  - `docker exec -it redis-1 redis-cli` 로 redis docker container 실행



### Step4: Spring cache annotations 사용

- @CachePut: update cache
- @Cacheable: To return cached response for a method
- @CacheEvict: To remove the cache entry no longer needed, thing delete for an entity
- @Caching:  Java does not allow you to use same annotation type twice on a method or class, so If you want to say @CacheEvict two different caches on same method then the @Cacheable can be used to aggregate other cache annotations.



```java
@RestController("/")
public class TodoListController {

	private ToDoList sample = new ToDoList(1, new ArrayList<ToDo>(Arrays.asList(new ToDo(1, "Comment", false), 
			new ToDo(2, "Clap", false),
			new ToDo(3, "Follow Author", false))), false);

	@Cacheable(value = "todo-list" , key="'getList'")
	@GetMapping
	public ToDoList getList() {
		return sample;
	}

	@Cacheable(value = "todo-single", key = "#id")
	@GetMapping("/todo/{id}")
	public Optional<ToDo> getToDo(@PathVariable("id") long id) {
		return sample.getTasks().stream().filter(x -> x.getId() == id).findFirst();
	}

	@PutMapping("/todo")
	@CachePut(value = "todo-single", key = "#toDo.id")
	@CacheEvict(value="todo-list" , key="'getList'")
	public ToDoList addToDo(@RequestBody ToDo toDo) {
		sample.getTasks().add(toDo);
		return sample;
	}

	@PostMapping("/todo/{id}")
	@CachePut(value = "todo-single", key = "#id")
	@CacheEvict(value="todo-list", key="'getList'")
	public ToDo updateToDo(@PathVariable("id") long id, @RequestBody ToDo toDo) throws Exception {
		Optional<ToDo> item = sample.getTasks().stream().filter(x -> x.getId() == id).findFirst();
		if (item.isPresent()) {
			item.get().setCompleted(toDo.isCompleted());
			return item.get();
		} else {
			throw new Exception("To Do item not found");
		}
	}
	
	@DeleteMapping("/todo/{id}")
	@Caching(evict = {
		@CacheEvict(value = "todo-single", key = "#id"),
		@CacheEvict(value="todo-list", key="'getList'")
	})
	public void deleteToDo(@PathVariable("id") long id) throws Exception {
		Optional<ToDo> item = sample.getTasks().stream().filter(x -> x.getId() == id).findFirst();
		if (item.isPresent()) {
			sample.getTasks().remove(item.get());
		} else {
			throw new Exception("To Do item not found");
		}
	}
}
```

수정후, 다시 `docker build -t spring-boot-redis-cluster .` 로 빌드

`docker run --rm --net spring-redis-network -p 4024:4024 --name spring-boot-redis spring-boot-redis-cluster`

- spring-boot-redis-cluster 이름의 컨테이너를 spring-boot-redis 네트워크에 연결

`docker exec -it redis-1 redis-cli info stats`

- redis-1 stat info 확인



### 캐싱잘 됬는지 확인

- postman으로 요청

![image](https://user-images.githubusercontent.com/47052106/158580135-e92f267d-6dc0-4c4b-8410-4ee96713070f.png)

캐싱한 덕분에 소요시간이 겨우 6ms밖에 안됨을 확인할 수 있다

- 처음 요청: 17ms 소요 (캐시 사용하지 않을 경우)
- 약 3분의1 시간으로 성능 up!!!

