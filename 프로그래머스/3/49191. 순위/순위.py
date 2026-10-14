def solution(n, results):
    win={}
    lose={}
    for i in range(1,n+1):
        win[i]=[]
        lose[i]=[]
        
    for elem in results:
        [x,y]=elem
        win[x].append(y)
        lose[y].append(x)
    
    num=0
    
    for i in range(1,n+1):
        win_set=set()
        lose_set=set()
    
        def winner(a):
            for next_node in win[a]:
                if next_node not in win_set:
                    win_set.add(next_node)
                    winner(next_node)
        def loser(a):
            for next_node in lose[a]:
                if next_node not in lose_set:
                    lose_set.add(next_node)
                    loser(next_node)
        winner(i)
        loser(i)
            
        
        if len(win_set)+len(lose_set)==n-1:
            num+=1
    return num