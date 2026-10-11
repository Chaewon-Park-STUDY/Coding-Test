def solution(k, room_number):
    store={}
    answer = []
    
    n=len(room_number)
    for i in range(n):
        k=room_number[i]
        visited=[]
        while k in store:
            visited.append(k)
            k=store[k]
        answer.append(k)
        store[k]=k+1
            
        for room in visited:
            store[room]=k+1
    return answer