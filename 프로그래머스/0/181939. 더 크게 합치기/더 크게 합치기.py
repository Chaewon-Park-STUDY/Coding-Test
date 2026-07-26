def solution(a, b):
    answer1 = str(a)+str(b)
    answer2= str(b)+str(a)
    max_value= max(int(answer1),int(answer2))
    return max_value