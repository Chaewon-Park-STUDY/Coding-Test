
def solution(orders, course):
    store=[]
    final=[]
    for i in range(len(course)):
        for j in range(len(orders)):
            arr=[]
            def node(start,orders,course):
                if len(arr)==course[i]:
                    temp=tuple(sorted(arr))
                    if temp not in store:
                        store.append(temp)
                    return 
                for k in range(start,len(orders[j])):
                    arr.append(orders[j][k])
                    start=k
                    node(start+1,orders,course)
                    arr.pop()
            node(0,orders,course)
    num_count=[0 for _ in range(len(store))]
                    
    for k in range(len(store)):
        for i in range(len(orders)):
            if all(elem in orders[i] for elem in store[k]):
                num_count[k]+=1
    for i in range(len(course)):
        candid=[]
        max_val=[]
        for j in range(len(store)):
            if num_count[j]>=2 and len(store[j])==course[i]:
                candid.append(store[j])
                max_val.append(num_count[j])
        if len(max_val)==0:
            pass
        else:
            for k in range(len(candid)-1,-1,-1):
                if max_val[k]!=max(max_val):
                    candid.pop(k)
        for l in range(len(candid)):
            letter=''
            for elem in candid[l]:
                letter+=elem
            final.append(letter)
    final.sort()
    return final
            
                
                
                    
 