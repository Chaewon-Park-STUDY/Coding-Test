def solution(user_id, banned_id):
    num=0
    n=len(banned_id)
    arr=[]
    store=set()
    
    def check(arr):
        nonlocal num
        for i in range(n):
            if len(arr[i])!=len(banned_id[i]):
                return False
            else:
                for j in range(len(banned_id[i])):
                    if banned_id[i][j]!=arr[i][j] and banned_id[i][j]!="*":
                        return False
        temp=tuple(sorted(arr))
        if temp not in store:
            store.add(temp)
            num+=1
                                   
    def dfs(user_id, banned_id):
        if len(arr)==n:
            return check(arr)
        
        for i in range(len(user_id)):
            if user_id[i] not in arr:
                arr.append(user_id[i])
                dfs(user_id,banned_id)
                arr.pop()

    dfs(user_id,banned_id)
    return num
    
    
        
        
        
                        
                
            
            
            
            
                