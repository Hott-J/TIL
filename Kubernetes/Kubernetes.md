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



**디플로이먼트를 직접 노출시키는 건 좋지않다**



**노드포트보다 로드밸런서가 좋은점**

노드포트

- 노드의 ip가 노출됨

로드밸런서

- 대표하는 ip만 노출됨
- 노드로 가야할 경로를 최적화할 수 있음



**실습**

![image](https://user-images.githubusercontent.com/47052106/162859790-5e54f7c2-270e-4ed9-b7e3-fe8f32ac8966.png)



![image](https://user-images.githubusercontent.com/47052106/162860604-e7d15495-6ad1-42db-9093-59272aff4844.png)



**주의점**

**NodePort를 expose할 때**

- --port는 워커 노드 뒤에 연결되는 Pod/컨테이너/애플리케이션(모두 유사한 말)를 접속하기 위한 포트입니다.



**LoadBalancer를 expose할 때** 

- --port는 로드밸런서를 통해서 Pod에 접속되기 위해 노출되는 접속 포트 자체입니다. 



## 2-5 배포한 것들 삭제하기



**서비스**

- 거실같은 개념
- 다른 어떤 곳을 거쳐가기 위해 항상 들러야 하는 곳



**실습**

![image](https://user-images.githubusercontent.com/47052106/162861567-241629a7-6681-414d-8702-af67dc4e6e6e.png)



## 3-1 쿠버네티스 구성 요소 확인

- 전체 구조

![image](https://user-images.githubusercontent.com/47052106/162890547-7bb7482e-a41d-4103-b997-0b0a7c5b1914.png)

 쿠버네티스는 전체 클러스터를 관리하는 **마스터**와 컨테이너가 배포되는 **노드**로 구성되어 있습니다. 모든 명령은 마스터의 API 서버를 호출하고 노드는 마스터와 통신하면서 필요한 작업을 수행합니다. 특정 노드의 컨테이너에 명령하거나 로그를 조회할 때도 노드에 직접 명령하는 게 아니라 마스터에 명령을 내리고 마스터가 노드에 접속하여 대신 결과를 응답합니다.

#### Master

 마스터 서버는 다양한 모듈이 확장성을 고려하여 기능별로 쪼개져 있는 것이 특징 ~~고통~~ 입니다. 관리자만 접속할 수 있도록 보안 설정을 해야 하고 마스터 서버가 죽으면 클러스터를 관리할 수 없기 때문에 보통 3대를 구성하여 안정성을 높입니다. AWS EKS 같은 경우 마스터를 AWS에서 자체 관리하여 안정성을 높였고(마스터에 접속 불가) 개발 환경이나 소규모 환경에선 마스터와 노드를 분리하지 않고 같은 서버에 구성하기도 합니다.

#### Node

 노드 서버는 마스터 서버와 통신하면서 필요한 Pod을 생성하고 네트워크와 볼륨을 설정합니다. 실제 컨테이너들이 생성되는 곳으로 수백, 수천대로 확장할 수 있습니다. 각각의 서버에 라벨을 붙여 사용목적(GPU 특화, SSD 서버 등)을 정의할 수 있습니다.

#### Kubectl

 API 서버는 json 또는 protobuf 형식을 이용한 http 통신을 지원합니다. 이 방식을 그대로 쓰면 불편하므로 보통 `kubectl`이라는 명령행 도구를 사용합니다. 어떻게 읽어야 할지 난감한데 [공식적](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.9.md#kubectl)으로 큐브컨트롤(cube control)이라고 읽지만 큐브씨티엘, 쿱컨트롤, 쿱씨티엘등도 많이 쓰입니다.



- **Master**

  ![image](https://user-images.githubusercontent.com/47052106/162890411-ac4c96e5-d5f1-456b-b9e2-e3c9c41abb13.png)

#### API 서버 kube-apiserver

 API 서버는 모오오든 요청을 처리하는 마스터의 핵심 모듈입니다. kubectl의 요청뿐 아니라 내부 모듈의 요청도 처리하며 권한을 체크하여 요청을 거부할 수 있습니다. 실제로 하는 일은 원하는 상태를 key-value 저장소에 저장하고 저장된 상태를 조회하는 매우 단순한 작업입니다. Pod을 노드에 할당하고 상태를 체크하는 일은 다른 모듈로 분리되어 있습니다. 노드에서 실행 중인 컨테이너의 로그를 보여주고 명령을 보내는 등 디버거 역할도 수행합니다.

#### 분산 데이터 저장소 etcd

 RAFT 알고리즘을 이용한 key-value 저장소입니다. 여러 개로 분산하여 복제할 수 있기 때문에 안정성이 높고 속도도 빠른 편입니다. 단순히 값을 저장하고 읽는 기능뿐 아니라 watch 기능이 있어 어떤 상태가 변경되면 바로 체크하여 로직을 실행할 수 있습니다.

 클러스터의 모든 설정, 상태 데이터는 여기 저장되고 나머지 모듈은 stateless하게 동작하기 때문에 etcd만 잘 백업해두면 언제든지 클러스터를 복구할 수 있습니다. etcd는 오직 API 서버와 통신하고 다른 모듈은 API 서버를 거쳐 etcd 데이터에 접근합니다. [k3s](https://k3s.io/) 같은 초경량 쿠버네티스 배포판에서는 etcd대신 sqlite를 사용하기도 합니다.

#### 스케줄러, 컨트롤러

 API 서버는 요청을 받으면 etcd 저장소와 통신할 뿐 실제로 상태를 바꾸는 건 스케줄러와 컨트롤러 입니다. 현재 상태를 모니터링하다가 원하는 상태와 다르면 각자 맡은 작업을 수행하고 상태를 갱신합니다.

**스케줄러** kube-scheduler

스케줄러는 할당되지 않은 Pod을 여러 가지 조건(필요한 자원, 라벨)에 따라 적절한 노드 서버에 할당해주는 모듈입니다.

**큐브 컨트롤러** kube-controller-manager

 큐브 컨트롤러는 다양한 역할을 하는 아주 바쁜 모듈입니다. 쿠버네티스에 있는 거의 모든 오브젝트의 상태를 관리합니다. 오브젝트별로 철저하게 분업화되어 Deployment는 ReplicaSet을 생성하고 ReplicaSet은 Pod을 생성하고 Pod은 스케줄러가 관리하는 식입니다.

**클라우드 컨트롤러** cloud-controller-manager

 클라우드 컨트롤러는 AWS, GCE, Azure 등 클라우드에 특화된 모듈입니다. 노드를 추가/삭제하고 로드 밸런서를 연결하거나 볼륨을 붙일 수 있습니다. 각 클라우드 업체에서 인터페이스에 맞춰 구현하면 되기 때문에 확장성이 좋고 많은 곳에서 자체 모듈을 만들어 제공하고 있습니다.



- **Node**

  ![image](https://user-images.githubusercontent.com/47052106/162890456-f9814408-8708-4d92-80a1-002d94ef5ce7.png)

#### 큐블릿 kubelet

 노드에 할당된 Pod의 생명주기를 관리합니다. Pod을 생성하고 Pod 안의 컨테이너에 이상이 없는지 확인하면서 주기적으로 마스터에 상태를 전달합니다. API 서버의 요청을 받아 컨테이너의 로그를 전달하거나 특정 명령을 대신 수행하기도 합니다.

#### 프록시 kube-proxy

 큐블릿이 Pod을 관리한다면 프록시는 Pod으로 연결되는 네트워크를 관리합니다. TCP, UDP, SCTP 스트림을 포워딩하고 여러 개의 Pod을 라운드로빈 형태로 묶어  서비스를 제공할 수 있습니다. 초기에는 kube-proxy 자체가 프록시 서버로 동작하면서 실제 요청을 프록시 서버가 받고 각 Pod에 전달해 주었는데 시간이 지나면서 iptables를 설정하는 방식으로 변경되었습니다. iptables에 등록된 규칙이 많아지면 느려지는 문제 때문에 최근 IPVS를 지원하기 시작했습니다.

### 추상화

 컨테이너는 도커고 도커가 컨테이너라고 생각해도 무리가 없는 상황이지만 쿠버네티스는 CRI(Container runtime interface)를 구현한 다양한 컨테이너 런타임을 지원합니다. [containerd](https://containerd.io/)(사실상 도커..), [rkt](https://coreos.com/rkt/), [CRI-O](https://cri-o.io/) 등이 있습니다.

CRI 외에 CNI(네트워크), CSI(스토리지)를 지원하여 인터페이스만 구현한다면 쉽게 확장하여 사용할 수 있습니다.



## 3-2 쿠버네티스의 기본 철학

**Desired-State**

![image](https://user-images.githubusercontent.com/47052106/162892300-c1d2f89a-bb4a-459a-9617-4d7510daa80f.png)



 쿠버네티스에서 가장 중요한 것은 **desired state - 원하는 상태** 라는 개념입니다. 원하는 상태라 함은 관리자가 바라는 환경을 의미하고 좀 더 구체적으로는 얼마나 많은 웹서버가 떠 있으면 좋은지, 몇 번 포트로 서비스하기를 원하는지 등을 말합니다.

쿠버네티스는 복잡하고 다양한 작업을 하지만 자세히 들여다보면 **현재 상태 current state**를 모니터링하면서 관리자가 설정한 **원하는 상태**를 유지하려고 내부적으로 이런저런 작업을 하는 단순한(?) 로직을 가지고 있습니다.

이러한 개념 때문에 관리자가 서버를 배포할 때 직접적인 동작을 명령하지 않고 상태를 선언하는 방식을 사용합니다. 예를 들어 “nginx 컨테이너를 실행해줘. 그리고 80 포트로 오픈해줘.”는 현재 상태를 원하는 상태로 바꾸기 위한 **명령 imperative**이고 “80 포트를 오픈한 nginx 컨테이너를 1개 유지해줘”는 원하는 상태를 **선언declarative** 한 것입니다. ~~더 이해가 안 된다~~

언뜻 똑같은 요청을 단어를 살짝 바꿔 말장난하는 게 아닌가 싶은데, 이런 차이는 CLI 명령어에서도 드러납니다.

```shell
$ docker run # 명령
$ kubectl create # 상태 생성 (물론 kubectl run 명령어도 있지만 잘 사용하지 않습니다)
```



**Pod Sequence Diagram**

![image](https://user-images.githubusercontent.com/47052106/162892124-106f8a05-5aa6-473b-99a6-949030af4941.png)



 흐름을 보면 각 모듈은 서로 통신하지 않고 오직 API Server와 통신하는 것을 알 수 있습니다. API Server를 통해 etcd에 저장된 상태를 체크하고 현재 상태와 원하는 상태가 다르면 필요한 작업을 수행합니다. 각 모듈이 하는 일을 보면 다음과 같습니다.



**kubectl**

-  ReplicaSet 명세를 yml파일로 정의하고 kubectl 도구를 이용하여 API Server에 명령을 전달
-  API Server는 새로운 ReplicaSet Object를 etcd에 저장

**Kube Controller**

-  Kube Controller에 포함된 ReplicaSet Controller가 ReplicaSet을 감시하다가 ReplicaSet에 정의된 Label Selector 조건을 만족하는 Pod이 존재하는지 체크
-  해당하는 Label의 Pod이 없으면 ReplicaSet의 Pod 템플릿을 보고 새로운 Pod(no assign)을 생성. 생성은 역시 API Server에 전달하고 API Server는 etcd에 저장

**Scheduler**

-  Scheduler는 할당되지 않은(no assign) Pod이 있는지 체크
-  할당되지 않은 Pod이 있으면 조건에 맞는 Node를 찾아 해당 Pod을 할당

**Kubelet**

-  Kubelet은 자신의 Node에 할당되었지만 아직 생성되지 않은 Pod이 있는지 체크
-  생성되지 않은 Pod이 있으면 명세를 보고 Pod을 생성
  - 컨테이너 런타임에게 Pod 생성 요청하여 컨테이너 런타임이 Pod 생성
-  Pod의 상태를 주기적으로 API Server에 전달

 위의 예제는 ReplicaSet에 대해 다뤘지만 모든 노드에 Pod을 배포하는 DaemonSet도 동일한 방식으로 동작합니다. DaemonSet controller와 Scheduler가 전체 노드에 대해 Pod을 할당하면 kubelet이 자기 노드에 할당된 Pod을 생성하는 식입니다.

각각의 모듈이 각자 담당한 상태를 체크하고 독립적으로 동작하는 것을 보면서 참 잘 만든 마이크로서비스 구조라는 생각이 듭니다.



## 3-3 실제 쿠버네티스의 파드 배포 흐름

![image](https://user-images.githubusercontent.com/47052106/162893641-0d98f2d5-e6e8-45a3-b4ea-cff9ca7b9b30.png)

 

* 참고

https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%89%BD%EA%B2%8C%EC%8B%9C%EC%9E%91/lecture/71413

https://subicura.com/2019/05/19/kubernetes-basic-1.html?utm_source=subicura.com&utm_medium=referral&utm_campaign=k8s

https://subicura.com/k8s/prepare/#%E1%84%8F%E1%85%AE%E1%84%87%E1%85%A5%E1%84%82%E1%85%A6%E1%84%90%E1%85%B5%E1%84%89%E1%85%B3%E1%84%80%E1%85%A1-%E1%84%8E%E1%85%A5%E1%84%8B%E1%85%B3%E1%86%B7%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%80%E1%85%A1%E1%84%8B%E1%85%AD