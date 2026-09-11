def solution(expression):
    operations=["+","-","*"]
    split_candid=[]
    store=[]
    max_val=0
  
    def splitting(expression):
        for i in range(len(expression)):
            if expression[i].isdigit()==False:
                split_candid.append(i)
        for i in range(len(split_candid)+1):
            letter=''
            if i==0:
                for elem in expression[0:split_candid[i]]:
                    letter+=elem
                store.append(int(letter))
                store.append(expression[split_candid[i]])
            elif i==len(split_candid):
                for elem in expression[split_candid[i-1]+1:]:
                    letter+=elem
                store.append(int(letter))
            else:
                for elem in expression[split_candid[i-1]+1:split_candid[i]]:
                    letter+=elem
                store.append(int(letter))
                store.append(expression[split_candid[i]])
    splitting(expression)
    n=len(store)

    def calculate(array,operator):
        if operator=="+":
            return array[0]+array[2]
        elif operator=="-":
            return array[0]-array[2]
        else:
            return array[0]*array[2]
        
    
    def apply(arr):
        nonlocal max_val
        new=store.copy()
        end=n-2
        for i in range(3):
            while arr[i] in new:
                temp=[]
                for j in range(len(new)):
                    if new[j]==arr[i]:
                        temp.extend(new[:j-1])
                        temp.append(calculate(new[j-1:j+2],arr[i]))
                        temp.extend(new[j+2:])
                        new=temp
                        break     
        max_val=max(max_val,abs(new[0]))
        
    arr=[]
    
    
    def dfs():
        if len(arr)==3:
            return apply(arr)
        
        for i in range(3):
            if operations[i] not in arr:
                arr.append(operations[i])
                dfs()
                arr.pop()
    dfs()
    return max_val
        