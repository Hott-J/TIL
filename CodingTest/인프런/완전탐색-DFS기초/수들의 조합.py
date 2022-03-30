def DFS(v,s,sum):
    global cnt
    if v==k:
        #print(sum)
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s,n):
            DFS(v+1,i+1,sum+arr[i])

n,k=map(int,input().split())
arr=[]
cnt=0
arr=list(map(int,input().split()))
m=int(input())
DFS(0,0,0)
print(cnt)