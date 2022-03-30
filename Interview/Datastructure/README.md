# Data Structure

<br>

## Table of Contents

* [배열과 연결 리스트](#배열과-연결-리스트)
* [배열 리스트와 연결 리스트](#배열-리스트와-연결-리스트)
* [해시 테이블](#해시-테이블)
  * [해시 충돌](#해시-충돌)
* [스택과 큐](#스택과-큐)
* [트리 (Tree)](#트리-tree)
  * [트리 순회](#트리-순회)
* [힙 (Heap)](#힙-heap)
* [이진 탐색 트리 (Binary Search Tree)](#이진-탐색-트리-binary-search-tree)
  * [시간 복잡도](#시간-복잡도)
* [그래프 (Graph)](#그래프-graph)
  * [구현 방법과 장단점](#구현-방법과-장단점)
* [[참고] Cache Locality](#참고-cache-locality)

<br>

## 배열과 연결 리스트
* 삽입과 삭제가 빈번하게 일어난다면 LinkedList를 사용하는 것이 좋음
* 데이터에 접근하는 것이 빈번하게 일어난다면 Array를 사용하는 것이 좋음
### 👉 배열 (Array)
* `메모리 상에 연속적으로 데이터를 저장하는` 자료구조
* `탐색 O(1)`: 인덱스를 사용해 `Random Access` 가능
* `삽입/삭제 O(N)`: 삽입/삭제한 원소보다 큰 인덱스를 갖는 원소들을 `Shift`해야 함
* `크기 고정적` (선언 시 지정한 크기 변경 불가): `Immutable`
* * Cache Locality가 좋아 Cache Hit 가능성이 큼

### 👉 연결 리스트 (Linked List)
* `메모리가 불연속적`으로 배치된 자료구조
* 다음 노드를 가리키는 `주소인 포인터`를 통해 접근하는 자료구조 (자료의 주소 값으로 서로 연결) 
* `탐색 O(N)`: 데이터 검색 시 처음 노드부터 순회하는 `순차 접근`
* `삽입/삭제 O(1)`: 주소의 연결만 바꾸면 됨 -> 하지만, 삽입/삭제할 원소를 찾는 것에 O(N)이 걸림

<br>

## 배열 리스트와 연결 리스트
* 삽입과 삭제가 빈번하게 일어난다면 LinkedList를 사용하는 것이 좋음
* 데이터에 접근하는 것이 빈번하게 일어난다면 ArrayList를 사용하는 것이 좋음

### 👉 배열 리스트 (Array List)
* 내부적으로는 배열을 활용하는 자료구조, `메모리가 연속적`으로 배치
* `탐색 O(1)`: 인덱스를 사용해 `Random Access` 가능
* `삽입/삭제 O(N)`: 해당 데이터를 제외한 모든 데이터로 임시 배열을 생성해 복사하므로 삽입, 삭제가 빈번할 경우 속도가 느림

### 👉 연결 리스트 (Linked List)
* `메모리가 불연속적`으로 배치된 자료구조
* 다음 노드를 가리키는 `주소인 포인터`를 통해 접근하는 자료구조 (자료의 주소 값으로 서로 연결) 
* `탐색 O(N)`: 데이터 검색 시 처음 노드부터 순회하는 `순차 접근`
* `삽입/삭제 O(1)`: 주소의 연결만 바꾸면 됨 -> 하지만, 삽입/삭제할 원소를 찾는 것에 O(N)이 걸림
* 포인터 사용으로 인한 메모리 낭비가 있음

<br>

## 해시 테이블
### 👉 정의
* `Key와 Value`로 데이터를 저장하는 자료구조
* Key에 `해시 함수`를 적용해 고유한 인덱스(`해시 값`)를 생성하고, 이 인덱스를 활용해 값을 저장/검색
* 실제 값이 저장되는 장소를 버킷(슬롯)이라고 함
* 배열과 리스트의 장점을 합친 자료구조로 `key 값`을 통해 해시 주소를 알아내어 평균적으로 탐색에 `O(1)`을 보장하는 자료구조

### 👉 해시 함수
* 임의의 길이의 데이터를 수학적 연산을 통해 `고정된 길이의 데이터로 매핑`하는 함수
* 해시 함수에 의해 얻어지는 값을 `해시`라고 함

### 👉 해시 충돌
* `서로 다른 key가 같은 해시 값으로 변경`되는 것
* 같은 해시 값에 대해 데이터를 조회해 탐색에 최대 `O(N)` 가능
* `체이닝`: 추가 메모리를 사용해 버킷에 데이터를 `연결 리스트`로 관리
* `개방 주소법`: 기존의 비어있는 버킷의 공간을 활용
  * 선형 조사법(Linear Probing): 현재 버킷의 인덱스에서 `고정 폭`씩 이동하며 데이터를 버킷에 저장
  * 이차 조사법(Quadratic Probing): 현재 버킷의 인덱스에서 `k^2`(k=1, 2, ..)씩 이동하며 데이터를 버킷에 저장
  * 이중 해싱(Double Hashing Probing): 해싱된 값을 한번 더 해싱 -> 연산 증가
* 많은 데이터를 효율적으로 관리하기 위해 하드디스크나, 클라우드에 존재하는 무한한 데이터들을 유한한 개수의 해시값으로 매핑하면 작은 메모리로도 프로세스 관리가 가능해져서 사용함

<br>

## 스택과 큐
### 👉 스택 (Stack)
* `LIFO(Last In First Out)` 방식으로 삽입되고 제거되는 `최근성`에 포커싱된 자료구조
* Array로 구현하는 것이 좋음

### 👉 큐 (Queue)

* `FIFO(First In First Out)` 방식으로 삽입되고 제거되는 `순차성`에 포커싱된 자료구조
* Linked List로 구현하는 것이 좋음

<br>

## 트리 (Tree)
### 👉 정의
* `사이클을 가지지 않는 그래프` (비선형 자료구조)
* 부모 자식 관계를 갖는 `계층적` 구조를 갖는 자료구조

### 👉 종류
* `이진 트리(Binary Tree)`: 최대 2개의 자식 노드들만 가질 수 있는 트리
* `포화 이진 트리(Perfect Binary Tree)`: 각 레벨에 노드가 꽉 차있는 트리
* `완전 이진 트리(Complete Binary Tree)`: 높이가 K인 트리에서 레벨 1~K-1까지 모두 채워져 있고 마지막 레벨에서는 왼쪽부터 순서대로 채워져 있는 트리
* `이진 탐색 트리(Binary Search Tree)`: 탐색을 위해 만들어진 자료구조로 `부모 노드의 키 값이 왼쪽 자식 노드의 키 값보다 크고 오른쪽 자식 노드의 키 값보다 작은` 트리

### 👉 트리 순회
* 중위 순회: 왼 -> 루트 -> 오른
* 전위 순회: 루트 -> 왼 -> 오른
* 후위 순회: 왼 -> 오른 -> 루트

<br>

## 힙 (Heap)
### 👉 정의
* 힙은 `완전 이진 트리`의 일종으로 `우선 순위 큐`를 구현하기 위해 만들어진 자료구조
* 이진 탐색 트리가 전체 노드를 탐색하기 위한 자료구조라면 힙은 `최소값 또는 최대값`을 쉽게 찾기 위한 자료구조
* 힙은 중복 값 허용 (이진 탐색 트리는 중복값 허용X)
* `부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰/작은 완전 이진 트리`로 힙은 자식 노드에도 구분 조건이 필요한 이진 탐색 트리보다 `느슨한 정렬` 상태를 유지
### 👉 종류
#### 최대 힙(max heap)
* `부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은` 완전 이진 트리
* 부모가 최대값
#### 최소 힙(min heap)
* `부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은` 완전 이진 트리
* 부모가 최소값

### 👉 시간 복잡도
* 원소 삽입: `O(logn)`
  * 새로운 노드를 힙의 마지막 노드에 삽입 -> 새로운 노드를 부모 노드들과 교환
* 원소 삭제: `O(logn)`
  * 루트 노드 삭제 -> 삭제된 루트에 힙의 마지막 노드를 가져옴 -> 재구성

<br>

## 이진 탐색 트리 (Binary Search Tree)
### 👉 정의
* 노드의 `왼쪽 서브 트리에는 그 노드의 값보다 작은 값들`을 지닌 노드들로 구성, `오른쪽 서브 트리에는 그 노드의 값보다 큰 값들`을 지닌 노드들로 구성
* `중위 순회`: 검색 시 내려가면서 해당 노드보다 찾는 값이 더 작으면 왼쪽에서 찾고, 찾는 값이 더 크면 오른쪽에서 찾음
* 중복 값을 가지지 않음
* 이진탐색과 연결 리스트가 결합된 자료 구조
  * 이진탐색 : `탐색에 소요되는 시간복잡도는 O(logN)`, but `삽입,삭제가 불가능`
  * 연결 리스트 : `삽입, 삭제의 시간복잡도는 O(1)`, but `탐색 시간복잡도가 O(N)`

### 👉시간 복잡도
* 탐색/삽입/삭제 평균 시간 복잡도: `O(logN)`
* 탐색/삽입/삭제 최악 시간 복잡도: `한쪽으로만 삽입된 경우 O(N)`
* 시간복잡도는 `트리의 Depth에 비례`
* 최악의 경우를 방지하는 방법: 자가 균형 트리(Balanced Tree)
  * `AVL 트리`: 왼쪽과 오른쪽 자식의 높이 차이가 1이하일 것을 요구, 삭제/추가 시에 재정렬을 통해 높이를 일정하게 유지, 레드 블랙 트리보다 엄격
  * `레드 블랙 트리`: 모든 노드가 빨강 또는 검정의 색을 갖는 트리로 루트부터 리프까지의 최장 경로는 최단 경로의 두 배 이상이 될 수 없음, 삭제/추가 시에 재정렬과 색깔 재배치를 통해 규칙을 유지

<br>

## 그래프 (Graph)

* 정점과 간선으로 이루어진 자료구조

### 구현 방법과 장단점
* `인접 행렬` 사용: 2차원 배열을 사용해 정점들의 연결관계를 파악하는 방법으로, 시간 복잡도 `O(1)`로 연결 관계를 파악할 수 있음, `정점과 엣지가 많을 경우 사용`, 구현 간편, 공간 낭비
* `인접 리스트` 사용: 각 정점의 adjacent list를 통해서 연결 관계를 파악하는 방법으로, 정점들의 관계를 `O(정점에 연결된 노드의 수)`로 파악하는 방법, `정점과 엣지가 적을 경우 사용`, 공간 낭비 적음, 탐색 시간이 느림, 구현 어려움

<br>

## [참고] Cache Locality
* Cache Locality
  * 시간 지역성: 최근에 접근한 데이터는 빠르게 다시 접근할 수 있음 (for, while 반복문)
  * 공간 지역성: 참조된 데이터 근처에 있는 데이터가 잠시 후에 사용될 가능성이 높음
    * 배열은 물리적으로 연속된 공간에 데이터를 저장하여 공간 지역성이 좋음
* Cache hit: 지역성을 활용하기 위해 캐쉬에 저장해놓은 메모리에 CPU가 참조하고자 하는 메모리가 있다면 cahce hit, 반대는 cache miss