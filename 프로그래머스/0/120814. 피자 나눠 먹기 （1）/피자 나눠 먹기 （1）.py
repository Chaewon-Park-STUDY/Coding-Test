def solution(n):
    find=n%7
    if 1<=find:
        answer =n//7+1
    else:
        answer=n//7
    return answer