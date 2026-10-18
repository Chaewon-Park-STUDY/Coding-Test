def solution(cards1, cards2, goal):
    a=len(cards1)
    b=len(cards2)
    start=0
    default="Yes"
    
    def dfs(num1,num2):
        nonlocal start,default
        if start==len(goal):
            return
        if num1<a and cards1[num1]==goal[start]:
            start+=1
            num1+=1
            dfs(num1,num2)
        else:
            if num2<b and cards2[num2]==goal[start]:
                num2+=1
                start+=1
                dfs(num1,num2)
            else:
                default="No"
                return 
    dfs(0,0)
    return default
        