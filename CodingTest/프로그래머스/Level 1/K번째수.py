def solution(array, commands):
    answer = []
    arr=[]
    for i in range(len(commands)):
        arr.append(array[commands[i][0]-1:commands[i][1]])
        arr[i].sort()
        answer.append(arr[i][commands[i][2]-1])
    return answer
