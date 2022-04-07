import itertools as it
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=int(input())
cnt=0
for x in it.combinations(a,k): # a라는 리스트에서 k를 뽑아서 조합을 만들어준다.
    if sum(x)%m==0:
        cnt+=1
print(cnt)