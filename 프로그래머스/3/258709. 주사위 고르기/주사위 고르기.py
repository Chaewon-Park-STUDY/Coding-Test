def solution(dice):
    n=len(dice)
    arr=[]
    store=[]
    sum_A=[]
    visited={}
        
    def search():
        if len(sum_A)==n//2:
            store.append(sum_A.copy())
            return 
            
        for i in range(6):
            sum_A.append(i)
            search()
            sum_A.pop()   
    search()
    
    k=len(store)
    def check(arr):
        A=arr
        B=[]
        a=len(arr)
        for i in range(n):
            if i not in arr:
                B.append(i)
        A_sums=[]
        B_sums=[]
        
        for choice in store:
            sum_of_A=0
            sum_of_B=0

            for j in range(a):
                sum_of_A += dice[arr[j]][choice[j]]
                sum_of_B += dice[B[j]][choice[j]]

            A_sums.append(sum_of_A)
            B_sums.append(sum_of_B)
        
        A_sums.sort()
        B_sums.sort()
        
        
        win = 0
        b = 0

        for sum_of_A in A_sums:
            while b < len(B_sums) and B_sums[b] < sum_of_A:
                b += 1

            win += b

        visited[tuple(arr)][0] = win
        
        
    max_val=0 
    max_index=[]
    def dfs(start):
        if len(arr)==n//2:
            visited[tuple(arr)]=[0 for _ in range(3)]
            return check(arr)
        
        for i in range(start,n):
            start=i
            arr.append(i)
            dfs(start+1)
            arr.pop()
    dfs(0)
    for elem in visited:
        max_val=max(max_val,visited.get(elem)[0])
        if max_val==visited.get(elem)[0]:
            max_index=elem
    final=[]
    for elem in max_index:
        elem+=1
        final.append(elem)
    return final
        
        
        
    
            
            
            