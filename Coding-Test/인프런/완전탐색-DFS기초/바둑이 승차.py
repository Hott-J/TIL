def DFS(len, sum,tsum):
    global temp
    #global total 
    if sum+(total-tsum)<temp:  # 앞으로 더해질것들을 다 더한다고 하더라도 temp보다 작으면 볼필요도 없다.
        return
    if sum>c:
        return
    if len==n:
        if sum>temp:
            temp=sum   
    else:
        DFS(len+1,sum+baduk[len],tsum+baduk[len]) # tsum+baduk[len]은 판단을 한 무게. 이걸 이용해서 앞으로 남은 것들을 total에서 빼서 구한다.
        DFS(len+1,sum,tsum+baduk[len])
    
c,n = map(int,input().split())
baduk=[]
for i in range(n):
    baduk.append(int(input()))
temp=-2147000000
total=sum(baduk)
DFS(0,0,0)

print(temp)