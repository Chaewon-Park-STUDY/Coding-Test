def solution(n, k):
    drink=0
    if n<10:
        drink=2000*k
    else:
        drink= 2000*(k-(n//10))
    answer = 12000*n+drink
    return answer