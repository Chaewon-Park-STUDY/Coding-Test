def solution(n, k):
    arr=[]
    num=0
    
    from math import factorial as fact
    def dfs():
        nonlocal num
            
        if len(arr)==n:
            num+=1
            return 
        
        for i in range(1,n+1):
            if i not in arr:
                if k-num>fact(n-len(arr)-1):
                    num+=fact(n-len(arr)-1)
                    continue
                arr.append(i)
                dfs()
                if num==k:
                    break
                arr.pop()

    dfs()
    return arr
        