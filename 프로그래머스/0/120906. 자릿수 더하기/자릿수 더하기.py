
def solution(n):
    if n<10:
        return n

    
    return solution(n//10)+n%10
    
