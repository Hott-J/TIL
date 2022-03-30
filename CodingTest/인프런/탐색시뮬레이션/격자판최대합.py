n = int(input())
a=[]
for _ in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

raw = col = sli1 = sli2 = tem = 0


for i in range(n):
    raw = max(raw,sum(a[i]))

for j in range(n):
    tem = 0
    for z in range(n):
        tem+=a[z][j]
    col = max(col,tem)

for s in range(n):
    sli1 += a[s][s]
    sli2 += a[n-s-1][s]

sli = max(sli1,sli2)

ans = max(raw,col)
ans = max(ans,sli)
print(ans)
