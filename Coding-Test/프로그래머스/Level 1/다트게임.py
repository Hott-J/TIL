def solution(dartResult):
    answer = []
    dartlist=list(dartResult)
    d=[]
    for i in range(len(dartlist)):
        if dartlist[i]=="1" and dartlist[i+1]=="0":
            d.append("10")
        elif dartlist[i]=="0" and dartlist[i-1]=="1":
            continue
        else:
            d.append(dartlist[i])
    print(d)
    for i in range(len(d)):
        if d[i]=='S':
            answer.append(int(d[i-1])**1)
        elif d[i]=='D':
            answer.append(int(d[i-1])**2)
        elif d[i]=='T':
            answer.append(int(d[i-1])**3)
        if d[i]=='*':
            if len(answer)>=2:
                answer[-1]=2*answer[-1]
                answer[-2]=2*answer[-2]
            else:
                answer[-1]=2*answer[-1]
        elif d[i]=='#':
            answer[-1]=answer[-1]*(-1)
    print(answer)
    return sum(answer)
