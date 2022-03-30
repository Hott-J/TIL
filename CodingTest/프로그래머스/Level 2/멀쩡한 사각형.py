from math import gcd

def solution(w,h):
    answer = w*h-((w//gcd(w,h)+h//gcd(w,h)-1)*gcd(w,h))
    return answer
