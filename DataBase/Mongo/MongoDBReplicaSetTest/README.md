# MongoDB replica set


### prerequisites

- docker
- docker-compose



### Create the replica Set

`./dbstart.sh`

**rs-init.sh을 찾을 수 없다고 하는 error**

- 직접 primary container에 접속해서 `scripts` 폴더에 접속 후, `./rs-init.sh` 실행하여 primary와 secondary 지정



### Connect to the primary docker instance

`docker exec -it mongo1 mongo`



### Shutdown the replica set

`docker-compose down`

