def solution(order):
    stack=[]
    arr=[i for i in range(1,len(order)+1)]
    arr.reverse()
    num_count=0
    num=0
    while num<len(order):
        if stack and stack[-1]==order[num]:
            stack.pop()
            num_count+=1
            num+=1
        elif arr and arr[-1]==order[num]:
            arr.pop()
            num_count+=1
            num+=1
        elif arr:
            box=arr.pop()
            stack.append(box)
        else:
            break
    return num_count
            
      
    
    