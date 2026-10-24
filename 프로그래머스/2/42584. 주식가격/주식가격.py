def solution(prices):
    stack=[]
    k=len(prices)
    answer=[0 for _ in range(k)]
    for i in range(k):
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)
            
    for i in range(k):
        if answer[i]==0:
            answer[i]=stack[-1]-stack.pop(0)
    return answer