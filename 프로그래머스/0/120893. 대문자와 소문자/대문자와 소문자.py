def solution(my_string):
    answer = ''
    for elem in my_string:
        if elem.isupper():
            elem=elem.lower()
            answer+=elem
        else:
            elem=elem.upper()
            answer+=elem
    return answer