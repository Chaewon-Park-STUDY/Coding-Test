def solution(myString, pat):
    letter=myString.upper()
    findit=pat.upper()
    if findit in letter:
        answer=1
    else:
        answer=0
    return answer