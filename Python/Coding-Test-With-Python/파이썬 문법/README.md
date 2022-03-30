## 시간복잡도
- 문제에서 가장 먼저 확인해야 하는 내용은 시간제한이다.
- 시간제한이 1초인 문제를 만났을 때, 일반적인 기준
  - N의 범위가 500 : 시간 복잡도가 O(N^3)인 알고리즘 설계 가능
  - N의 범위가 2,000 : 시간 복잡도가 O(N^2)인 알고리즘 설계 가능
  - N의 범위가 100,000 : 시간 복잡도가 O(NlogN)인 알고리즘 설계 가능
  - N의 범위가 10,000,000 : 시간 복잡도가 O(N)인 알고리즘 설계 가능

## 정수형
- 정수형은 정수를 다루는 자료형이다.
  - 양의 정수, 음의 정수, 0이 포함

```python
# 양의 정수
a=1000 # a라는 변수에 1000이라는 상수값을 넣겠다.
# 음의 정수
b=-7
# 0
c=0
```

## 실수형
- 실수형은 소수점 아래의 데이터를 포함하는 수 자료형이다.
  - 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리됨.
  - 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성.
- 개발 과정에서 실수 값을 제대로 비교하지 못해 원하는 결과를 얻지 못할 수 있다. 
  - round() 함수를 이용하여 반올림한다. round(123.456,2) -> 123.46 (셋째 자리 반올림)

```python
# 소수부가 0일 때 0을 생략
a=5. #5.0
# 정수부가 0일 때 0을 생략
a=-.7 #-0.7
```

## 지수 표현 방식
- 파이썬은 e나 E를 이용한 지수 표현 방식을 이용
  - 1e9 는 10의 9제곱
  - 임의의 큰 수를 표현하기 위해 자주 사용
  - 실수형 데이터로 출력됨
- int(1e9) 처럼 정수로 형변환 가능

