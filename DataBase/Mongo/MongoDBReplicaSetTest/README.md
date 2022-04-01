# MongoDB Replica Set


### prerequisites

- docker

- docker compose

- linux

  

### 사용 이유

- 고가용성

- Primary: Write

- Secondary: Read-Only

  

### command

```js
docker network create mongo-cluster
docker run --name mongo1 -d --net mongo-cluster -p 9042:9042 mongo mongod --replSet docker-rs --port 9042
docker run --name mongo2 -d --net mongo-cluster -p 9142:9142 mongo mongod --replSet docker-rs --port 9142
docker run --name mongo3 -d --net mongo-cluster -p 9242:9242 mongo mongod --replSet docker-rs --port 9242
docker exec -it mongo1 mongo --port 9042
config = {"_id" : "docker-rs", "members" : [{"_id" : 0,"host" : "mongo1:9042"},{"_id" : 1,"host" : "mongo2:9142"},{"_id" : 2,"host" : "mongo3:9242"}]}
rs.initiate(config)
rs.status() 
```



### 주의사항

**API Server에서 `/etc/host` 파일을 수정해야한다**

``` tex
sudo vi/etc/hosts
192.168.154.118 mongo1 mongo2 mongo3 #192.168.154.118에 API Server IP를 적는다
```



### 결과 화면

- 시뮬레이션 생성
  - `Write` 작업을 하므로 `Primary`와 연결이 맺어진다![image](https://user-images.githubusercontent.com/47052106/161195996-fd0cd70e-bb23-4cd3-babc-c2b9aa05525c.png)



- 자산 조회
  - `Read` 작업을 하므로 `Secondary`와 연결이 맺어진다

​			![image](https://user-images.githubusercontent.com/47052106/161196807-f46a927f-5210-4009-906d-aa92aba43cf8.png)

  - 추가 조회

    - 다른 `Secondary`와 연결이 맺어졌다

    ![image](https://user-images.githubusercontent.com/47052106/161196926-c0abfe06-7e1c-4247-ae2a-f609460156a3.png)

​      



### 고가용성 테스트

- 동작중인 컨테이너 확인

  - `mongo1:9042`
  - `mongo2:9142`
  - `mongo3:9242`

  ![image](https://user-images.githubusercontent.com/47052106/161197494-b1459402-079c-4310-8283-ddee8e740eac.png)

- 상태 확인

  - ![image](https://user-images.githubusercontent.com/47052106/161197697-28f4e4d8-c934-4325-97a9-e5ae44cd1da7.png)

- `Primary`를 죽여보자

  ![image](https://user-images.githubusercontent.com/47052106/161197876-d6b3fc3f-fc1d-45e3-ac45-4a9df1797114.png)

  - 누가 Primary가 되었는가

    - 기존의 `Primary` 였던 `mongo1:9042`는`health-check`에 실패하였다

    - `mongo2:9142`가 `Primary`가 되었음을 확인할 수 있다

      ![image](https://user-images.githubusercontent.com/47052106/161198009-17fffcdd-5a49-4c39-8837-04740c355998.png)



- 그렇다면 `Write` 작업은 잘 될 것인가?

  - 잘된다!!!

  - `Primary`가 된 `mongo2:9142`와 연결을 맺어 `Write` 작업이 원활히 수행됨을 확인할 수 있었다

    - **고가용성 구조 성공** 

    ![image](https://user-images.githubusercontent.com/47052106/161198279-44332f48-55d4-4a88-9631-63d0927ab33e.png)

- 그렇다면 `Read` 작업은?

  - `Secondary`로 남아있던 `mongo3:9242`와 연결을 맺는다

  - 너무 잘된다!!!

    ![image](https://user-images.githubusercontent.com/47052106/161198510-967f0d13-a683-4271-9b6c-d28879000e54.png)



- 멈춰있던 `mongo1:9042`를 다시 켜보자

  - `monog1:9042`는 `Secondary`로 재시작되었다

    ![image](https://user-images.githubusercontent.com/47052106/161199157-1262713d-f6e9-415f-8098-8328f0d975b5.png)

