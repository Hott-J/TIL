def solution(d, budget):
    answer = 0
    d.sort()
    sum=0
    for num in d:
        sum+=num
        if(sum>budget):
            break
        answer+=1
    return answer
