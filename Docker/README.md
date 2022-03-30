## 컨테이너란?

- 애플리케이션이 구동하기 위한 설비를 미리 구축한 환경시스템
  - Ex) Spring + MongoDB + Java etc


## 나오게된 배경

- 서비스에 따라 자유롭게 축소 및 확장하기 위해서
- 가상화 플랫폼? 
  - 자유롭게 축소 확장하기에는 가상머신이 어울리지 않다
  - 컨테이너는 용량이 작음 (최소한의 환경만 들어가있음) 그러므로 확장이 좋고 배포에 용이


## 굳이 리눅스에서 돌리는 이유?

- 리눅스 커널 기능을 사용하여 컨테이너가 생성된다
  - chroot: 독립된 공간 형성
  - namespace: 6가지 isolate 기능 지원
  - cgroup: 필요한만큼 하드웨어 지원
- 윈도우나 맥은 커널이 없으므로, 하이퍼바이저(VirtualBox)를 활성화시켜서 그 위에 컨테이너를 돌린다
  - 실제 현장에서는 라이센스 비용이 들어가지 않는 리눅스 기반으로 컨테이너를 동작한다
  - 따로 하이퍼바이저를 운영할 필요 없으므로


## 일반 프로그램과 컨테이너의 차이

NodeJS로 짠 앱이라고 가정

일반프로그램

- NodeJS 설치(OS에 따라 다름) + apt-get install + node기반으로 실행 

컨테이너

```dockerfile
FROM node:12
COPY app.js / # 컨테이너의 최상위 디렉터리로 app.js 복사
ENTRYPOINT ["node", "/app.js"] # node명령어로 /app.js 실행
```

- 환경이 필요하고 실행하는 건 똑같지만 모양이 다르다

## 사용 이유?

- 개발자가 만든 그대로 어디서든 돌아감!
  - 개발자의 개발환경과 회사의 운영환경이 다르므로 개발자가 만든 프로그램을 사내에 도입하기 어려웠다

- 확장/축소가 쉽고 MSA, Devops에 적합!
  - 일반 프로그램
    - 100MB 프로그램에 OS는 1GB라고 가정
    - 프로그램 확장할때 OS도 확장되어야함 (가상환경)

  - 컨테이너 구조
    - 도커 엔진 위에 여러개의 컨테이너를 올림 (프로그램 하나 당 100MB만큼만 확장됨)


## 동작방식

- 도커 호스트 (도커가 실행되는 곳. 도커데몬이 있음)
- 도커 허브 (컨테이너 이미지들을 저장해두고 있는 장소)
- `$ docker search nginx` 
  - 도커 허브에 nginx 있는지 찾아달라
  - 도커데몬은 nginx를 찾아서 호스트에 리스트를 알려줌
- `$ docker pull nginx:latest`
  -  나의 하드디스크로 이미지를 가져옴. 이미지는 하나지만 레이어는 따로따로 있다. (컨테이너 이미지, 이미지는 하드디스크에 파일형태로 저장됨)
- `$ docker run -d --name web -p 80:80 nginx:latest`
  - run 대신 create, start도 가능
  - 실행함(컨테이너화, 메모리에 올라감)

용어 정리

- 도커호스트: 도커데몬이 실행되고 있는 곳(리눅스 커널)
- 도커데몬: `systemctl start docker` 으로 실행한 도커



## 맥에서 도커 이미지 레이어 확인

- https://iamjjanga.tistory.com/50



## 컨테이너  만들기

- 무엇을 컨테이너로 만드는가
  - 개발한 애플리케이션(실행파일)과 운영환경(파이썬, 텐서플로 등)이 모두 들어있는 독립된 공간
  - MSA. 고객의 요구에 바로바로 대응. 짧은 라이프사이클에 대응. 독립된 컨테이너 내부 코드만 변경하면 됨
  
- 어떻게 만들어요?
  - Dockerfile
  
    - 쉽고, 간단, 명확한 구문을 가진 텍스트 파일로 Top-Down 해석
  
    - 대소문자를 구분하지 않으나 가독성을 위해 사용
  
    - 잘만들어진 도커파일을 보며 문법에 익숙해지자!
  
    - ```te
      #: commment
      FROM: 컨테이너의 Base image (운영환경)
      MAINTAINER: 이미지를 생성한 사람의 이름 및 정보
      LABEL: 컨테이너 이미지에 컨테이너의 정보를 저장
      RUN: 컨테이너 빌드를 위해 base image에서 실행할 명령어
      COPY: 컨테이너 빌드시 호스트의 파일을 컨테이너로 복사
      ADD: 컨테이너 빌드시 호스트의 파일 (tar, url 포함)을 컨테이너로 복사
      WORKDIR: 컨테이너 빌드시 명령이 실행될 작업 디렉터리 설정
      ENV: 환경변수 지정
      USER: 명령 및 컨테이너 실행시 적용할 유저 설정
      VOLUME: 파일 또는 디렉토리를 컨테이너의 디렉토리로 마운트
      EXPOSE: 컨테이너 동작 시 외부에서 사용할 포트 지정
      CMD: 컨테이너 동작 시 자동으로 실행할 서비스나 스크립트 지정
      ENTRYPOINT: CMD와 함께 사용하면서 명령어 지정 시 사용, cmd는 argument entrypoint는 명령어
      ```
  
    - 예제
  
    - ```dockerfile
      FROM node:12
      COPY hello.js /
      CMD ["node", "/hello.js"]
      ```
  
      - `docker build -t hellojs .`
        - 뒤에 . 을 붙임으로써 현재 디렉토리에 있는 파일을 기준으로 로컬파일을 갖고 컨테이너를 만든다
  
