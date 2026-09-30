def solution(my_string, index_list):
    answer = ''
    for elem in index_list:
        answer+=my_string[elem]
    return answer