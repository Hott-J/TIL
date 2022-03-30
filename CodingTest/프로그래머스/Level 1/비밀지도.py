def solution(n, arr1, arr2):
    answer = []
    num1=""
    num2=""
    for i in range(n):
        ans=""
        num1=""
        num2=""
        for j in range(n):
            if arr1[i]>=2**(n-(j+1)) or arr2[i]>=2**(n-(j+1)):
                #num1+="1"
                ans+="#"
                arr1[i]=arr1[i]%(2**(n-(j+1)))
                arr2[i]=arr2[i]%(2**(n-(j+1)))
            elif arr2[i]<2**(n-(j+1)) and arr2[i]<2**(n-(j+1)):
                num1+="0"
                ans+=" "
        answer.append(ans)
    print(answer)
    return answer
