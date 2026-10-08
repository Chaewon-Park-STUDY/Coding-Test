def solution(places):
    answer = [0 for _ in range(5)]
    for i in range(5):
        is_continue=True
        
        def in_range(x,y):
            return 0<=x and x<5 and 0<=y and y<5
        dxs,dys=[1,0,-1,0],[0,1,0,-1]
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=="P":
                    x,y=j,k
                    def dfs(x,y,num):
                        nonlocal is_continue
                        for l in range(4):
                                dir=l
                                nx,ny=x+dxs[dir],y+dys[dir]
                                if num==2:
                                    return 
                                if in_range(nx,ny) and (nx,ny)!=(j,k):
                                    if places[i][nx][ny]=="O":
                                        dfs(nx,ny,num+1)
                                    elif places[i][nx][ny]=="X":
                                        continue
                                    else:
                                        is_continue=False
                                        return 

                    dfs(j,k,0)
                if is_continue==False:
                    break
            if is_continue==False:
                break
        if is_continue==True:
            answer[i]=1
    return answer
            