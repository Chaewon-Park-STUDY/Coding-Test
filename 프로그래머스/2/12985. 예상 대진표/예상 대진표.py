def solution(n,a,b):
    num=0
    
    def check(a,b):
        if a%2==0:
            if a//2==(b+1)//2:
                return True
        else:
            if (a+1)//2==b//2:
                return True
        return False
        
        
    def dfs(a,b):
        nonlocal num
        num+=1
        if abs(a-b)==1:
            if check(a,b):
                return
        
        if a%2==0:
            a//=2
        else:
            a=(a+1)//2
        if b%2==0:
            b//=2
        else:
            b=(b+1)//2
            
        dfs(a,b)
    dfs(a,b)
    return num
        
        
    