def solution(num_list):
    num_list.sort()
    answer=[]
    for elem in num_list[:5]:
        answer.append(elem)
    return answer