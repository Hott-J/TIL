N,M = map(int,input().split())
a = list(map(int,input().split()))
l=0
r=1
cnt=0
res=a[0]
while True: ## 어려운포인트
    if res<M: ## 이곳 
        if r<N: ## 이곳
            res+=a[r]
            r+=1
        else: ## 이곳
            break
    elif res==M:
        res-=a[l]
        l+=1
        cnt+=1
    else:
        res-=a[l]
        l+=1
        
print(cnt)
