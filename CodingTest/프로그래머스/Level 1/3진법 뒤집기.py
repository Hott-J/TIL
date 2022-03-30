NOTATION='0123456789ABCDEF'

def numeral_system(number,base):
    q,r=divmod(number,base)
    n=NOTATION[r]
    return numeral_system(q,base)+n if q else n

def solution(n):
    answer = 0
    ans=0
    answer=numeral_system(n,3)
    answer=answer[::-1]
    for i in range(len(answer)):
        ans+=int(answer[i])*(3**(len(answer)-i-1))
    return ans
