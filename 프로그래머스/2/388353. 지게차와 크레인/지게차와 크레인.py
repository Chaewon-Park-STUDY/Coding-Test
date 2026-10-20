def solution(storage, requests):
    n=len(storage)
    m=len(storage[0])
    storage = [list(row) for row in storage]
    
    def in_range(x,y):
        return 0<=x and x<n and 0<=y and y<m
    
    def check(x,y):
        visited=set()
        dxs,dys=[1,0,-1,0],[0,1,0,-1]
        
        def dfs(x,y):
            visited.add((x,y))                      
            for i in range(4):
                dir=i
                nx,ny=x+dxs[dir],y+dys[dir]
                if not in_range(nx,ny):
                    return True
                elif storage[nx][ny]=="" and (nx,ny) not in visited:
                    if dfs(nx,ny):
                        return True
            return False
        return dfs(x,y)
       
        
    num=0
    for elem in requests:
        remove=[]
        for i in range(n):
            for j in range(m):
                if len(elem)==1:
                    if storage[i][j]==elem:
                        x,y=i,j
                        if check(x,y):
                            remove.append((x,y))
                else:
                    if storage[i][j]==elem[0]:
                        x,y=i,j
                        storage[x][y]=""  
                        num+=1
        num+=len(remove)
        for x,y in remove:
            storage[x][y]=""
    return n*m-num     
                        
                            