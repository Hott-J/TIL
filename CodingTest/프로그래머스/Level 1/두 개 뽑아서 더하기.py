def solution(numbers):
    answer = []
    temp=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] in answer:
                print("hi")
            else:
                answer.append(numbers[i]+numbers[j])
    answer=sorted(answer)
    return answer
