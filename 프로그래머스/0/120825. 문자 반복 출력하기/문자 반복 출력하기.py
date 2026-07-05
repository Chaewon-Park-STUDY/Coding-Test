def solution(my_string, n):
    answer = ''
    for elem in my_string:
        answer+=(elem*n)
    return answer