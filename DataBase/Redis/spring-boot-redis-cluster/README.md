

# Spring Boot + Redis Clusters + Sharding + Docker + Cache Perfect Guide



들어가기전 미리 학습하면 좋은 내용

- https://meetup.toast.com/posts/226
- 1,2,3,4 전부 보면 좋습니다



## Redis Docker Standalone Cache 



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

- `git clone https://github.com/avinash10584/spring-boot-redis-cluster.git`



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
  - `docker pull redis`

- `docker run --rm -p 4025:6379 -d --name redis-1 redis redis-server`
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

- ![image](https://user-images.githubusercontent.com/47052106/158577771-5cdf1bb4-0c00-4c90-bfca-26377184d005.png)

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

![image](https://user-images.githubusercontent.com/47052106/158577807-fc9e01a6-ab2a-434a-8417-9170f3888d3a.png)

캐싱한 덕분에 소요시간이 겨우 6ms밖에 안됨을 확인할 수 있다

- 처음 요청: 17ms 소요 (캐시 사용하지 않을 경우)
- 약 3분의1 시간으로 성능 up!!!





## Sharing with Redis Clusters

- 샤딩
  - 큰 데이터를 여러 노드에 저장하기 위함
  - 키 공간 전체가 16384 슬롯 (해시 슬롯)으로 분할되어 저장된 키는 이러한 슬롯 중 하나에 매핑
    - HASH_SLOT = CRC16(key) mod 16384



실행중인 컨테이너 stop

`docker stop redis-1`

`docker stop spring-boot-redis`



Redis는 최소 3개의 클러스터로 구성되어야한다

- Redis image는 클러스터 지원을 기본값으로 disabled 이므로, config 파일을 추가해야한다.
  - /redis-conf 에 project 있다

![image](https://user-images.githubusercontent.com/47052106/158721138-3c2fd388-413a-4f99-89a5-1dc911cb2567.png)



샤딩을 해보자

```
docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4025:6379 -d --name redis-1 redis redis-server /redis_config/node1.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4026:6379 -d --name redis-2 redis redis-server /redis_config/node2.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4027:6379 -d --name redis-3 redis redis-server /redis_config/node3.conf
```



docker desktop으로 확인

![image](https://user-images.githubusercontent.com/47052106/158721806-1e0e689b-6125-4bb0-b9f7-58ab896b8539.png)

클러스터 모드로 이미지가 시작했지만, 클러스터들을 연결하진 않았다. 마스터 슬레이브 설정에서 이를 할 수 있지만 먼저 data sharding을 먼저 해보자



클러스터 생성

`docker exec -it redis-1 redis-cli --cluster create 172.20.0.2:6379 172.20.0.3:6379 172.20.0.4:6379`

- 반드시 자기 주소를 적을 것 (위의 yml에 정의한 172.20.0.2는 필자의 주소다)

![image](https://user-images.githubusercontent.com/47052106/158722163-c6a326d7-89e4-4641-bf07-c49924e91d6d.png)

16383개의 키가 해시슬롯 형태로 3개 노드에 각각 할당됨을 확인할 수 있다. 아래와 같은 실행화면이 뜨지 않는다면 IPV4 주소를 잘못 입력한 것!



`docker inspect spring-redis-network`

- redis node ip address checking



application-cluster.yml 수정

```yml
server: 
  port: 4024
  servlet:
    context-path: /app

spring: 
  application:
    name: todolist-redis
  cache:
    type: redis
  redis:
     cluster:
       nodes:
        - 172.20.0.3:6379 # 자기 주소로 해야함
        - 172.20.0.2:6379
        - 172.20.0.4:6379
       maxRedirects: 2
```



수정한 클러스터 설정대로 다시 spring boot app 도커 이미지를 빌드하고 네트워크에 연결하여 실행해보자

```
docker stop spring-boot-redis

DOCKER_BUILDKIT=1 docker build -t spring-boot-redis-cluster .

docker run --rm --net spring-redis-network -e "SPRING_PROFILES_ACTIVE=cluster" -p 4024:4024 --name spring-boot-redis spring-boot-redis-cluster
```



![image](https://user-images.githubusercontent.com/47052106/158722731-9b408855-44a6-425c-b290-97ae5ef3be5a.png)

위와 같이 총 4개의 컨테이너가 실행중 확인

- browser로 제대로 동작하는지 확인 (http://localhost:4024/app)
- `docker exec -it redis-2 redis-cli cluster nodes`
  - 각각의 노드에서 클러스터 설정 확인

![image](https://user-images.githubusercontent.com/47052106/158723371-5ee5c739-030b-42c0-a200-e65ea90e52aa.png)

​		해시 슬롯 16383 제대로 분할되었는지 체크



- 샤딩을 이용하면 대규모 데이터 셋을 위해 데이터를 여러 노드로 분산하여 해시를 통해 검색을 줄일 수 있다
- 현재 클러스터에는 분산 시스템의 2가지 주요 안전 점검인 failover 처리 및 복제 기능은 없다





## Replication with redis cluster

![image](https://user-images.githubusercontent.com/47052106/158725298-52d2c59a-c29e-4327-990b-418cba0a8a39.png)

Redis cluster를 통해 failover 및 복제 처리를 진행할 수 있다

- 1 마스터, 2 슬레이브 구조
- 하나의 노드가 장애가 발생했을 때, 새로운 마스터를 클러스터내에서 추첨을 한다
- 마스터에서만 write 작업, 슬레이브는 read-only

- 위처럼, 마스터가 사라질 경우 전체 상태가 이미 슬레이브 노드들에 복재가 되어 마스터가 선점됬을 때 즉시 쓰기작업이 허용된다



Redis Sentinel?

- Redis 서버에 대한 상태를 감시
- 마스터에 장애가 발생할 경우 슬레이브를 마스터로 자동으로 변경하여 failover에 대처
- 작동방식은 레디스 상태체크 시 다수결에 의해 결정되므로, sentinel은 홀수로 구성해야한다



#### Redis Cluster를 사용하면 Sentinel은 필요없다

- Redis Cluster는 어떤 마스터 인스턴스에 문제가 발생시 자동적으로 failover를 수행한다



먼저, 클러스터들을 마스터/슬레이브로 변경해야한다

3개의 마스터 노드들의 슬레이브 역할을 할 3개의 replication 노드를 더 추가해보자



```
docker stop redis-1
docker stop redis-2
docker stop redis-3


# Start redis nodes

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4025:6379 -d --name redis-1 redis redis-server /redis_config/node1.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4026:6379 -d --name redis-2 redis redis-server /redis_config/node2.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 4027:6379 -d --name redis-3 redis redis-server /redis_config/node3.conf

# Start replicas

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 5025:6379 -d --name redis-1-slave redis redis-server /redis_config/node1-replica.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 5026:6379 -d --name redis-2-slave redis redis-server /redis_config/node2-replica.conf

docker run --rm --net spring-redis-network -v C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster\redis-conf:/redis_config -p 5027:6379 -d --name redis-3-slave redis redis-server /redis_config/node3-replica.conf
```

![image](https://user-images.githubusercontent.com/47052106/158743568-0537630d-c555-41f4-8eb0-3dafaba7e8ed.png)

결과 화면이다. slave란 단어표현이 적절한지 잘 모르겠다,,, Replica와 혼용해서 사용되고 있는 것 같다. 가급적 slave란 단어는 사용하지 않는 것이 좋다

이해를 돕기 위해 slave로 컨테이너 이름을 정했다



```
# 네트워크 확인
docker inspect spring-redis-network

# 클러스터 생성
docker exec -it redis-1 redis-cli --cluster create 172.20.0.2:6379 172.20.0.3:6379 172.20.0.4:6379 172.20.0.6:6379  172.20.0.7:6379 172.20.0.8:6379 --cluster-replicas 1
```

![image](https://user-images.githubusercontent.com/47052106/158743557-6d21b021-b300-4413-9819-c354c7143dd8.png)



```
[ERR] Node 172.20.0.3:6379 is not empty. Either the node already knows other nodes (check with CLUSTER NODES) or contains some key in database 0.
```

해당 오류가 발생하면, 데이터가 있는 실행중인 노드를 멈춰야한다. 클러스터를 생성하려면 반드시 비어있어야한다.



`docker exec -it redis-2 redis-cli cluster nodes`

![image](https://user-images.githubusercontent.com/47052106/158743699-c9dc041f-cddd-4f07-b87e-65b100b9a03f.png)

제대로 클러스터가 마스터/슬레이브 구조로 되어있는지 확인



`docker exec -it redis-1 redis-cli info Replication`

![image](https://user-images.githubusercontent.com/47052106/158744111-d5b7384d-437b-44f7-824b-b86340995a3e.png)

현재 redis-1 이 master임을 확인



`docker stop redis-2`

- redis-2 (master) stop

`docker exec -it redis-1 redis-cli cluster nodes`

- master가 죽으면 어떻게 될까? slave가 과연 master가 됬을지~~~~

![image](https://user-images.githubusercontent.com/47052106/158744575-c578bef0-4d2d-4cbd-9d3a-515a6d61c0fa.png)

놀랍게도, 클러스터로 구축하니 자동으로 failover 처리가 됬음을 확인할 수 있다!!!!



### Redis master/slave network with sentinel (no sharding)

- 샤딩이 필요없음
- 하나의 노드로도 메모리가 충분할 경우
- 클러스터를 생성하지않고 슬레이브 생성
- 결국 샤딩까지 해주는 클러스터 구조가 끝판왕!

![image](https://user-images.githubusercontent.com/47052106/158745172-e1d6f243-c265-4ba4-9a55-7dcaad155434.png)

Redis sentinel을 통해 failover 처리를 할 수 있다



![image](https://user-images.githubusercontent.com/47052106/158745298-96d9b078-c787-4424-b0d8-bf36578564bf.png)

센티널의 경우 클러스터와 컨셉이 다르다. 마스터가 죽으면 센티널들끼리 이야기를 통해 새로운 마스터를 결정한다



`/redis-conf-sentinel` 을 참고

- sentinel monitor redis-cluster 172.20.0.2 6379 2
  - 센티널은 오직 마스터 노드만 바라보면 된다
- sentinel down-after-milliseconds redis-cluster 5000
- sentinel failover-timeout redis-cluster 10000



`docker stop $(docker ps -a -q)`

```
docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 4025:6379 -d --name redis-1 redis redis-server /redis_config/node1.conf

docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 5025:6379 -d --name redis-1-slave redis redis-server /redis_config/node1-slave-1.conf

docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 5026:6379 -d --name redis-2-slave redis redis-server /redis_config/node1-slave-2.conf


docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 6025:6379 -d --name sentinel-1 redis redis-server /redis_config/sentinel1.conf --sentinel

docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 6026:6379 -d --name sentinel-2 redis redis-server /redis_config/sentinel2.conf --sentinel

docker run --rm --net spring-redis-network -v  C:\Users\hakjae_chung\Desktop\개인공부\TIL\DataBase\Redis\spring-boot-redis-cluster/redis-conf-sentinel:/redis_config -p 6027:6379 -d --name sentinel-3 redis redis-server /redis_config/sentinel3.conf --sentinel

docker logs sentinel-2
```

실행중인 컨테이너 전부 종료후 다시 실행



application-sentinel.yml

```yml
server: 
  port: 4024
  servlet:
    context-path: /app

spring: 
  application:
    name: todolist-redis
  cache:
    type: redis
  redis:
    sentinel:
      master: redis-cluster
      nodes:
        - 172.20.0.5:6379
        - 172.20.0.6:6379
        - 172.20.0.7:6379
```



```
docker stop spring-boot-redis

DOCKER_BUILDKIT=1 docker build -t /spring-boot-redis-cluster .

docker run --rm --net spring-redis-network -e "SPRING_PROFILES_ACTIVE=sentinel" -p 4024:4024 --name spring-boot-redis spring-boot-redis-cluster
```



`docker stop redis-1`

- master stop

`docker logs sentinel-1`

- sentinel log 확인

```
1:X 18 Jun 2020 21:25:06.046 # +sdown master redis-cluster 172.18.0.2 6379
1:X 18 Jun 2020 21:25:07.679 # +new-epoch 1
1:X 18 Jun 2020 21:25:07.891 # +vote-for-leader bfebc5c7d07121c78633024dcbc89a14bf1e4563 1
1:X 18 Jun 2020 21:25:07.948 # +odown master redis-cluster 172.18.0.2 6379 #quorum 3/2
1:X 18 Jun 2020 21:25:07.948 # Next failover delay: I will not start a failover before Thu Jun 18 21:25:28 2020
1:X 18 Jun 2020 21:25:08.580 # +config-update-from sentinel bfebc5c7d07121c78633024dcbc89a14bf1e4563 172.18.0.7 6379 @ redis-cluster 172.18.0.2 6379
1:X 18 Jun 2020 21:25:08.580 # +switch-master redis-cluster 172.18.0.2 6379 172.18.0.4 6379
1:X 18 Jun 2020 21:25:08.581 * +slave slave 172.18.0.3:6379 172.18.0.3 6379 @ redis-cluster 172.18.0.4 6379
1:X 18 Jun 2020 21:25:08.581 * +slave slave 172.18.0.2:6379 172.18.0.2 6379 @ redis-cluster 172.18.0.4 6379
```

sentinel들끼리 추첨을 통해 복제된 slave 노드들 중 하나를 master로 승격시킴을 확인
