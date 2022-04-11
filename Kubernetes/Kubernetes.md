# 쿠버네티스 환경 구성



## 1.1 쿠버네티스란?

**컨테이너 관리 (오케스트레이션)**

![image](https://user-images.githubusercontent.com/47052106/162612972-21cbec1b-4dde-41b8-8229-487e95ec55da.png)



**도커?**

![image](https://user-images.githubusercontent.com/47052106/162612989-97787d4b-c1bc-4a63-9103-49801ddc7ed8.png)



**쿠버네티스 배포 종류**

![image](https://user-images.githubusercontent.com/47052106/162613008-e65bf463-e8cb-4c9b-a850-04ea74843c74.png)

![image](https://user-images.githubusercontent.com/47052106/162613030-99bfdb09-1b80-4b07-be11-d07cadb7541d.png)



## 1-2 코드로 쿠버네티스 랩 환경 구성하기

**Prerequsites**

- Vagrant
  - 코드를 풀어 VM에 설치
  - Virtual Box와 궁합이 맞음
- Virtual Box
- Code



**vagrant up 하는 과정에서 오류가 발생하였다**

`error execution phase preflight: couldn't validate the identity of the API Server`



- 해결 방안

```shell
# 한줄씩 실행
vagrant up m-k8s-1.20
vagrant up w1-k82-1.20
vagrant up w2-k82-1.20
vagrant up w3-k82-1.20

# 하나씩 삭제하는법
vagrant destory -f w1-k8s-1.20
```



* 참고

https://www.inflearn.com/questions/330276



## 1-3 쿠버네티스 랩을 쉽게 접근하기 위한 터미널 구성

**Prerequsites**

- putty
- super putty
  - 다수의 세션을 쉽게 관리해줌



## 2-1 배포를 통해 확인하는 파드

**애플리케이션 배포 구성도**

![image](https://user-images.githubusercontent.com/47052106/162728438-f70fb1cc-5628-4393-a72a-147d7df653b4.png)



**파드?**

- 컨테이너들의 집합
- 컨테이너들 + 볼륨
- 대부분 하나의 컨테이너가 하나의 파드로 이루어진 경우가 많다
- 한가지 일을 하는 단위

![image](https://user-images.githubusercontent.com/47052106/162728299-0a0c5a71-17e0-41b6-beeb-51874d6df46a.png)



**실습**

![image](https://user-images.githubusercontent.com/47052106/162728218-7f7e380d-13b1-40d9-b2f8-cf0d61997502.png)

`kubectl run nginx --image=nginx`

- 전체 쿠버네티스 클러스터 딱 1개의 pod만 생성



**마스터노드**

- 관리를 해주는 노드

**워커노드**

- pod등이 생성되어 동작하는 노드들

​	

## 2-2 배포한 파드를 외부에서도 접속하게 하는 서비스



**외부에서 172.16.103.129 접근이 안된다**



**가능하게 하려면?**

- 외부와 통신할 수 있는 문 (서비스)이 필요하다
- 이는 각각의 노드포트와 연결되어있다

![image](https://user-images.githubusercontent.com/47052106/162730531-faaa8b38-b0c8-46ea-a570-f31c2d43cd66.png)



**실습**

![image](https://user-images.githubusercontent.com/47052106/162730651-27c74bee-63c5-4f43-ac58-703e6864f176.png)



`kubectl expose pod nginx --type=NodePort --port=80`

- pod 노출시키는 명령어
- type을 정하지 않으면 기본값으로 clusterIP라는 타입으로 지정됨
  - 쿠버네티스 클러스터 내부에서 사용할 수 있는 타입
- 위 실습을 보면 31179가 노드포트에 접속되는 포트이고 80번은 pod에 접속되는 포트 번호이다. nginx는 웹서비스라 80번을 사용하도록 함



`kubectl get po -o wide`

- pod가 어디있는지 확인
  - 위 실습에선 w2-k8s에 존재



**파드가 하나인데 하나의 파드가 죽으면,,,?**



## 2-3 파드와 디플로이먼트 차이

![image](https://user-images.githubusercontent.com/47052106/162733837-cfcf516e-b21e-47ef-9fbc-8a643e886188.png)

 

**원하는 구성도**

![image](https://user-images.githubusercontent.com/47052106/162733940-b6d09823-8c98-49e3-8329-502c3f10db17.png)



**배포 방법**

- `kubectl run`
  - 잘 안쓴다
  - 파드만 만들 수 있고, deployment를 못 만든다
- `kubectl apply`
  - yml 파일과 함께하여 deployment 생성

![image](https://user-images.githubusercontent.com/47052106/162733982-3ac05a2c-7e9a-459a-9e6f-10f22eccbab6.png)



**디플로이먼트로 다수의 파드를 만든다는 뜻은?**

- replicaSet을 구성한다는 것이다

![image](https://user-images.githubusercontent.com/47052106/162734155-24c6705b-a864-4213-adc5-28695c56e580.png)



**실습**

![image](https://user-images.githubusercontent.com/47052106/162732736-abc5b0d0-d428-44b1-9fb9-d379fb46b28f.png)

`kubectl create deployment deploy-nginx --image=nginx`

- kubectel create deployment <name> --image=<imageName>



![image](https://user-images.githubusercontent.com/47052106/162733253-0a14fdac-3bdd-418d-aef8-2acfbdf7230d.png)

`kubectl scale deployment deploy-nginx --replica=3`

- scale out



## 2-4 외부로 노출하는 더 좋은 방법인 로드밸런서

