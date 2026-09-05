
num=0
max_val=200**8
def solution(n, wires):
    global num
    global max_val
    if num==0:
        graph=[[] for _ in range(n+1)]
        for elem in wires:
            graph[elem[0]].append(elem[1])
            graph[elem[1]].append(elem[0])
    num+=1
    
    for cut_a,cut_b in wires:
        visited=[]
        num_a=1
        visited.append(cut_a)
        visited.append(cut_b)
        
        def dfs(node):
            nonlocal num_a
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.append(next_node)
                    num_a+=1
                    dfs(next_node)
        dfs(cut_a)
        
        num_b=n-num_a
        max_val=min(max_val,abs(num_a-num_b))
    return max_val
        
        

