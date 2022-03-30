# :book: 이진 탐색 알고리즘

## 이진 탐색 알고리즘

- 순차 탐색 : 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인**하는 방법
- 이진 탐색 : *정렬되어 있는 리스트에서* **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
- 예시 (이미 정렬된 10개의 데이터 중에서 값이 4인 원소를 찾는다)
  - `0 2 4 6 8 10 12 14 16 18`
  - 시작점: 0, 끝점: 9, 중간점: 4 (소수점 이하 제거)
  - 중간점은 8이므로 4보다 크다. 즉, 오른쪽은 볼 필요없다.
  - 시작점: 0, 끝점: 3, 중간점: 1
  - 중간점은 2이므로 4보다 작다. 즉, 왼쪽은 볼 필요없다.
  - 시작점: 2, 끝점: 3, 중간점: 2
  - 중간점은 4이다. 찾았다.
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례
- 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다.
  - 2단계를 거치면 8개가량의 데이터만 남는다.
  - 3단계를 거치면 4개가량의 데이터만 남는다.
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장

```python
# 재귀

def binary_search(array, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  # 찾은 경우 중간점 인덱스 반환
  if array[mid] ==  target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  elif array[mid]<target:
   return binary_search(array,target,mid+1,end)
   
# 반복문

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    # 맞은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid -1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start=mid+1
  return None
```

### 파이썬 이진 탐색 라이브러리

- bisect_left(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환 (c++: lower_bound)
- bisect_right(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환 (c++: upper_bound)

![bisect](https://user-images.githubusercontent.com/47052106/105399507-10500a80-5c67-11eb-986f-3856e891f5b4.JPG)

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))
```

### 파라메트릭 서치
- 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
  - 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결

## 문제

### 떡볶이 떡 만들기

![문제](https://user-images.githubusercontent.com/47052106/105413431-6c238f00-5c79-11eb-8114-9e631952885d.JPG)

![조건](https://user-images.githubusercontent.com/47052106/105413428-6b8af880-5c79-11eb-9c67-b7617523f04e.JPG)

![아이디어](https://user-images.githubusercontent.com/47052106/105417712-59ac5400-5c7f-11eb-9bd8-3860f850c4f3.JPG)

![222](https://user-images.githubusercontent.com/47052106/105417715-5a44ea80-5c7f-11eb-812b-481383993fbd.JPG)

![333](https://user-images.githubusercontent.com/47052106/105417717-5add8100-5c7f-11eb-83e2-1f73cd1e6aff.JPG)

![444](https://user-images.githubusercontent.com/47052106/105417719-5add8100-5c7f-11eb-8696-e0e9badebdde.JPG)

```python
# 내 코드
from bisect import bisect_left, bisect_right

n,m=list(map(int,input().split()))
dduck = list(map(int,input().split()))
dduck.sort()
l=0
maxlong=0
for i in range(min(dduck),max(dduck)+1):
  sum=0
  right_index = bisect_right(dduck, i)
  for j in range(right_index,len(dduck)):
    sum+=dduck[j]-i
  if sum==m:
    l=i
    maxlong=max(i,l)
print(maxlong)

# 모범 답안
n,m=list(map(int,input().split()))
array = list(map(int,input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start =0
end = max(array)

# 이진 탐색 수행 (반복적)
result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    # 잘랐을 때의 떡의 양 계산
    if x>mid:
      total+=x-mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total<m:
    end = mid -1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    start = mid +1
```

![문제2](https://user-images.githubusercontent.com/47052106/105418357-55346b00-5c80-11eb-9503-c57bddc6f888.JPG)

![조건22](https://user-images.githubusercontent.com/47052106/105418356-54033e00-5c80-11eb-8bf2-899aafe18a74.JPG)

![1111](https://user-images.githubusercontent.com/47052106/105418859-25d22e00-5c81-11eb-9078-dbacb34020ea.JPG)

```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
if x not in a:
  print("-1")
else:
  print(count_by_range(a,x,x))
```




