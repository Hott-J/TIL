# Docker

## 컨테이너란?

- 애플리케이션이 구동하기 위한 설비를 미리 구축한 환경시스템

## 나오게된 배경

- 서비스에 따라 자유롭게 축소 및 확장하기 위해서

## 리눅스에서 돌리는 이유?

- 리눅스 커널 기능을 사용하여 컨테이너 생성
  - chroot: 독립된 공간 형성
  - namespace: isolate 기능 지원
  - cgroup: 필요한만큼 하드웨어 지원

## 사용 이유?

- 개발자가 만든 그대로 어디서든 돌아감!
- 확장/축소가 쉽고 MSA, Devops에 적합!









- 컨테이너 동작방식
  - 도커 호스트(도커가 실행되는 곳. 도커데몬)
  - 도커 허브(컨테이너들을 저장해두고 있는 장소)
  - $ docker search nginx: 도커 허브에 nginx 있는지 찾아달라
  - nginx를 찾아서 호스트에 알려줌
  - $ docker pull nginx:latest: 나의 하드디스크로 이미지를 가져옴. 이미지는 하나지만 레이어는 따로따로 있다. (컨테이너 이미지)
  - $ docker run -d --name web -p 80:80 nginx:latest: 실행함(컨테이너화)



도커호스트: 도커데몬이 실행되고 있는 곳(리눅스 커널)

도커데몬: systemctl start docker 으로 실행한 도커



## 컨테이너  만들기

- 무엇을 컨테이너로 만드는가
  - 개발한 애플리케이션(실행파일)과 운영환경(파이썬, 텐서플로 등)이 모두 들어있는 독립된 공간
  - MSA. 고객의 요구에 바로바로 대응. 짧은 라이프사이클에 대응. 독립된 컨테이너 내부 코드만 변경하면 됨.
- 어떻게 만들어요?
  - Dockerfile
    - 문법
    - 잘만들어진 도커파일을 보며 문법에 익숙해지자!
- 내가 만든 컨테이너 배포?
  - $ docker build -t hello.js:latest
  - $ docker login (인증)
  - $ docker push hello.js:latest
- 도커 호스트에 다양한 리눅스 배포판 컨테이너들이 올라갈 수 있는 이유
  - https://bluese05.tistory.com/10
  - https://bcho.tistory.com/805
  - Container의 OS는 기본적으로 Linux OS만 지원하는데, Container 자체에는 Kernel등의 OS 이미지가 들어가 있지 않다. Kernel은 Host OS를 그대로 사용하되, Host OS와 Container의 OS의 다른 부분만 Container 내에 같이 Packing된다. 예를 들어 Host OS가 Ubuntu version X이고, Container의 OS가 CentOS version Y라고 했을때, Container에는 CentOS version Y의 full image가 들어가 있는 것이 아니라, Ubuntu version X와 CentOS version Y의 차이가 되는 부분만 패키징이 된다. Container 내에서 명령어를 수행하면 실제로는 Host OS에서 그 명령어가 수행된다. 즉 Host OS의 Process 공간을 공유한다.



## 컨테이너 보관창고

도커 레지스트리

- 컨테이너 보관 창고가 있어요?
  - Registry: 컨테이너 이미지를 저장하는 저장소
  - 도커허브
  - Private Registry: 사내의 컨테이너 저장소
- 도커 허브를 사용
  - 이미지 10만여개 존재
  - hub.docker.com
  - 이미지 검색
    - $ docker search "keyword"
  - public
- private Registry 구축
  - registry라는 컨테이너를 실행한다
  - $ docker run -d -p 5000:5000 --restart always --name registry registry:2
  - 앞에 호스트와 포트번호가 필요하다



