def solution(n, q, ans):
    store=[] #모든 가능한 조합들 담김
    arr=[]
    def code(n,q,ans,start):
        if len(arr)==5:
            store.append(tuple(arr))
            return 
        for i in range(start,n+1):
            arr.append(i)
            start=i
            code(n,q,ans,start+1)
            arr.pop()
    code(n,q,ans,1)
    final=[]
    
    for i in range(len(store)):
        passed=False
        for j in range(len(q)):
            num=0
            for elem in q[j]:
                if elem in store[i]:
                    num+=1
            if num==ans[j]:
                passed=True
                continue
            else:
                passed=False
                break
        if passed==False:
            continue
        else:
            final.append(store[i])
    return len(final)
    
        
        

        
        