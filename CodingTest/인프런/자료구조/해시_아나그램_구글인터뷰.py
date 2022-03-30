word1=input()
word2=input()
a1=dict()
a2=dict()

for i in word1:
    a1[i]=a1.get(i,0)+1
for i in word2:
    a2[i]=a2.get(i,0)+1

for k in a1.keys():
    if k in a2.keys():
        if a1[k]!=a2[k]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")