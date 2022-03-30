def solution(N, stages):
    f={}
    
    answer=[]
    s=sorted(stages)
    for i in range(1,N+1):
        if i in s:
            f[i]=s.count(i)/len(s)
            while i in s:
                s.remove(i)
        else:
            f[i]=0
    
    sf=sorted(f.items(),reverse=True,key=lambda x:x[1])
    print(sf)
    for i in sf:
        print(i)
        answer.append(i[0])
    return answer
