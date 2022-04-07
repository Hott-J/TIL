n = int(input())
st=[]
en=[]
cnt=0

for i in range(n):
    s,e=map(int,input().split())
    st.append(s)
    en.append(e)
a,b=zip(*sorted((zip(en,st))))
#print(b,a)
events = [0]
k = 0

for i in range(1,n):
    if b[i]>=a[k]:
        events.append(i)
        k=i
print(len(events))