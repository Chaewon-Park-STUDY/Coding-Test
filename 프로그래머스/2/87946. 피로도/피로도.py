arr=[]

max_val=0
def check(arr,k,dungeons):
    global max_val
    num=0
    if k>=dungeons[arr[0]][0]:
        left=k-dungeons[arr[0]][1]
        num+=1
        is_continue=True
        while left>0:
            for i in range(1,len(arr)):
                if left>=dungeons[arr[i]][0]:
                    left-=dungeons[arr[i]][1]
                    num+=1
                else:
                    is_continue=False
                    break
            max_val=max(max_val,num)
            if is_continue==False:
                break
            if left<=0:
                break

            
def solution(k, dungeons):
    n=len(dungeons)
    
    def dfs():
        if len(arr) == n:
            return check(arr,k,dungeons)

        for i in range(n):
            if i not in arr:
                arr.append(i)
                dfs() 
                arr.pop()  
    dfs()
    return max_val