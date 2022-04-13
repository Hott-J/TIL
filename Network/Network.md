#  도커 / 쿠버네티스 /클라우드 네트워크 이해



### 우리가 이해를 못하는 이유는 무엇인가

- 리눅스
  - namespace

- CS 기본개념
- 클라우드에 대한 이해
- 온프레미스에 대한 이해
  - 결국 이 개념이 클라우드로 `소프트화` 된 것
- 이것들을 모르면 가장 중요한 **Trouble Shooting**을 할 수 가 없다



### 도커 네트워크의 이해



**Keywords**

- docker0
- bridge
- veth



**Architecture**

![image](https://user-images.githubusercontent.com/47052106/163109725-c30c39a1-3834-4774-bfcb-7f2ae9d2b016.png)

**docker0**

- `bridge`를 `소프트웨어화`한 네트워크 인터페이스



컨테이너들이 연결이 될 수 있는데, 이 연결이 브릿지에 연결될 수 있고 이를 veth라는 기술을 써서 각 컨테이너에 연결됨

- *너 `bridge` 알아?*
- *너 `container` 알아?*



**Network bridge**

![image](https://user-images.githubusercontent.com/47052106/163110156-8b406743-ecc8-4109-8ae6-71520d640976.png)

- 2개 이상의 네트워크를 L2 레벨로 연결하여 1개의 싱글 LAN(docker0) 으로 통신 (스위치와 유사)
- 이게 소프트웨어적으로 올라올 수 있는 것!!!
- 원래는 하드웨어장비



**Container**

- `독립된` 리눅스 머신 `하나` (논리적)
- 독립된 리눅스 공간을 보장받기는 하지만 사실은 `프로세스`이다
  - 프로세스지만 리눅스 커널 기준으로 Linux의 `namespace`와 `cgroup`을 해당 프로세스에 `적용`한 것
  - 이를 통해 자연스럽게 독립된 공간이 보장됨



**veth**

- Pair 가상 네트워크 인터페이스 (두 개의 namespace를 연결)
- 호스트와 (네트워크 네임스페이스만 격리된) 컨테이너를 연결하는 가상 인터페이스



**namespace**

- 커널에서 제공해주는 자원들을 독립적으로 사용하게끔 해준다

- 네임스페이스는 동일한 시스템에서 별개의 독립된 공간을 격리된 환경에서 운영하는 가상화 기술. 이는 아파트가 각 호실별로 격리된 주거환경을 제공하는 것과 비슷
- 네트워크 네임스페이스 등
  - 격리된 네트워크 공간을 만들어 두면 OS와 컨테이너간 동일 port 사용 가능
  - nginx 컨테이너, apache 컨테이너는 둘다 웹서버 80포트를 동시에 사용할 수 있음
    - namespace를 적용하는 순간 네트워크 자원을 나눠갖으므로 각 컨테이너마다 80포트를 사용할 수 있음
    - 실제로는 그렇지 않지만 내부적으로는 80포트를 쓴다라고 생각
- 버젼충돌, 포트충돌에 대한 걱정을 안해도됨



![image](https://user-images.githubusercontent.com/47052106/163113226-bb56c220-89c5-495f-b197-e79f09d85524.png)

- 컨테이너 3개 생성했더니 docker0에 veth 3개가 연결됨을 확인 (bridge)



**컨테이너 내부 접속**

![image](https://user-images.githubusercontent.com/47052106/163114009-16668d79-ed85-4659-80be-d68b0497ab04.png)

**eth0**

- ip 할당받게 되는 network interface



**각 컨테이너마다 내부망 생성 확인**

![image](https://user-images.githubusercontent.com/47052106/163114638-e0717b7b-279c-48e8-bb2f-dfec5050d62b.png)

- `docker inspect $(docker ps -q) | grep "IPAddress\|Id"`





### 쿠버네티스 네트워크의 이해



**Ingress**

- 외부접속 가능한 URL 경로에 따른 교통정리
- DNS에 대한 개념 (도메인 <-> IPAddress)
  - 로컬에 있을 수도 있고, 외부에 있을 수도 있다.
  - ![image](https://user-images.githubusercontent.com/47052106/163115546-54288abb-32a0-453b-adc2-be85f6a0bdee.png)



**pod**

- 컨테이너라고 보자
- 각각의 프로세스



**Service(Cluster IP)**

- pod를 묶어서 관리

- 각각 pod마다 ip 할당받음
  - 하지만 pod ip로 바로 접근하지 않고 Service를 통해 접근한다
    - 하나의 pod가 죽었을 경우, 새로 pod가 띄워지지만 이는 새로운 ip를 할당받으므로

- NodePort
  - 굳이 url로 접근하지 않아도 되는 상황이라면 ip address를 가지고 접근



### 추가적인 공부

![image](https://user-images.githubusercontent.com/47052106/163145339-e889495b-0407-4315-8b28-ad95299ed244.png)

**Proto** : 프로토콜의 종류 (TCP/UDP)

 

**Local Address**  

- `로컬 (자신) IP와 포트번호`, `0.0.0.0` 은 특정 아이피와 연결되어 있지 않음을 의미. 즉 어느 IP와도 연결 가능한 상태

- **127.0.0.1, 127.0.1.1, ::1 (for IPv6)** → localhost, the loop back interface - those services can only be contacted from your local machine
  - 루프백 인터페이스로서, 자기 자신만 호출 가능한 상태
-  **0.0.0.0:xxx, :::xxx** → any local address:port-number - active connections: the IP-address and the port used by that special connection
  - 모든 인터페이스를 받는다는 뜻

 

**Foreign Address**  :

- `상대측 IP와 포트번호`,` 0.0.0.0 `은 아직 통신이 시작되지 않았으며 특정한 IP와 포트가 연결되지 않았음을 의미.

- UDP프로토콜은 소켓을 상대측의 주소와 포트를 연결하지 않으므로 상대측은 `*:*` 표시됨.
- 참고로 `:` 기호는 IPv6 용이다

 

**State**

- LISTENING : 현재 서비스를 대기중 

- ESTABLISHED : 다른 컴퓨터와 연결된 상태

- CLOSED : 연결이 완전히 종료된 상태

- TIME WAIT : 연결은 종료되었지만 당분간 소켓은 열어놓은 상태

 

**Send-Q, Recv-Q**

- 보내고 받는 패킷의 socket buffer size

- data 송/수신할때 크기가 변하게 됨

- Recv-Q : 전송받은 bytes중 아직 처리 못하고 recv()하고 있는 상태의 data RNXT – RACK 

- Send-Q : send() 되었으나 아직 전송되지 못하고 대기하고 있는 상태 SNXT – SUNA 





**실습**

![image](https://user-images.githubusercontent.com/47052106/163181979-48f3c11c-9c07-48ce-a298-e56f285ffc9b.png)



```
# 브릿지 생성 및 셋업
ip link add br0 type bridge
ip link set br0 up
ip addr add 10.201.0.1/24 brd 10.201.0.255 dev br0
iptables --policy FORWARD ACCEPT #방화벽 DROP -> ACCEPT 변경

# container4 네트워크 네임스페이스 셋업
# 먼저 container4라는 네트워크 네임스페이스를 하나 만들어줍니다. brid4, veth4 쌍으로 된 가상 인터페이스들을 생성합니다. veth4를 container4 네트워크 네임스페이스에 연결하고, ip(10.201.0.4)를 할당해줍니다. 마지막으로 container4 네트워크 네임스페이스의 lo와 veth4와 디바이스를 활성화합니다.
ip netns add container4
ip link add brid4 type veth peer name veth4
ip link set veth4 netns container4
ip netns exec container4 ip a add 10.201.0.4/24 dev veth4
ip netns exec container4 ip link set dev lo up
ip netns exec container4 ip link set dev veth4 up
ip link set brid4 master br0
ip link set dev brid4 up
ip netns exec container4 ip route add default via 10.201.0.1

# container5 네트워크 네임스페이스 셋업
ip netns add container5
ip link add brid5 type veth peer name veth5
ip link set veth5 netns container5
ip netns exec container5 ip a add 10.201.0.5/24 dev veth5
ip netns exec container5 ip link set dev lo up
ip netns exec container5 ip link set dev veth5 up
ip link set brid5 master br0
ip link set dev brid5 up
ip netns exec container5 ip route add default via 10.201.0.1

# NAT 및 DNS 셋업
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 10.201.0.0/24 -j MASQUERADE
mkdir -p /etc/netns/container4/
echo 'nameserver 8.8.8.8' > /etc/netns/container4/resolv.conf
mkdir -p /etc/netns/container5/
echo 'nameserver 8.8.8.8' > /etc/netns/container5/resolv.conf
```

