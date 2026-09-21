import sys
sys.setrecursionlimit(10000)


def solution(n, m, x, y, r, c, k):
    path=["d","l","r","u"]
    store=[]
    
    def x_in_range(a):
        return 1<=a and a<n+1 
    def y_in_range(b):
        return 1<=b and b<m+1
 
    
    def move(elem,start_x,start_y,num):
        is_continue=False
        if elem=="l":
            if y_in_range(start_y-1):
                start_y-=1
                num-=1
                is_continue=True
        elif elem=="r":
            if y_in_range(start_y+1):
                start_y+=1
                num-=1
                is_continue=True
        elif elem=="u":
            if x_in_range(start_x-1):
                start_x-=1
                num-=1
                is_continue=True
        else:
            if x_in_range(start_x+1):
                start_x+=1
                num-=1
                is_continue=True
        
        return start_x,start_y,num,is_continue
  
    arr=[]
    def check(arr, curr_x, curr_y):
        if curr_x == r and curr_y == c:
            if len(store)==0:
                store.append(''.join(arr))

    
    def dfs(curr_x, curr_y, left):
        if len(store)>0:
            return 
        if len(arr)==k:
            return check(arr,curr_x,curr_y)
        for i in range(4):
            arr.append(path[i])
            next_x,next_y,next_left,play=move(path[i],curr_x,curr_y,left)
            dist=abs(r-next_x)+abs(c-next_y)
            if play==True and dist<=next_left and (next_left-dist)%2==0:
                dfs(next_x,next_y,next_left)
            arr.pop()
    dfs(x,y,k)
            
    if len(store)>0:
        return store[0]
    else:
        return "impossible"