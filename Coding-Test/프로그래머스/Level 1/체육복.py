def solution(n, lost, reserve):
    answer = 0
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for num in set_reserve:
        if num-1 in set_lost:
            set_lost.remove(num-1)
        elif num+1 in set_lost:
            set_lost.remove(num+1)
    return n-len(set_lost)
