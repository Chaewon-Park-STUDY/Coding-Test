def solution(k, score):
    a=len(score)
    arr=[]
    answer=[]
    
    for i in range(a):
        def dfs():
            arr.append(score[i])
            arr.sort(reverse=True)
            if len(arr)==k+1:
                arr.pop()
            answer.append(arr[-1])
        dfs()
    return answer
            
                
                
            