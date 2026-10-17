def solution(babbling):
    able=["aya","ye","woo","ma"]

    num=0
    for elem in babbling:
        n=len(elem)
        spoken=[]
        def dfs(start):
            nonlocal num
            if start==n:
                num+=1
                return
            if len(spoken)==0:
                if elem[start:start+2] in able:
                    spoken.append(elem[start:start+2])
                    start+=2
                    dfs(start)
                elif elem[start:start+3] in able:
                    spoken.append(elem[start:start+3])
                    start+=3
                    dfs(start)
            else:
                if elem[start:start+2] in able and spoken[-1]!=elem[start:start+2]:
                    spoken.append(elem[start:start+2])
                    start+=2
                    dfs(start)
                elif elem[start:start+3] in able and spoken[-1]!=elem[start:start+3]:
                    spoken.append(elem[start:start+3])
                    start+=3
                    dfs(start)
                else:
                    return
        dfs(0)
    return num
               
                
                
            