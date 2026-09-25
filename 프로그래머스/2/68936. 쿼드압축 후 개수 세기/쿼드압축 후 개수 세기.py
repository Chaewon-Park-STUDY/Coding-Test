def solution(arr):
    n=len(arr)

    
    count_1=0
    count_0=0
    
    def check(a,b,c):
        x=arr[a][b]
        nonlocal count_1
        nonlocal count_0
        for elem in arr[a:a+c]:
            for _ in elem[b:b+c]:
                if _==x:
                    continue
                else:
                    return False
        if x==1:
            count_1+=1
        else:
            count_0+=1
        return True
            
    store=[(0,0,n)]
    while store:
        a,b,c=store.pop()
        if check(a,b,c):
            continue
        half=c//2
            
        store.append((a+half,b,half))
        store.append((a,b,half))
        store.append((a,b+half,half))
        store.append((a+half,b+half,half))
            
    return [count_0,count_1]
            
    
    
    
    
    
    
    
    
    