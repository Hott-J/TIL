# 1. node 설치
FROM node:12-alpine

#2.패키지 우선 복사
COPY ./package* /usr/src/app/
WORKDIR /usr/src/app
RUN     npm install

#FROM ubuntu:20.04
#RUN apt-get update
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm 

# 2. 소스 복사 . 디렉터리 코드를 아래 경로로 옮긴다.
COPY . /usr/src/app 

# 3. 노드 제이에스 패키지 설치
WORKDIR /usr/src/app

# 4. WEB 서버 실행 (Listen 포트 정의) 
EXPOSE 3000
CMD node app.js