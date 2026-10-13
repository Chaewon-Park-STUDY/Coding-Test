def solution(babbling):
    store=["aya","ye","woo","ma"]
    num=0
    for elem in babbling:
        n=len(elem)
        def dfs(start):
            nonlocal num
            if start==n:
                num+=1
                return
            
            for i in range(2,4):
                if elem[start:start+i] in store:
                    dfs(start+i)
                else:
                    continue
        dfs(0)
    return num