def solution(my_string):
    answer = ''
    vowel= ["a", "e", "i","o","u"]
    arr=list(map(str, list(my_string)))
    for elem in arr:
        if elem not in vowel:
            answer+=elem
    return answer