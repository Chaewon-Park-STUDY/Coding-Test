def solution(num_list):
    mul_total=1
    sum_total=0
    for elem in num_list:
        mul_total*=elem
        sum_total+=elem
    if mul_total<sum_total**2:
        answer=1
    else:
        answer=0
    return answer