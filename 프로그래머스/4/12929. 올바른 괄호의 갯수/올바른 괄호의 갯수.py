def solution(n):
    picks=["(",")"]
    
    arr=[]
    num=0
    
    def dfs():
        nonlocal num
        if len(arr)==2*n:
            num+=1
            return 
        
        for i in range(2):
            if picks[i]=="(":
                if arr.count(picks[i])<n:
                    arr.append(picks[i])
                    dfs()
                    arr.pop()
            else:
                if arr.count(picks[i])<n and arr.count(")")<arr.count("("):
                    arr.append(picks[i])
                    dfs()
                    arr.pop()
    dfs()
    return num