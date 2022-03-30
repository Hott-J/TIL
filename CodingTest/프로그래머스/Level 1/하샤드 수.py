def solution(x):
    answer = True
    num=0
    xnum=x
    while xnum!=0:
        num+=xnum%10
        xnum=xnum//10
    print(num)
    if x%num==0:
        answer=True
    else:
        answer=False
    return answer
