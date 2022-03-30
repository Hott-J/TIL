def DFS(v,sum):
    global temp
    if v>temp:
        return
    if sum>m:
        return
    if sum==m:
        if v<temp:
            temp=v
    else:
        for i in range(n):
            DFS(v+1,sum+money[i])

n = int(input())
money = list(map(int,input().split()))
m = int(input())
temp=2147000000
money.sort(reverse=True)
#print(money)

DFS(0,0)
print(temp)