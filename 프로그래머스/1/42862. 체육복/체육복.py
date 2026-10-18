def solution(n, lost, reserve):

    candid=set()
    arr=[]
    
    new_lost=lost.copy()
    again=new_lost.copy()
    for elem in again:
        if elem in reserve:
            reserve.remove(elem)
            new_lost.remove(elem)

    default=n-len(new_lost)
    
    def dfs(start):
        nonlocal default
        if start==len(new_lost):
            default=max(default,n-len(new_lost)+len(arr))
            return 
        
        for i in range(len(reserve)):
            if abs(new_lost[start]-reserve[i])==1 and reserve[i] not in candid:
                candid.add(reserve[i])
                arr.append((new_lost[start],reserve[i]))
                dfs(start+1)
                arr.pop()
                candid.remove(reserve[i])
        dfs(start+1) 
        
    dfs(0)
    return default
                    