

def solution(n, lighthouse):
    arr={}
    for i in range(n+1):
        arr[i]=[]
    for elem in lighthouse:
        [x,y]=elem
        arr.get(x).append(y)
        arr.get(y).append(x)
    
    stack=[(1,0)]
    order=[]
    dp=[0 for _ in range(n+1)]
    
    while stack:
        node,parent=stack.pop()
        order.append((node, parent))
        for next_node in arr[node]:
            if next_node==parent:
                continue
            stack.append((next_node,node))

    for node, parent in reversed(order):
        on,off=1,0
        for next_node in arr[node]:
            if next_node==parent:
                continue
            child_on, child_off = dp[next_node]
            on+=min(child_on,child_off)
            off+=child_on
        dp[node]=[on,off]
    return min(dp[1][0],dp[1][1])
   
 