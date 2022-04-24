# Blocking I/O & Non-Blocking I/O



- Blocking (x) 

- Blocking I/O (o)



*Blocking I/O 는 기본적으로 Synchronous*



- I/O는 커널이 하는 일

- 동기화는 커널의 대답을 기다리는 것

- 비동기화는 커널에 일시켜 놓고 다른 일을 하는 것

 

**동기 입출력**

![image](https://user-images.githubusercontent.com/47052106/164960852-168e7e78-8074-4976-9813-7214efedd9e8.png)

- fopen() call
- file system에 입출력을 시도하는 인터페이스로 내려감
- Device Driver를 움직임
- 실제로 disk에 write (2차 메모리)
  - 여기까지 안가기도 함
- 다 썼다고 알려줌
- fprintf() 리턴



**비동기 입출력**

- 기본적으로 스레드 2개 이상의 환경

![image](https://user-images.githubusercontent.com/47052106/164964895-e63b2d57-c99f-47eb-aaee-cb27368bed54.png)

- fopen() call
- file system에 입출력을 시도하는 인터페이스로 내려감
- fprintf() return!
  - I/O request pending
- 이후에, disk write
- 완료되면 Thread2에 다 됬다고 알려줌
  - 완료가 언제 되는가?
  - 대충짬 -> 본인 PC에서는 잘됨 -> 고객 PC에선 안됨
  - 우연에 맡기는 프로그래머
    - sleep() 남발하는 프로그래머



추가자료

- https://baek-kim-dev.site/38