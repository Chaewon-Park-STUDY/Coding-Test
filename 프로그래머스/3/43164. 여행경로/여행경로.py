def solution(tickets):
    graph={}
    for elem in tickets:
        if elem[0] not in graph:
            graph[elem[0]]=[]
        graph.get(elem[0]).append(elem[1])
    for key in graph:
        graph.get(key).sort(reverse=True)
    store=[]
    
    start="ICN"
    def dfs(node):
        while len(graph.get(node,[]))>0:
            next_node=graph.get(node).pop()
            dfs(next_node)
        store.append(node)
    dfs(start)
 
    return store[::-1]
            
        
        
