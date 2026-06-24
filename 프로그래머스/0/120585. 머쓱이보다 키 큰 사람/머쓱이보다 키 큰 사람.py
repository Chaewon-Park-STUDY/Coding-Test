def solution(array, height):
    num=0
    for elem in array:
        if elem>height:
            num+=1
    answer = num
    return answer