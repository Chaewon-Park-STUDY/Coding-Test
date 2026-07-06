def solution(my_string, letter):  
    answer = ''
    for elem in my_string:
        if elem==letter:
            pass
        else:
            answer+=elem
    return answer