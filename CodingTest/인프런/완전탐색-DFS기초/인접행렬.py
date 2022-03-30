n,m=map(int,input().split())

arr=[[0]*n for _ in range(n)]

for i in range(m):
    x,y,k=map(int,input().split())
    arr[x-1][y-1]=k

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()