- 내가 만든 컨테이너 배포?

  - `$ docker build -t hello.js:latest .`
  - `$ docker login` 
    - 인증 (도커 허브)
  - `$ docker push hello.js:latest`
    - 허브에 저장
  - 허브에 업로드하려면 container 이름을 `chung1306/containerName` 와 같이 설정해야한다
    - ` docker tag webserver chung1306/webserver`
      - 도커 이미지 이름 변경하는 방법 (webserver -> chung1306/webserver)

- 도커 호스트에 다양한 리눅스 배포판 컨테이너들이 올라갈 수 있는 이유
  - https://bluese05.tistory.com/10
  - https://bcho.tistory.com/805
  - Container의 OS는 기본적으로 Linux OS만 지원하는데, Container 자체에는 Kernel등의 OS 이미지가 들어가 있지 않다. Kernel은 Host OS를 그대로 사용하되, Host OS와 Container의 OS의 다른 부분만 Container 내에 같이 Packing된다. 예를 들어 Host OS가 Ubuntu version X이고, Container의 OS가 CentOS version Y라고 했을때, Container에는 CentOS version Y의 full image가 들어가 있는 것이 아니라, Ubuntu version X와 CentOS version Y의 차이가 되는 부분만 패키징이 된다. Container 내에서 명령어를 수행하면 실제로는 Host OS에서 그 명령어가 수행된다. 즉 Host OS의 Process 공간을 공유한다.



## 컨테이너 보관창고

**도커 레지스트리**

- 컨테이너 보관 창고가 있어요?
  - `Registry`: 여러 형태의 컨테이너 이미지를 저장하는 저장소
  - `Docker Hub`: hub.docker.com
  - `Private Registry`: 사내의 컨테이너 저장소
- 도커 허브를 사용
  - 이미지 10만여개 존재
  - hub.docker.com
  - 이미지 검색
    - `$ docker search "keyword"`
  - public
- private Registry 구축 (사내에서만 운영)
  - registry라는 컨테이너를 실행한다
  - `$ docker run -d -p 5000:5000 --restart always --name registry registry:2`
  - 앞에 호스트와 포트번호가 필요하다
  -  `$ docker tag mongo localhost:5000/mongo`
    - localhost가 아니라 IP Address가 들어갈 수 있다 (외부에 업로드)
  - `$ docker push localhost:5000/mongo`
    - 나의 저장소에 업로드
    - `/var/lib/docker/volumes/[container id]/_data/docker/registry/v2/repositories`에 저장되어있다



## 컨테이너 사용

**컨테이너 실행 라이프 사이클**

- 이미지 검색

  - `docker search [옵션] <이미지이름:태그명>`

- 이미지 다운로드

  - `docker pull [옵션] <이미지이름:태그명>`

- 다운받은 이미지 목록 출력

  - `docker images`

- 다운 받은 이미지 상세보기

  - `docker inspect [옵션] <이미지이름:태그명>`

- 이미지 삭제

  - `docker rmi [옵션] <이미지이름>`

- 이미지를 컨테이너화 (running X)

  - `docker create [옵션] <이미지이름:태그명> `

- 컨테이너 실행

  - `docker start [옵션] <컨테이너이름>`

- 컨테이너 상태 보기

  - `docker ps [옵션]`

- 실행중인 컨테이너 상세 보기

  - `docker inspect <컨테이너이름>`

- 컨테이너 멈춤

  - `docker stop [옵션] <컨테이너이름>`

- 컨테이너 삭제

  - `docker rm [옵션] <컨테이너이름>`

- **이미지 생성 + 컨테이너 생성/실행**

  - `docker run [옵션] <이미지이름:태그명>`
  - `pull -> create -> start`를 한번에 모아놓은 명령어

- webserver 컨테이너에서 동작되는 프로세스 확인

  - `docker top [옵션] webserver`

- webserver 컨테이너 로그 정보

  - `docker logs [옵션] webserver`
  - `docker logs -f`

- webserver 컨테이너를 /bin/bash로 실행

  - `docker exec webserver /bin/bash`

- 포그라운드로 실행중인 컨테이너에 연결

  - `docker attach [옵션] 컨테이너이름`

  

## 컨테이너 관리

**컨테이너 리소스 제한**

- 기본으로 컨테이너는 호스트 하드웨어 리소스의 사용 제한을 받지 않는다
  - 컨테이너가 필요로 하는 만큼의 리소스만 할당해야한다
- Docker command를 통해 제한할 수 있는 리소스
  - CPU
  - Memory
  - Disk I/O
  - `docker run --help`

