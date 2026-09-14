def solution(arr, k):
    answer=[]
    if k%2!=0:
        for elem in arr:
            elem*=k
            answer.append(elem)
    else:
        for elem in arr:
            elem+=k
            answer.append(elem)
    return answer
            
        