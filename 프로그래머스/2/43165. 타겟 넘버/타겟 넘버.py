arr=[]
num=0

def check(arr,numbers,target):
    total=0
    global num
    for k in range(len(numbers)):
        if arr[k]==2:
            total+=numbers[k]
        else:
            total+=(-1)*numbers[k]
            
    if total==target:
        num+=1

def solution(numbers, target):
    global num
    def dfs(start):
        if len(arr)==len(numbers):
            return check(arr,numbers,target)

        for i in range(2,4):
            arr.append(i)
            dfs(start+1)
            arr.pop()
    dfs(0)
    return num
            
        