**Memory 리소스 제한**

- 제한 단위는 b, k, m, g로 할당
- -- memory, -m: 컨테이너가 사용할 최대 메모리 양을 지정
  - `docker run -d -m 512m nignx:1.14`
    - 512m 넘어가면 kill됨
- --memory-swap: 컨테이너가 사용할 스왑 메모리 영역에 대한 설정, 스왑사이즈 = 메모리+스왑. 스왑 사이즈 생략 시 최대 메모리의 2배가 설정됨
  - `docker run -d -m 200m --memory-swap 300m nginx:1.14`
    - 200m까지 쓸 수 있고, 스왑사이즈도 300m 쓸 수 있음. 총 500m을 쓸 수 있는게 아니라 300m을 쓸 수 있음. 스왑메모리는 100m이란 뜻
- --memory-reservation: --memory 값보다 적은 값으로 구성하는 소프트 제한 값 설정
  - `docker run -d -m 1g --memory-reservation 500m nginx:1.14`
    - 적어도 500m은 쓸 수 있게끔 보장되고 1g까지 쓸 수 있다
- --oom-kill-disable: OOM Killer가 프로세스 kill 하지 못하도록 보호
  - `docker run -d -m 200m --oom-kill-disable nginx:1.14`



**CPU 리소스 제한**

- --cpus: 컨테이너에 할당할 CPU core수를 지정. --cpus="1.5" 컨테이너가 최대 1.5개의 CPU 파워 사용가능
  - `docker run -d --cpus=".5" ubuntu`
- --cpuset-cpus: 컨테이너가 사용할 수 있는 CPU나 코어를 할당. cpu index는 0부터. --cpuset-cpus=0-4
  - `docker run -d --cpuset-cpus 0-3 ubuntu`
- --cpu-share: 컨테이너가 사용하는 CPU 비중을 1024 값을 기반으로 설정. --cpu-share 2048 기본 값보다 두 배 많은 CPU 자원을 할당
  - `docker run -d --cpu-shares 2048 ubuntu`



**Block I/O 제한**

- --blkio-weight, --blkio-weight-device: Block IO의 Quota를 설정할 수 있으며 100~1000까지 선택. 디폴트 500
  - `docker run -it --rm --blkio-weight 100 ubuntu /bin/bash`
- --device-read-bps, --device-write-bps: 특정 디바이스에 대한 읽기와 쓰기 작업의 초당 제한을 kb, mb, gb 단위로 설정
  - `docker run -it --rm --device-write-bps /dev/vda:1mb ubuntu /bin/bash`
  - `docker run -it --rm --device-write-bps /dev/vad:10mb ubuntu /bin/bash`
- --device-read-iops, --device-write-iops: 컨테이너의 read/write 속도의 쿼터를 설정한다. 초당 quota를 제한해서 I/O를 발생시킴. 0이상의 정수로 표기. 초당 데이터 전송량=IOPS * 블럭크기(단위 데이터 용량)
  - `docker run -it --rm --device-write-iops /dev/vad:10 ubuntu /bin/bash`
  - `docker run -it --rm --device-write-iops /dev/vad:100 ubuntu /bin/bash`



**컨테이너 사용 리소스를 확인하는 모니터링 툴**

- docker monitoring commands
  - docker stat: 실행중인 컨테이너의 런타임 통계를 확인
    - `docker stats [options] [container...]`
    
  - docker event: 도커 호스트의 실시간 event 정보를 수집해서 출력
    - `docker events -f container=<NAME>`
    - `docker image -f container=<NAME>`
    
  - cAdvisor
    - https://github.com/google/cadvisor
    
      

## 컨테이너 볼륨

- 컨테이너 이미지는 read-only
- 컨테이너에 추가되는 데이터들은 별도의 read-write 레이어에 저장
  - Union File System (Overlay)
  - read-only, read-write가 하나의 레이어처럼 보이고 동작
  - 실수로 컨테이너 삭제되면???
    - Read-write 레이어 사라짐: 데이터 전부 날라감
    - 중요 데이터는 영구적으로 보존해야한다!!!
- 디스크에 영구적으로저장
  - `docker run -d --name db -v /dbdata:/var/lib/mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=pass mysql`
    - -v로 볼륨 마운트: 디스크에 저장
    - 컨테이너 삭제해도 호스트 디비에는 여전히 데이터가 남아있으므로, 동일하게 docker run하면 그대로 사용할 수 있다
  - `docker run -d -v /webdata:/var/www/html:ro httpd`
    - 보통 ro (read-only)옵션을 줘서 볼륨 마운트된 데이터를 write하지 못하게 보호
  - `docker run -d -v /var/lib/mysql -e M~~`
    - 임의의 디렉터리를 만들어서 알아서 마운트
- 컨테이너끼리 데이터 공유하기
  - `docker run -v /webdata:/webdata -d --name df smlinux/df`
  - `docker run -d -v /webdata:/usr/share/nginx/html:ro -d ubuntu`
    - web content generator의 webdata가 index.html을 만들면 /webdata/index.html 형태로 저장되고 이게 ubuntu로 띄운 webserver에서 서빙해준다