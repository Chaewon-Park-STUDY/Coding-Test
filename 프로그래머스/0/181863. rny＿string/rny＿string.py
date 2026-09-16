def solution(rny_string):
    answer=''
    for elem in rny_string:
        if elem=="m":
            answer+="rn"
        else:
            answer+=elem
    return answer
    