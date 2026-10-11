def solution(num):
    num_count=0

    while num:
        if num==1:
            break
        num_count+=1
        if num%2==0:
            num//=2
        else:
            num*=3
            num+=1
    if num_count>500:
        return -1
    else:
        return num_count