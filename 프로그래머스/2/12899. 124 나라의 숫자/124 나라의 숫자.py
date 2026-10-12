def solution(n):

    
    
    def dfs(a):
        if a==0:
            return ""
        parent=(a-1)//3
        
        letter=dfs(parent)
        if (a+3)%3==1:
            result="1"
        elif (a+3)%3==2:
            result="2"
        else:
            result="4"
        
        
        return letter+result
    return dfs(n)
    
