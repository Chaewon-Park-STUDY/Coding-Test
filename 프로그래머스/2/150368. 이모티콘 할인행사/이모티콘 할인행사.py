def solution(users, emoticons):
    sale=[10,20,30,40]
    m= len(emoticons)
    n= len(users)
    arr=[]
    answer=set()
    
    def check(arr):
        store=[]
        service_num=0
        sell_price=0
        
        buy_index=[[] for _ in range(n)]
        buy_price=[0 for _ in range(n)]
        for i in range(m):
            store.append(emoticons[i]*(100-arr[i])*0.01)
        for i in range(n):
            price=0
            rate=users[i][0]
            for j in range(m):  
                if arr[j]>=rate:
                    buy_index[i].append(j)
                    price+=store[j]
            buy_price[i]=price
            if buy_price[i]>=users[i][1]:
                service_num+=1
            else:
                sell_price+=buy_price[i]
        answer.add((service_num,sell_price))
                        

    def sale_rate():
        if len(arr)==m:
            return check(arr)
        for i in range(4):
            arr.append(sale[i])
            sale_rate()
            arr.pop()
    sale_rate()
    answer = sorted(answer, reverse=True)
    return list(answer[0])