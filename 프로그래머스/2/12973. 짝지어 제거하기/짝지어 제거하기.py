def solution(s):
    answer=0
    
    def dfs(letter):
        nonlocal answer
        k=len(letter)
        
        stack=[]
        for i in range(k):
            if stack:
                if stack[-1]==letter[i]:
                    stack.pop()
                else:
                    stack.append(letter[i])
            else:
                stack.append(letter[i]) 
        if not stack:
            answer=1
                   
    dfs(s)
    return answer
    