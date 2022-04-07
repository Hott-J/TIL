s = input()
res=0
for i in s:
    if i.isdecimal():
        res=res*10+int(i) # 문자열을 정수로 바꾸는 방법
print(res)
cnt=0
for j in range(1,res+1):
    if res%j==0:
        cnt+=1
print(cnt)