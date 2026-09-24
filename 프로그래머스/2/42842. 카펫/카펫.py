def solution(brown, yellow):
    answer=[]
    for i in range(1,yellow+1):
        if yellow%i==0 and i+(yellow//i)==(brown-4)//2:
            n=i
            m=yellow//i
            break
    answer.append(m+2)
    answer.append(n+2)
    return answer