
                
def solution(begin, target, words):
    graph={}
    n=len(words)
    words.insert(0,begin)
    for elem in words:
        graph[elem]=[]
        store=[]
        for _ in elem:
            store.append(_)
        for i in range(n+1):
            def check(current,i):
                arr=[]
                num=0
                for _ in words[i]:
                    arr.append(_)
                for k in range(len(store)):
                    if store[k]==arr[k]:
                        num+=1
                if num==len(store)-1:
                    return True
            if check(elem,i):
                graph.get(elem).append(words[i])

    word=begin
    visited=[begin]
    
    if target not in words:
        return 0
    candid=[]
    def dfs(start,count):
        if start==target:
            candid.append(count)
            return 
        for next_node in graph[start]:
            if next_node not in visited:
                visited.append(next_node)
                result= dfs(next_node,count+1)
                visited.pop()
                    
    dfs(word,0)
    return min(candid)
            
            
    