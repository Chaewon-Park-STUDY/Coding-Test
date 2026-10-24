def solution(priorities, location):
    k=len(priorities)
    stack=[i for i in range(k)]
    answer=[]
    store={}
    for i in range(k):
        store[i]=priorities[i]
    while True:
        is_changed=False
        for i in range(1,len(stack)):
            if store[stack[0]] < store[stack[i]]:
                index=stack.pop(0)
                stack.append(index)
                is_changed=True
                break
        if is_changed==False:
            if len(stack)==0:
                break
            answer.append(stack[0])
            stack.pop(0)
    return answer.index(location)+1
            