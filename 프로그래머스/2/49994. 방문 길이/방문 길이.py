def solution(dirs):
    visited=set()
    
    def in_range(x,y):
        return -5<=x and x<6 and -5<=y and y<6
    
    x,y=0,0
    dxs,dys=[0,0,1,-1],[1,-1,0,0]    #U,D,R,L
    direction={}
    direction["U"]=0
    direction["D"]=1
    direction["R"]=2
    direction["L"]=3    
    
    for elem in dirs:
        def move(x,y,elem):
            dir=direction[elem]
            nx,ny=x+dxs[dir],y+dys[dir]
            if in_range(nx,ny):
                arr=[]
                arr.append((nx,ny))
                arr.append((x,y))
                arr.sort()
                if tuple(arr) not in visited:
                    visited.add(tuple(arr))
                x,y=nx,ny
            return x,y
            
        x,y=move(x,y,elem)
    return len(visited)