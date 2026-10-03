def solution(relation):
    a=len(relation)
    b=len(relation[0])
    
    arr = [] 
    final=[]
     
    def check(arr):
        store=set()
        for row in range(a):
            temp=[]
            for _ in range(len(relation[row])):
                if _ in arr:
                    temp.append(relation[row][_])
            store.add(tuple(temp))

        if len(store)==a and len(final)==0:
            final.append(set(arr))
        if len(store)==a and len(final)!=0 and not(any(elem.issubset(arr) for elem in final)):
            final.append(set(arr))
                    
        
        
    for i in range(1,b+1):
        def dfs(start):
            if len(arr)==i:
                return check(arr)
            for j in range(start,b):
                arr.append(j)
                start=j
                dfs(start+1)
                arr.pop()
        dfs(0)
                
    return len(final)