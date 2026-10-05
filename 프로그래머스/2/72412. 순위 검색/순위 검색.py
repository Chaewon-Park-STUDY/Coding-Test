def solution(info, query):
    store=[]
    a=len(info)
    b=len(query)
    candid={}
    for c in info:
        parts = c.split()
        key = tuple(parts[:4])
        score = int(parts[-1])

        if key not in candid:
            candid[key] = []
        candid[key].append(score)

    num=[0 for _ in range(b)]
    for q in query:
        arr = []
        for elem in q.split():
            if elem != "and":
                arr.append(elem)
        store.append(arr)
    
    for key in candid:
        candid[key].sort()
    
    from bisect import bisect_left
    
    for i in range(b):
        for key in candid:
            if set(elem for elem in store[i][:4] if elem != "-").issubset(key):
                idx = bisect_left(candid[key], int(store[i][-1]))
                num[i] += len(candid[key]) - idx
    return num
                
    
