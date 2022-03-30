a=[]
cnt=0

for _ in range(7):
    temp = list(map(int,input().split()))
    a.append(temp)

for i in range(7):
    for j in range(3):
        res1=[]
        res2=[]
        for k in range(5):
            res1.append(a[i][k+j])
            res2.append(a[k+j][i])
        if res1==res1[::-1] or res2==res2[::-1]:
            cnt+=1
            print(res1)
            print(res2)

print(cnt)