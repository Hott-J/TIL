# :book: 다이나믹 프로그래밍

## 다이나믹 프로그래밍

- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
- **이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 합니다.**
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성
- 동적 계획법이라고도 부른다
- 일반적인 프로그래밍 분야에서의 동적이란?
  - *자료구조에서 동적 할당은 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법*
  - 반면에 다이나믹 프로그래밍에서 다이나믹은 **별다른 의미 없이 사용**
- 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용
  - **최적 부분 구조**
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결
  - **중복되는 부분 문제**
    - 동일한 작은 문제를 반복적으로 해결

### 피보나치 수열

- `1,1,2,3,5,8,13,21,34,55,89...`
- 점화식이란 인접한 항들 사이의 관계식을 의미
- 피보나치 수열을 점화식으로 표현하면 다음과 같다
  - An=An-1+An-2, A1-1,A2=1

![피보](https://user-images.githubusercontent.com/47052106/105494636-6de36600-5cfe-11eb-9fba-349ef9d91c61.JPG)

![11](https://user-images.githubusercontent.com/47052106/105494631-6cb23900-5cfe-11eb-9368-dcd6bf11286b.JPG)

```python
# 재귀
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1) + fibo(x-2)
```

![시간복잡](https://user-images.githubusercontent.com/47052106/105494879-c7e42b80-5cfe-11eb-8e98-6f2bcbf7a050.JPG)

![시간](https://user-images.githubusercontent.com/47052106/105495196-36c18480-5cff-11eb-9fd8-ffbbf665574b.JPG)

### 피보나치 디피를 사용하자

![디피](https://user-images.githubusercontent.com/47052106/105495361-6f615e00-5cff-11eb-9af9-4cecce9877af.JPG)

- **메모이제이션**
  - 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나
  - 한번 계산된 결과를 메모리 공간에 메모하는 기법
    - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
    - 값을 기록해 놓는다는 점에서 캐싱이라고도 한다

![탑다운](https://user-images.githubusercontent.com/47052106/105495699-d4b54f00-5cff-11eb-906d-97cb2f7869b2.JPG)

- 탑다운
  - 재귀
- 보텀업
  - 반복문

```python
# 탑다운 디피
# 한번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 디피)

def fibo(x):
  # 종료 조건
  if x ==1 or x==2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x]!=0:
    return d[x]
  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo(x-1)+fibo(x-2)
  return d[x]
  
# 보텀업 방식

d = [0] * 100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]
```

![메모이동작](https://user-images.githubusercontent.com/47052106/105496732-39bd7480-5d01-11eb-81ac-2cc0ae0a1e1f.JPG)

![맴ㅎ아뷴속](https://user-images.githubusercontent.com/47052106/105497009-9caf0b80-5d01-11eb-8fd2-8db0be979635.JPG)

### 다이나믹 프로그래밍 vs 분할 정복

- 다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때  사용
  - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
- 다이나믹 프로그래밍과 분할 정복의 차이점은 **부분 문제의 중복**
  - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복
  - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다

![분할](https://user-images.githubusercontent.com/47052106/105497355-10511880-5d02-11eb-97d3-c26875b021c4.JPG)

![접근](https://user-images.githubusercontent.com/47052106/105497466-3971a900-5d02-11eb-8051-93bb8022788f.JPG)

## 문제

### 개미전사

![개미전사](https://user-images.githubusercontent.com/47052106/105513908-3da7c180-5d16-11eb-8352-d30f1e52ef51.JPG)

![문제](https://user-images.githubusercontent.com/47052106/105513911-3f718500-5d16-11eb-8402-4ceba9613492.JPG)

![조건](https://user-images.githubusercontent.com/47052106/105513912-400a1b80-5d16-11eb-83b4-d760b010136e.JPG)

- 풀이

![111](https://user-images.githubusercontent.com/47052106/105533131-13163280-5d2f-11eb-8ec7-b2ddb6281ea6.JPG)

![222](https://user-images.githubusercontent.com/47052106/105533139-14475f80-5d2f-11eb-8093-1f352a0ebda6.JPG)

![33](https://user-images.githubusercontent.com/47052106/105533142-14dff600-5d2f-11eb-8efc-0f09d9e3e9c9.JPG)

![44](https://user-images.githubusercontent.com/47052106/105533144-14dff600-5d2f-11eb-8ba2-f1af624dd689.JPG)

```python
n=int(input())
array=list(map(int,input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] *100

# 보텀업
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
  d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
```

### 1로 만들기

![1로](https://user-images.githubusercontent.com/47052106/105536494-cc770700-5d33-11eb-9f9b-62c73d185636.JPG)

![111](https://user-images.githubusercontent.com/47052106/105537105-c170a680-5d34-11eb-9b60-671a48e6f17f.JPG)

![222](https://user-images.githubusercontent.com/47052106/105537107-c2a1d380-5d34-11eb-8dc4-b4f528e02960.JPG)

```python
n=int(input())

d = [0] * 30001

# 보텀업

for i in range(2,n+1):
  d[i]=1+d[i-1]
  if i%5==0:
    d[i]=min(d[i],d[i//5]+1)
  if i%3==0:
    d[i]=min(d[i],d[i//3]+1)
  if i%2==0:
    d[i]=min(d[i],d[i//2]+1)
print(d[n])
```

### 효율적인 화폐 구성

![효](https://user-images.githubusercontent.com/47052106/105540473-989ee000-5d39-11eb-9ee3-4cb00ebc24b8.JPG)

![조](https://user-images.githubusercontent.com/47052106/105540638-de5ba880-5d39-11eb-8fee-a2b486d22a38.JPG)

![11](https://user-images.githubusercontent.com/47052106/105540643-df8cd580-5d39-11eb-8ca3-8de25fd020bf.JPG)

![2](https://user-images.githubusercontent.com/47052106/105540981-7063b100-5d3a-11eb-8920-4d97c9990271.JPG)

![3](https://user-images.githubusercontent.com/47052106/105540984-70fc4780-5d3a-11eb-8c5d-585ededd49ba.JPG)

![4](https://user-images.githubusercontent.com/47052106/105540986-7194de00-5d3a-11eb-96b0-9beb13cb1d7a.JPG)

![5](https://user-images.githubusercontent.com/47052106/105540989-722d7480-5d3a-11eb-82c5-d6e1139606ae.JPG)

```python
n,m=map(int,input().split())

array=[]
for i in range(n):
  array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[10001]*(m+1)

# 보텀업
d[0]=0
for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]]!=10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])
```

### 금광

![금광](https://user-images.githubusercontent.com/47052106/105543304-fd0f6e80-5d3c-11eb-8674-f1c4ada98f1d.JPG)

![조건](https://user-images.githubusercontent.com/47052106/105547442-d7d12f00-5d41-11eb-9da3-efc4db77740b.JPG)

![1](https://user-images.githubusercontent.com/47052106/105547445-d869c580-5d41-11eb-8907-0388dd2b16d1.JPG)

![2](https://user-images.githubusercontent.com/47052106/105547490-ea4b6880-5d41-11eb-97e3-19b3578e20da.JPG)

```python
for tc in range(int(input())):
  n,m=list(map(int,input().split()))
  array=list(map(int,input().split()))

  dp=[]
  index=0
  for i in range(n):
    dp.append(array[index:index+m])
    index+=m

  for j in range(1,m):
    for i in range(n):
      if i==0:
        dp[i][j]=max(dp[i][j-1]+dp[i][j],dp[i][j]+dp[i+1][j-1])
      elif i==n-1:
        dp[i][j]=max(dp[i][j]+dp[i-1][j-1],dp[i][j]+dp[i][j-1])
      else:
        dp[i][j]=max(dp[i][j]+dp[i-1][j-1],dp[i][j-1]+dp[i][j],dp[i][j]+dp[i+1][j-1])

  res=0
  for i in range(n):
    res=max(res,dp[i][m-1])
  print(res)
  ```

### 병사 배치하기

![병사](https://user-images.githubusercontent.com/47052106/105548111-9725e580-5d42-11eb-8a49-b81878f7f2a5.JPG)

![병'](https://user-images.githubusercontent.com/47052106/105548116-98571280-5d42-11eb-8a92-9f1db044211c.JPG)

![조건](https://user-images.githubusercontent.com/47052106/105548118-98571280-5d42-11eb-94e4-3d43ba355062.JPG)

![11](https://user-images.githubusercontent.com/47052106/105551644-47e1b400-5d46-11eb-98fb-9b9ee30adf1c.JPG)

![22](https://user-images.githubusercontent.com/47052106/105551649-4912e100-5d46-11eb-97bc-cc59b9a43120.JPG)

![33](https://user-images.githubusercontent.com/47052106/105551654-4912e100-5d46-11eb-8630-60c07ffdfd1a.JPG)

![44](https://user-images.githubusercontent.com/47052106/105551657-49ab7780-5d46-11eb-8159-b8cabee4a1e3.JPG)

```python
n=int(input())
array=list(map(int,input().split()))
# 순서를 뒤집어 최장 증가 부분 수열 문제로 변환
array.reverse()

dp=[1]*n

# LIS 알고리즘 수행
for i in range(1,n):
  for j in range(0,i):
    if array[j]<array[i]:
      dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
```
