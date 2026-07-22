def solution(str1, str2):
    answer = 0 
    for i in range(len(str1)-len(str2)+1):
        if all(str1[i+j]==str2[j] for j in range(len(str2))):
            answer=1
            break
        else:
            continue
    if answer==0:
        answer=2
    return answer