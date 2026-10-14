def solution(n, infection, edges, k):
    is_infected=set()
    is_infected.add(infection)
    store={}
    store[1]=[]
    store[2]=[]
    store[3]=[]
    
    num=0
    for [x,y,z] in edges:
        store[z].append((x,y))
    arr=[]
    
    def check(pipe):
        nonlocal num
        def repeat(node, pipe_type):
            for x, y in store[pipe_type]:
                if x == node and y not in is_infected:
                    is_infected.add(y)
                    repeat(y, pipe_type)

                elif y == node and x not in is_infected:
                    is_infected.add(x)
                    repeat(x, pipe_type)
        for elem in pipe:
            for node in list(is_infected):
                repeat(node,elem)
     
        num=max(num,len(is_infected)) 
        is_infected.clear()
        is_infected.add(infection)
        
        
    def dfs():
        if len(arr)==k:
            return check(arr)
        for i in range(1,4):
            arr.append(i)
            dfs()
            arr.pop()
    dfs()
    
    return num