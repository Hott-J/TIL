# MongoDB Replica Set


### prerequisites

- docker



### 사용 이유

- 고가용성

- Primary: Write

- Secondary: Read-Only

  

### command

```js
docker network create mongo-cluster
docker run --name mongo1 -d --net mongo-cluster -p 9042:9042 mongo:3.6 mongod --replSet docker-rs --port 9042
docker run --name mongo2 -d --net mongo-cluster -p 9142:9142 mongo:3.6 mongod --replSet docker-rs --port 9142
docker run --name mongo3 -d --net mongo-cluster -p 9242:9242 mongo:3.6 mongod --replSet docker-rs --port 9242
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
