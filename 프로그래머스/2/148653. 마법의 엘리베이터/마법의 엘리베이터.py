def solution(storey):
    num=0
    
    def dfs(a):
        nonlocal num
        if a==0:
            return 
        for i in range(1,10**11):
            if a//10**i==0:
                index=i-1
                division= a//10**(i-1)
                break
        digit=a%10
        rest=a//10
        if digit>5:
            num+=10-digit
            a=rest+1
        elif digit!=5:
            num+=digit
            a=rest
        else:
            num+=5
            if rest%10<5:
                a=rest
            else:
                a=rest+1
        dfs(a)
    dfs(storey)
    return num

        