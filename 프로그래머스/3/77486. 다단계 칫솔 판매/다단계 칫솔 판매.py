def solution(enroll, referral, seller, amount):
    store={}
    price={}
    for elem,key in zip(enroll,referral):
        if key!="-":
            store[elem]=[key]
        else:
            store[elem]=[]
        price[elem]=[]
    for elem,key in zip(seller,amount):
        price.get(elem).append(key*100-(key*100)//10)
        a=(key*100)//10
        def dfs(p,a):
            for next_node in store[p]:
                price.get(next_node).append(a-a//10)
                a=a//10
                if a==0:
                    return 
                dfs(next_node,a)
        dfs(elem,a)
    answer=[]
    for elem in price:
        answer.append(sum(price.get(elem)))
    return answer
            
        