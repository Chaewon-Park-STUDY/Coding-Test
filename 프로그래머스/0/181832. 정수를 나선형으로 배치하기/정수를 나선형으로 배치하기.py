def solution(n):
    grid=[[0 for _ in range(n)]for _ in range(n)]
    
    def in_range(x,y):
        return 0<=x and x<n and 0<=y and y<n
    num=1
    grid[0][0]=num
    dxs,dys=[0,1,0,-1],[1,0,-1,0]
    dir=0
    
    x,y=0,0
    while num<n**2:
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny) and grid[nx][ny]==0:
            x,y=nx,ny
            num+=1
            grid[x][y]=num
        else:
            dir=(dir+1)%4
            grid[x][y]=num
    return grid
            
            
    