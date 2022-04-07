def solution(n):
    answer=0
    li=[True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if li[i]==True:
            for j in range(i+i,n+1,i):
                li[j]=False
    for z in range(2,n+1):
        if li[z]==True:
            answer+=1
    return answer
