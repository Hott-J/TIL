a=[]

for _ in range(9):
    temp = list(map(int,input().split()))
    a.append(temp)

def check(a):
    for i in range(9):
        chk1=[0]*10
        chk2=[0]*10
        for j in range(9):
            chk1[a[i][j]]=1
            chk2[a[j][i]]=1
        if sum(chk1)!=9 or sum(chk2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            chk3=[0]*10
            for k in range(3):
                for s in range(3):
                    chk3[a[i*3+k][j*3+s]]=1
            if sum(chk3)!=9:
                return False
    return True

if check(a):
    print("YES")
else:
    print("NO")

