def solution(my_string, is_suffix):
    answer = 0
    arr=[]
    for i in range(len(my_string)):
        letter=''
        for elem in my_string[i:]:
            letter+=elem
        arr.append(letter)
    if is_suffix in arr:
        answer=1
    return answer