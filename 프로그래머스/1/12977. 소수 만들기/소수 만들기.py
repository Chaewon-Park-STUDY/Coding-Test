def solution(nums):
    n=len(nums)
    arr=[]
    num=0
    
    def is_prime(arr):
        sum_val=sum(arr)
        for i in range(2,sum_val):
            if sum_val%i==0:
                return False
        return True
    
    def dfs(start):
        nonlocal num
        if len(arr)==3:
            if is_prime(arr):
                num+=1
            return
        for i in range(start,n):
            arr.append(nums[i])
            start=i
            dfs(start+1)
            arr.pop()
    dfs(0)
    return num