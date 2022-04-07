import itertools

def solution(orders, course):
    answer = []
    for size in course:
        combi=[]
        combi_dict=dict()
        for order in orders:
            combi.extend(list(itertools.combinations(sorted(order),size)))
            
        for temp in combi:
            order_str=''.join(temp)
            combi_dict[order_str]=combi_dict.get(order_str,0)+1
        #print(combi_dict)
        answer.extend([k for k,v in combi_dict.items() if max(combi_dict.values())==v and v>1] )
        #print(type(combi_dict.values))                                      
            
    return sorted(answer)
