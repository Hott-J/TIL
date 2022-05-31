# DB 인덱싱하는 이유와 원리와 내부구조

**인덱스**

- 데이터베이스의 테이블에 대한 검색 속도를 향상시켜주는 자료구조이다.
- 테이블의 특정 컬럼에 인덱스를 생성하면, 해당 컬럼의 데이터를 정렬한 후 별도의 메모리 공간에 데이터의 물리적 주소와 함께 저장된다.
- 컬럼의 값과 물리적 주소를 (key, value)의 한 쌍으로 저장한다.
- 추가적으로, Clustered Index와 Non-Clustered Index 개념도 찾아보자



*자료구조*

- 선형

  - Linked-List

- 비선형

  - 이진트리

  - B트리

    

**인덱스를 사용하면 좋은 경우**

- 규모가 큰 테이블
- 삽입, 수정, 삭제 작업이 자주 발생하지 않는 컬럼
  - 삭제가 제일 문제
- WHERE나 ORDER BY, JOIN 등이 자주 사용되는 컬럼
- 데이터의 중복도가 낮은 컬럼



**인덱스의 자료구조**

- 해시 테이블
  - 실제로 잘 사용되지 않음
  - 그 이유로는, 해시테이블은 등호 연산에 최적화되어있기 때문. 디비는 부등호 연산이 자주 사용됨
    - 해시 테이블 내의 데이터들은 정렬되어 있지 않으므로 부등호 연산이 빠르지 않다
  - Hash Collision 고려해야함
- B+ Tree
  - B+ Tree는 B-Tree의 단점을 개선?
    - 조회시에는 개선한게 맞다
      - 인덱싱은 조회위주
    - File System은 B-Tree를 사용함
      - 삭제나 업데이트가 잦으므로
    - 삭제나 업데이트 같은 경우 B+Tree가 오히려 안좋다



**커널을 누가 갖고 있는가**

- OS
- DB



**데이터는 결국 파일의 형태로 저장되어 있다**

- 파일 4번7번9번1번3번5번...
  - 파일은 HDD에 저장
  - 해당 순서는 저장 순서 (파일은 뒤에 계속 추가하는 방식으로 늘어남)
  - 결국 이는 내가 원하는 값을 검색하기 어려움
  - 인덱스?
    - 기본적으로 RAM 메모리에 들어있음 (1차)
    - 빠른 검색
    - 존재하지 않는 데이터를 판단
      - 6번이 있는가?
      - 선형검색자료구조라면 풀스캔을 해야함 (총 6번)
      - 즉, 비선형검색자료구조를 이용!
    - 이진트리 사용
      - ![image](https://user-images.githubusercontent.com/47052106/171103571-3b3dd44d-11d7-4ff8-a0f8-ceeb855b6491.png)
      - 2번만에 6이 존재하는지 안하는지 알 수 있음
      - but, 이진트리는 하나의 노드안에 하나의 key만 존재
      - B-Tree는 하나의 노드안에 여러개의 key가 존재함 (depth가 낮아짐)



**B-tree란**

![image](https://user-images.githubusercontent.com/47052106/171109425-8c917e40-831c-4add-b502-b1ab3f03bb4a.png)

```
1. node의 key의 수가 k개라면, 자식 node의 수는 k+1개이다. 
2. node의 key는 반드시 정렬된 상태여야 한다. 
3. 자식 node들의 key는 현재 node의 key를 기준으로 크기 순으로 나뉘게 된다. 
4. root node는 항상 2개 이상의 자식 node를 갖는다. (root node가 leaf node인 경우 제외) 
5. M차 트리일 때, root node와 leaf node를 제외한 모든 node는 최소 ⌈M2⌉⌈M2⌉\left \lceil \frac{M}{2} \right \rceil, 최대 MMM개의 서브 트리를 갖는다. 
6. 모든 leaf node들은 같은 level에 있어야 한다. 
```



**B+tree란**

![image](https://user-images.githubusercontent.com/47052106/171109524-811febd9-75d0-49c3-8f5a-ec267af5c8e8.png)

```
1. leaf node를 제외하고 데이터를 저장하지 않기 때문에 메모리를 더 확보할 수 있다. 따라서 하나의 node에 더 많은 포인터를 가질 수 있기 때문에 트리의 높이가 더 낮아지므로 검색 속도를 높일 수 있다. (cache-hit)
 
2. Full scan을 하는 경우 B+Tree는 leaf node에만 데이터가 저장되어 있고, leaf node끼리 linked list로 연결되어 있기 때문에 선형 시간이 소모된다. 반면 B-Tree는 모든 node를 확인해야 한다. 
 
반면, B-Tree의 경우 최상의 경우 특정 key를 root node에서 찾을 수 있지만, B+Tree의 경우 반드시 특정 key에 접근하기 위해서 leaf node까지 가야 하는 단점이 있다.  
```



**B+Tree 사용 이유**

-   인덱스 컬럼은 부등호를 이용한 순차 검색 연산이 자주 발생할 수 있다. 따라서 B+Tree의 Linked list를 이용하면 순차 검색을 효율적으로 할 수 있게 된다. 



**인덱싱 적용 예시**

![image](https://user-images.githubusercontent.com/47052106/171113500-73eb67ad-2776-48e9-9a9a-ea01f6de8b18.png)

![image](https://user-images.githubusercontent.com/47052106/171113531-c6956e15-b13f-4383-801e-f5703ea0eae8.png)