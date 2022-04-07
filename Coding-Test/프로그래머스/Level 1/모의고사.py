def solution(answers):
    answer=[]
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    for i,num in enumerate(answers):
        if num==one[i%len(one)]:
            score[0]+=1
        if num==two[i%len(two)]:
            score[1]+=1
        if num==three[i%len(three)]:
            score[2]+=1
    m=max(score)
    print(m)
    for i, num in enumerate(score):
        if num==m:
            answer.append(i+1)
    '''answer1 = [] 
    answer2=[]
    answer3=[]
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            answer1.append(answers[i])
        if answers[i]==two[i%8]:
            answer2.append(answers[i])
        if answers[i]==three[i%10]:
            answer3.append(answers[i])
    if len(answer1)>len(answer2)and len(answer1)>len(answer3):
        answer.append(1)
    elif len(answer2)>len(answer1)and len(answer2)>len(answer3):
        answer.append(2)
    elif len(answer3)>len(answer1)and len(answer3)>len(answer2):
        answer.append(3)
    elif len(answer1)==len(answer2) and len(answer2)!=len(answer3):
        answer.append(1)
        answer.append(2)
    elif len(answer2)==len(answer3) and len(answer1)!=len(answer3):
        answer.append(2)
        answer.append(3)
    elif len(answer1)==len(answer3) and len(answer2)!=len(answer3):
        answer.append(1)
        answer.append(3)
    elif len(answer1)==len(answer2) and len(answer2)==len(answer3):
        answer.append(1)
        answer.append(2)
        answer.append(3)'''
    return answer
