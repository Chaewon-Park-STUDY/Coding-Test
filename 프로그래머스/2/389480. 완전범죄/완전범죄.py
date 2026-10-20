def solution(info, n, m):
    k=len(info)
    min_A=10**8
    
    visited=set()
    def dfs(idx,num_A,num_B):
        nonlocal min_A
        if idx==k:
            min_A=min(min_A,num_A)
            return
        state = (idx, num_A, num_B)
        if state in visited:
            return
        else:
            visited.add(state)
        if num_A + info[idx][0]<n:
            dfs(idx + 1, num_A + info[idx][0], num_B)
        if num_B+info[idx][1]<m:
            dfs(idx + 1, num_A, num_B + info[idx][1])
        
        
    dfs(0,0,0)
    if min_A==10**8:
        return -1
    else:
        return min_A
                    
                