arr = [list(map(int,input().split()))for _ in range(7)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        #print("hi")
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and arr[xx][yy]==0:
                #print(xx,yy)
                arr[xx][yy]=1
                DFS(xx,yy)
                arr[xx][yy]=0

cnt=0
arr[0][0]=1
DFS(0,0)
print(cnt)
