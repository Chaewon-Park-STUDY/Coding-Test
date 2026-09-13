def solution(my_string, alp):
    answer = ''
    for elem in my_string:
        if elem==alp:
            a=elem.upper()
            answer+=a
        else:
            answer+=elem
    return answer