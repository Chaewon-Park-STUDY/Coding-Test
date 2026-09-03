
arr=[]
num=0
start=0

def num_count(arr):
    global num
    if sum(arr)==0:
        num+=1
    
def solution(number):
    
    def dfs(start):
        if len(arr)==3:
            return num_count(arr)
        
        for i in range(start,len(number)):
            arr.append(number[i])
            start=i
            dfs(start+1)
            arr.pop()
    dfs(0)
    return num
    
    
    