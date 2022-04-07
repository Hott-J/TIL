n=int(input())
a=dict()
for i in range(n):
    word=input()
    a[word]=1

for i in range(n-1):
    word=input()
    a[word]=0

for key,val in a.items():
    if val==1:
        print(key)
        break