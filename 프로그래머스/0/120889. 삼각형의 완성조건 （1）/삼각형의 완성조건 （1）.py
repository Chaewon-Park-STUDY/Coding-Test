def solution(sides):
    answer = 0
    num=0
    for i in range(3):
        if sides[i]==max(sides):
            new=i
    for j in range(3):
        if j!=new:
            num+=sides[j]
            
    if max(sides)<num:
        answer=1
    else:
        answer=2
        
            
    
    return answer