## 수 자료형의 연산
- 파이썬에서 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환
- 다양한 로직을 설계할 때 나머지 연산자(%)를 이용
- 파이썬에서 몫을 얻기 위해 몫 연산자(//)를 사용

## 리스트 자료형
- 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
  - C나 자바에서의 배열의 기능 및 연결 리스트와 유사
  - C+++의 벡터와 기능적으로 유사
  - 리스트 대신에 배열 혹은 테이블이라고도 부름
  - 대괄호안에 원소를 넣어 초기화하며, 쉼표로 원소를 구분
- list(), [] 로 비어 있는 리스트를 선언
- 리스트의 원소에 접근할 때는 인덱스 값을 괄호에 넣는다. 인덱스는 0부터 시작

```python
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n=10
a=[0] * n #[0,0,0,0,0,0,0,0,0,0]
```

### 인덱싱과 슬라이싱
- 파이썬의 인덱스 값은 양의 정수와 음의 정수를 모두 사용
  - 음의 정수를 넣으면 원소를 거꾸로 탐색(-1부터 차례대로 작아진다)

```python
a[-1] # 뒤에서 첫번쨰 원소 출력
```
- 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용
  - 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정
```python
print(a[1:4]) # 두 번째 원소부터 네 번째 원소까지 (1~3)
```

### 리스트 컴프리헨션
- 리스트를 초기화하는 방법 중 하나
```python
# 0부터 9까지의 수를 포함하는 리스트
array=[i for i in range(10)] # [0,1,2,3,4,5,6,7,8,9]

# 0부터 19까지의 수 중에서만 홀수만 포함
array=[i for i in range(20) if i%2==1]

# 1부터 9까지의 수들의 제곱 값을 포함
array=[i*i for i in range(1,10)]
```
- 2차원 리스트를 초기화할 때 효과적으로 사용됨
- array=[[0] * m] * n 처럼 코드 작성시 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식
  - 하나의 인덱스 바꾸면 전체가 바뀌어지므로 예기치 못한 오류 발생
  
#### 언더바 사용
- 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바를 자주 사용
```python
for _ in range(5):
  print("Hello World")
```
#### 관련 기타 메서드
- append()
  - 원소 삽입
- sort()
  - 오름차순
- reverse()
- insert()
  - 특정 인덱스에 데이터 추가
- count()
- remove()
  - 여러 개 중 하나만 제거
  - 모두 제거하려면 특정 함수 사용
```python
# 모두 제거
a=[1,2,3,4,5,5,5]
remove_set={3,5} # 집합
result = [i for i in a if i not in remove_set]
```  

## 문자열 자료형

- 큰따옴표나 작은 따옴표로 초기화
- 문자열안에 큰따옴표나 작은 따옴표가 포함되는 경우
  - 전체 문자열이 큰(작은)이면, 내부는 작은(큰) 포함
  - 백슬래시를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있다.
- 문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱 이용
  - 특정 인덱스의 값을 변경할 수는 없다.
  
## 튜플 자료형
- 리스트와 유사하지만 문법적 차이가 있다.
  - 한번 선언된 값을 변경할 수 없다.
  - 튜플은 소괄호를 이용한다.
- 튜플은 리스트에 비해 상대적으로 공간 효율적이다.
  - 더 적은 양의 메모리 사용

### 사용 좋은 경우
- 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
  - 최단 경로 알고리즘에서는 (비용,노드 번호)의 형태로 튜플 자료형을 자주 사용
- 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
- 리스트보다 메모리를 효율적으로 사용해야 할 때

## 사전 자료형
- 사전 자료형은 키와 값의 쌍을 데이터로 가지는 자료형이다.
  - 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비
- 변경 불가능한 자료형을 키로 사용
- 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리
- 키와 값을 별도로 뽑아내기 위한 메서드를 지원
  - keys() , key 객체의 형태로 반환되므로 list로 형변환해서 반환시킬 수 있다.
  - values()

## 집합 자료형
- 중복을 허용하지 않는다
- 순서가 없다
- 리스트 혹은 문자열을 이용해서 초기화할 수 있다
  - set() 함수 이용
- 중괄호안에 각 원소를 콤마 기준으로 구분하여 삽입함으로써 초기화
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리
- 집합 연산으로 합집합, 교집합, 차집합 연사 등이 있다.
```python
data=set([1,2,3])

# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러 개 추가
data.update([5,6])

# 특정한 값을 갖는 원소 삭제
data.remove(3)
```

## 자주 사용되는 표준 입력 방법
- input() 함수는 한 줄의 문자열을 입력 받는 함수
- map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
  - list(map(int,input().split())) # 공백을 기준으로 데이터를 입력받을 때
```python
n=int(input())
data=list(map(int,input().split()))
# 공백을 기준으로 split하면 문자열 형태로 리스트가 반환되므로, int형으로 변경한뒤에 그걸 다시 리스트로
```
- print()는 기본적으로 출력 이후에 줄 바꿈을 수행
  - 줄 바꿈을 원치 않는 경우 'end' 속성을 이용
```python
print(7,end=" ")
print(8,end=" ")
# 7 8
```

### 빠르게 입력 받기
- sys.stdin.readline() 메서드
  - 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용
  
## 조건문
- 프로그램의 흐름을 제어
- 프로그램의 로직을 설정
- 기본 형태는 if ~ elif ~ else 이다.
  elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 된다.
- 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
  
### 비교 연산자
- == , != , > , < , >= , <=
  - 0<x<20 가능

### 논리 연산자
- and , or , not

### 기타 연산자
- in 연산자와 not in 연산자
  - 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능
  - x in 리스트 
  - x not in 문자열

## 반복문
- 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
  - 무한 루프를 유의해야 한다. 반복문을 탈출할 수 있는지 확인

### for문
  - in 뒤에 오는 데이터(리스트,튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
  - 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용
  
### continue 키워드
- 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때

### break 키워드
- 반복문을 즉시 탈출하고자 할 때

## 함수
- 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미
- 불필요한 소스코드의 반복을 줄임
- 파라미터의 변수를 직접 지정할 수 있다.
  - 매개변수의 순서가 달라도 상관이 없다
```python
def add(a,b):
add(b=3,a=7)
```

### 내장 함수
- 파이썬이 기본적으로 제공하는 함수

### 사용자 정의 함수
- 개발자가 직접 정의하여 사용

### global 키워드
- global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
```python
a=10
def func():
  global a
  a+=1
  print(a)
func() # 11
```
- 지역변수가 해당 함수안에서는 전역변수보다 우선한다.

### 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
```python
def op(a,b):
  add=a+b
  sub=a-b
  mul=a*b
  div=a/b
  return add,sub,mul,div
a,b,c,d=op(a,b)
```

### 람다 표현식
- 함수를 간단하게 작성
- print((lambda a,b:a+b)(3,7)) 입력으로 받을 매개변수를 명시하고, 함수를 작성
```python
array=[('홍',50),('이',32),('아',74)]

def my_key(x):
  return x[1]

print(sorted(array,key=my_key)) # my_key 순서로 정렬
print(sorted(array,key=lambda x:x[1])) # 람다 함수로 간편하게 정렬
# [('이'',32),('홍',50),('아',74)]
```
### 여러 개의 리스트에 적용
```python
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result=map(lambda a,b:a+b,list1,list2)
# [7,9,11,13,15]
```

### map 함수
- map(변환 함수, 순회 가능한 데이터)
  - 순회 가능한 데이터의 객체 하나씩 가져와서, 변환 함수 혹은 람다 함수에 적용하여 새로운 iterable 객체를 생성
```python
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
  {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
  {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
  {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
  {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]
 
def conver_to_name(user):
    first, last = user["name"].split()
    return {"first": first, "last": last}

for name in map(conver_to_name, users):
     print(name)

{'first': 'Brett', 'last': 'Holland'}
{'first': 'Madison', 'last': 'Martinez'}
{'first': 'Michael', 'last': 'Jenkins'}
{'first': 'Karen', 'last': 'Rodriguez'}
{'first': 'Amber', 'last': 'Rhodes'}

for mail in map(lambda u: "남" if u["sex"] == "M" else "여", users):
     print(mail)

남
여
남
여
여
```
- map 의 반환값은 map 객체이다. list(), tuple() 과 같은 내장함수로 변환가능하다.

## 실전에서 유용한 표준 라이브러리
- 내장 함수
  - sum()
  - min() , max()
  - eval()
  - sorted()
  - sorted(array, key=lambda x:x[1], reverse=True) : 정렬 기준 두번째 원소 기준으로 오름차순
- itertools
  - 반복되는 형태의 데이터를 처리
  - 순열과 조합 라이브러리가 포함
```python
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data=['a','b','c']
result=list(permutations(data,3) # 모든 순열 구하기
result1=list(combinations(data,2) # 2개를 뽑는 모든 조합 구하기
result2=list(product(data,repeat=2)) # 2개를 뽀는 모든 순열 구하기 (중복 허용)
result3=list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
```
- heapq
  - 우선순위 큐
  - 다익스트라
- bisect
  - 이진 탐색
- collections
  - 덱, 카운터등의 유용한 자료구조 포함
  - Counter는 등장 횟수를 세는 기능을 제공
    - 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려준다.
```python
from collections import Counter

counter=Counter(['r','b','r','g','b','b'])
print(counter['b']) #3
print(dict(counter)) # {'r':2,'b':3,'g':1} # 사전 자료형으로 반환
```
- math
  - 팩토리얼, 제곱근, 최대공약수, 삼각함수
```python
import math

math.gcd(21,14) # 최대 공약수
``` 
