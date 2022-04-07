n = int(input())
st =[]
en = []
peo= []

def DFS(L,sum):
    global res
    if L > n-1:
        res = max(res,sum)
        return
    else:
        DFS(L+1,sum)
        DFS(L+2,sum+peo[L])
for i in range(n):
    s,e,p = map(int,input().split())
    st.append(s)
    en.append(e)
    peo.append(p)

res = 0
DFS(0,0)
print(res)