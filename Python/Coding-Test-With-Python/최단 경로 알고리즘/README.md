# :book: 최단 경로 알고리즘

## 최단 경로 문제

- 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미
- 다양한 문제 상황
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 *노드*로 표현
- 지점 간 연결된 도로는 그래프에서 *간선*으로 표현

![노드간선](https://user-images.githubusercontent.com/47052106/105572383-2ca09400-5d9a-11eb-83f4-42f65667b40d.JPG)

### 다익스트로 최단 경로 알고리즘 개요

- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
  - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않는다
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

- 동작 과정
  - 출발 노드를 설정
  - 최단 거리 테이블을 초기화
  - 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택 (그리디)
  - 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
  - 위 과정에서 3번과 4번을 반복

![다익1](https://user-images.githubusercontent.com/47052106/105572385-2dd1c100-5d9a-11eb-8f05-26664219239e.JPG)

![다익2](https://user-images.githubusercontent.com/47052106/105572386-2e6a5780-5d9a-11eb-8911-7f5dd62f77b8.JPG)

![다익동작1](https://user-images.githubusercontent.com/47052106/105572388-2e6a5780-5d9a-11eb-9aea-85b90745fe69.JPG)

![동작2](https://user-images.githubusercontent.com/47052106/105572390-2f02ee00-5d9a-11eb-9586-413902437997.JPG)

![동작3](https://user-images.githubusercontent.com/47052106/105572391-2f9b8480-5d9a-11eb-87f1-54552819e126.JPG)

![동작4](https://user-images.githubusercontent.com/47052106/105572392-2f9b8480-5d9a-11eb-95e0-60ef55349fc7.JPG)

![동작5](https://user-images.githubusercontent.com/47052106/105572393-30341b00-5d9a-11eb-9b43-8094f298f26d.JPG)

![동작6](https://user-images.githubusercontent.com/47052106/105572394-30ccb180-5d9a-11eb-9a73-6bf55fb1cd82.JPG)

![동작7](https://user-images.githubusercontent.com/47052106/105572395-30ccb180-5d9a-11eb-8b20-d66ca2086f04.JPG)

- 그리디 알고리즘
  - 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않습니다.
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있습니다.
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됩니다.
  - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 합니다.
  
- 간단한 구현 방법
  - 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)합니다.

```python
import sys
input=sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m= map(int,input().split())
# 시작 노드 번호를 입력받기
start=int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph=[[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited=[False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a,b,c=map(int,input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:
      min_value=distance[i]
      index=i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start]=0
  visited[start]=True
  for j in graph[start]:
    distance[j[0]]=j[1]
  # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost=distance[now]+j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost<distance[j[0]]:
        distance[j[0]]=cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print("INF")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
```

- 총 O(v) 번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 합니다.
- 따라서 전체 시간 복잡도는 O(v^2) 입니다.
- 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 이 코드로 문제를 해결할 수 잇다.
  - 하지만 노드의 개수가 10000개 넘어가는 문제라면 어떻게 해야 할까요?

### 우선순위 큐

![우선순위큐](https://user-images.githubusercontent.com/47052106/105607095-44027000-5de0-11eb-84ff-2efbd5ab77c4.JPG)

### 힙

![힙](https://user-images.githubusercontent.com/47052106/105607114-5bd9f400-5de0-11eb-86d5-18477be6270c.JPG)

### 최소 힙

```python
import heapq

# 오름차순 힙 정렬
def heapsort(iterable):
  h=[]
  result=[]
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

### 최대 힙

```python
import heapq

# 내림차순 힙 정렬
def heapsort(iterable):
  h=[]
  result=[]
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,-value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용
- 다익스트라 알고리즘이 동작하는 기본 원리는 동일
  - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다름
  - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용
  
![다익우선](https://user-images.githubusercontent.com/47052106/105615486-74640180-5e14-11eb-97c0-b75fd093d10c.JPG)

![1](https://user-images.githubusercontent.com/47052106/105615491-7cbc3c80-5e14-11eb-9ba1-d69d54295c5c.JPG)

![2](https://user-images.githubusercontent.com/47052106/105615492-7ded6980-5e14-11eb-994d-6cef6b35476e.JPG)

![3](https://user-images.githubusercontent.com/47052106/105615493-7e860000-5e14-11eb-9349-630044c88899.JPG)

![4](https://user-images.githubusercontent.com/47052106/105615494-7e860000-5e14-11eb-8a95-1bfd3b514891.JPG)

![5](https://user-images.githubusercontent.com/47052106/105615495-7f1e9680-5e14-11eb-9fbf-29a37a59e066.JPG)

![7](https://user-images.githubusercontent.com/47052106/105615496-7f1e9680-5e14-11eb-872e-849cdba45216.JPG)

![8](https://user-images.githubusercontent.com/47052106/105615497-7fb72d00-5e14-11eb-8090-9429590dc661.JPG)

![9](https://user-images.githubusercontent.com/47052106/105615498-7fb72d00-5e14-11eb-9ab7-c5accc6455fa.JPG)

```python
import heapq
import sys
input=sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m= map(int,input().split())
# 시작 노드 번호를 입력받기
start=int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph=[[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a,b,c=map(int,input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist,now=heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now]<dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost=dist+i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘을 수행
dikstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i]==INF:
    print("INF")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
```

- 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV) 입니다.
- 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 회수로는 처리되지 않습니다.
  - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있습니다.
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사
  - 시간 복잡도를 O(ElogE)로 판단
  - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리
    - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV)

### 플로이드 워셜 알고리즘
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다.
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속함
  
![플로이드](https://user-images.githubusercontent.com/47052106/105636840-7d54e180-5ead-11eb-89a5-f5f561cce656.JPG)

![1](https://user-images.githubusercontent.com/47052106/105636842-7e860e80-5ead-11eb-9f3d-27c4d23ee390.JPG)

![2](https://user-images.githubusercontent.com/47052106/105636843-7e860e80-5ead-11eb-9a50-2daf8644b3b5.JPG)

![3](https://user-images.githubusercontent.com/47052106/105636846-7f1ea500-5ead-11eb-93c0-3544a82c45db.JPG)

![4](https://user-images.githubusercontent.com/47052106/105636847-7f1ea500-5ead-11eb-93b4-a6408c0ff368.JPG)

![5](https://user-images.githubusercontent.com/47052106/105636848-7fb73b80-5ead-11eb-97e4-7e70af20323a.JPG)

```python
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m= int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph=[[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0
      
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a,b,c=map(int,input().split())
  graph[a][b]=c
  
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if graph[a][b]==INF:
      print("INF",end="")
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b],end="")
  print()
```  

### 플로이드 워셜 알고리즘 성능 분석

- 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행
  각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려
- 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)입니다.

### 문제

![진보](https://user-images.githubusercontent.com/47052106/105698100-c443e500-5f48-11eb-82bd-7a10a85da271.JPG)  

- 핵심 아이디어
  - 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있습니다.
- N과 M의 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리즘을 구현

```python
import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

n,m,c=map(int,input().split())

graph=[[]for _ in range(n+1)]

distance=[INF]*(n+1)

for _ in range(m):
  a,b,x=map(int,input().split())
  graph[a].append((b,x))

def dijkstra(c):
  q=[]
  heapq.heappush(q,(0,c))
  distance[c]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost < distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(c)

# 도달할 수 있는 노드의 개수
count=0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance=0
for d in distance:
  # 도달할 수 있는 노드인 경우
  if d!=1e9:
    count+=1
    max_distance=max(max_distance,d)

# 시작 노드는 제외해야 하므로 count-1 을 출력
print(count-1,max_distance)
```

![미래도시](https://user-images.githubusercontent.com/47052106/105701073-1be44f80-5f4d-11eb-82ec-ad54ccc759fc.JPG)
om/47052106/105698100-c443e500-5f48-11eb-82bd-7a10a85da271.JPG)

- N의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 이용해도 효율적으로 해결
- 플로이드 워셜 알고리즘을 수행한 뒤에 1번 노드에서 x까지의 최단 거리 + x에서 k까지의 최단거리를 계산하여 출력

```python
INF = int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  c,d=map(int,input().split())
  graph[c][d]=1
  graph[d][c]=1

x,k=map(int,input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
      
distance = graph[1][k]+graph[k][x]

if distance >=INF:
  print("-1")
else:
  print(distance)
```
