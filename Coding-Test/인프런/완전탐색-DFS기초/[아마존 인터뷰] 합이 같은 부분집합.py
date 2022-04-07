import sys

def DFS(v,sum):
    if sum>s//2:
        return
    if v==n:
        if sum==(s-sum):
            print("YES")
            sys.exit()
    else:
        DFS(v+1,sum+arr[v])
        DFS(v+1,sum)

n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
chk = [0]*(n+1)
DFS(0,0)
print("NO")