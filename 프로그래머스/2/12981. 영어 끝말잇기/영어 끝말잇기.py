def solution(n, words):
    k=len(words)
    visited=set()
    idx_list=[1 for _ in range(n)]
    
    
    def dfs(num,person,idx):
        if num==k+1:
            arr=[0,0]
            return arr
        if words[num-1] in visited:
            arr=[person,idx]
            return arr
        elif len(words[num-1])==1:
            arr=[person,idx]
            return arr
        elif num>1 and words[num-2][-1]!=words[num-1][0]:
            arr=[person,idx]
            return arr
        visited.add(words[num-1])
        num+=1
        idx_list[person-1]+=1
        person+=1
        if person!=n:
            person=(person)%n
        else:
            person=n
        idx=idx_list[person-1]
        return dfs(num,person,idx)
    return dfs(1,1,1)
       
            
            