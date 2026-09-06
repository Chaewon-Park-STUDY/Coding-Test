def in_range(x,y,n,m):
    return 0<=x and x<m and 0<=y and y<n

dxs,dys=[1,0,-1,0],[0,1,0,-1]

def candid(x,y,n,m,grid):
    arr=[]
    for i in range(4):
        dir=i
        nx,ny=x+dxs[dir],y+dys[dir]
        if in_range(nx,ny,n,m) and grid[nx][ny]!="X":
            arr.append((nx,ny))
    if len(arr)>0:
        return arr
    return False
            
def solution(maps):
    store=[]
    m=len(maps)
    n=len(maps[0])
    maps=[list(row) for row in maps]
    

    for i in range(m):
        for j in range(n):
            is_continue=True
            total=0
            if maps[i][j]!="X":
                total+=int(maps[i][j])
                maps[i][j]="X"
                stack=[]
                x,y=i,j
                while is_continue:
                    if candid(x,y,n,m,maps)==False:
                        if stack:
                            x,y=stack.pop()
                            if maps[x][y]!="X":
                                total+=int(maps[x][y])
                                maps[x][y]="X"
            
                        else:
                            is_continue=False
                            store.append(total)
                            break
                    else:
                        stack.extend(candid(x,y,n,m,maps))
                        x,y=stack.pop()
                        if maps[x][y]!="X":
                            total+=int(maps[x][y])
                            maps[x][y]="X"
    if len(store)==0:
        store.append(-1)
    else:
        store.sort()
    return store