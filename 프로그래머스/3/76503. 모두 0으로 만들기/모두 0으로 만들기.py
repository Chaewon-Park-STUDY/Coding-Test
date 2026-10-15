def solution(a, edges):
    store={}
    for i in range(len(a)):
        store[i]=[]
    for elem in edges:
        [x,y]=elem
        store[x].append(y)
        store[y].append(x)
        
    num_count=0
    parent={}
    
    if sum(a)!=0:
        num_count=-1
        return num_count
         
    stack=[(0,-1)]
    order=[]
    while stack:
            current,par=stack.pop()
            order.append(current)
            parent[current]=par
            
            for next_node in store[current]:
                if next_node==par:
                    continue
                stack.append((next_node,current))
                    
              
    order.reverse()
    for i in range(len(order)-1):
        num_count+=abs(a[order[i]])
        a[parent[order[i]]]+=a[order[i]]


    return num_count