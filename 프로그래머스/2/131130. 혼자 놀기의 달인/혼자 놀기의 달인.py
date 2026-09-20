def solution(cards):
    n=len(cards)
    max_val=0
    
    for i in range(n):
        score=0
        group_1=[]
        start=cards[i]
        group_1.append(i+1)
        while True:
            if start not in group_1:
                group_1.append(start)
                start=cards[start-1]
            else:
                break
        if len(group_1)==n:
            score=0
            max_val=max(max_val,score)
        else:
            left=[]
            for j in range(n):
                if j+1 not in group_1:
                    left.append(j+1)
            for j in range(len(left)):
                start=cards[left[j]-1]
                group_2=[]
                group_2.append(left[j])
                while True:
                    if start not in group_2:
                        group_2.append(start)
                        start=cards[start-1]
                    else:
                        break
                score=len(group_1)*len(group_2)
                max_val=max(max_val,score)
    return max_val
            
        
        
            