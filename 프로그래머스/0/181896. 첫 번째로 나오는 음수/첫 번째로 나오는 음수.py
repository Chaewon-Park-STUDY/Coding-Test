def solution(num_list):
    answer = 0
    is_negative=False
    for elem in num_list:
        if elem<0:
            answer=num_list.index(elem)
            is_negative=True
            break
    if is_negative==False:
        answer=-1
    return answer