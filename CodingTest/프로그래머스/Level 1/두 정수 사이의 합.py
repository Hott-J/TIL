def solution(a, b):
    answer = 0
    if a!=b and a<b:
        answer=((a+b)/2)*(b-a+1)
    elif a!=b and a>b:
        answer=((a+b)/2*(a-b+1))
    else:
        answer=a
    return answer
