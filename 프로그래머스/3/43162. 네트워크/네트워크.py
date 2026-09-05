num=0

def solution(n, computers):
    global num
    if num==0:
        graph=[[] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if i!=j and computers[i][j]==1:
                    graph[j+1].append(i+1)
    num+=1
    visited=[]
    group_num=0
    
    for i in range(1,n+1):
        if i not in visited:
            group_num+=1
            visited.append(i)
            def dfs(node):
                for next_node in graph[node]:
                    if next_node not in visited:
                        visited.append(next_node)
                        dfs(next_node)

            dfs(i)
        
    return group_num
                