def solution(num_list):
    num_even=0
    num_odd=0
    for elem in num_list:
        if elem%2==0:
            num_even+=1
        else:
            num_odd+=1
    answer = []
    answer.append(num_even)
    answer.append(num_odd)
    return answer