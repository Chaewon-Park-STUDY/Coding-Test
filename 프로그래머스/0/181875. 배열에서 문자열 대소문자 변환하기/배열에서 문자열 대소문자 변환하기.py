def solution(strArr):
    answer=[]
    for i in range(len(strArr)):
        if i%2==0:
            letter=strArr[i].lower()
        else:
            letter=strArr[i].upper()
        answer.append(letter)
    
    return answer