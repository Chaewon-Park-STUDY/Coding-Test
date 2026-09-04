index=[]
arr=[]
num=0

prime_set=set()
count_num=0
def solution(numbers):
    global num
    num+=1
    if num==1:
        store=[]
        for elem in numbers:
            store.append(elem)
    n=len(store)
     
    def is_prime(arr):
        global count_num
        letter=''
        for elem in arr:
                letter+=elem
        
        if all(int(letter)%i!=0 for i in range(2,int(letter))) and int(letter) not in prime_set and int(letter)!=1 and int(letter)!=0:
            count_num+=1
            prime_set.add(int(letter))
            
            
    def dfs():
        if len(arr) > 0:
            is_prime(arr)
        for i in range(n):
            if i not in index:
                index.append(i)
                arr.append(store[i])
                dfs()
                arr.pop()
                index.pop()
    dfs()
    return count_num
        
    