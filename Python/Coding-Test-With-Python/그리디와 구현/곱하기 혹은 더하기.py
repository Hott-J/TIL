string = input()
sum = int(string[0])

for i in range(1,len(string)):
    if int(string[i])<=1 or sum<=1:
        sum+=int(string[i])
    else:
        sum*=int(string[i])

print(sum)