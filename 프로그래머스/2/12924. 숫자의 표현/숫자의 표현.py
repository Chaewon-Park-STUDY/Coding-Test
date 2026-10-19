def solution(n):
    num_count=0
    arr=[i for i in range(1,n+1)]
    arr.reverse()
    
    for i in range(1,n+1):
        def dfs(start, num_sum):
            nonlocal num_count
            if num_sum==n:
                num_count+=1
                return
            if num_sum>n:
                return

            num_sum+=start
            dfs(start+1,num_sum)
        dfs(arr.pop(),0)
    
    return num_count