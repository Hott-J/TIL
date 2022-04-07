import collections

def solution(p,c):
    answer = ''
    result=collections.Counter(p)-collections.Counter(c)
    return list(result)[0]
