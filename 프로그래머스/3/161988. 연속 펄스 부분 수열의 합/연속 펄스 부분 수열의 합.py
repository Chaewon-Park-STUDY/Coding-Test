def solution(sequence):
    arr_A=[]
    arr_B=[]
    max_val=0
    reverse=[]
    for elem in sequence:
        elem*=-1
        reverse.append(elem)
    
    for i in range(len(sequence)):
        if i%2==0:
            arr_A.append(sequence[i])
        else:
            arr_A.append(reverse[i])
            
    for i in range(len(sequence)):
        if i%2!=0:
            arr_B.append(sequence[i])
        else:
            arr_B.append(reverse[i])
    n=len(sequence)
    total=arr_A[0]
    max_val=arr_A[0]
    store=[]
    
    for i in range(1,n):
        total=max(arr_A[i],total+arr_A[i])
        max_val=max(max_val,total)
    
    store.append(max_val)
    total=arr_B[0]
    max_val=arr_B[0]
    
    for i in range(1,n):
        total=max(arr_B[i],total+arr_B[i])
        max_val=max(max_val,total)
        
    store.append(max_val)
    
    return max(store)
 