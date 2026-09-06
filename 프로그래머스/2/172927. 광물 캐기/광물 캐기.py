min_val=10**10

def solution(picks, minerals):
    store=["d","i","s"]
    
    n=len(minerals)
    if n%5>0:
        if sum(picks)>=n//5+1:
            pairs=n//5+1
        else:
            pairs=sum(picks)
    else:
        if sum(picks)>=n//5:
            pairs=n//5
        else:
            pairs=sum(picks)
    
    Fatigue={}
    Fatigue["d"]=[1,1,1]
    Fatigue["i"]=[5,1,1]
    Fatigue["s"]=[25,5,1]
    
    def fatigue(a,b,minerals):
        if a=="d":
            if minerals[b]=="diamond":
                return Fatigue.get(a)[0]
            elif minerals[b]=="iron":
                return Fatigue.get(a)[1]
            else:
                return Fatigue.get(a)[2]
        elif a=="i":
            if minerals[b]=="diamond":
                return Fatigue.get(a)[0]
            elif minerals[b]=="iron":
                return Fatigue.get(a)[1]
            else:
                return Fatigue.get(a)[2]
        else:
            if minerals[b]=="diamond":
                return Fatigue.get(a)[0]
            elif minerals[b]=="iron":
                return Fatigue.get(a)[1]
            else:
                return Fatigue.get(a)[2]
                
    def check(start,arr):
        global min_val
        total=0
        for i in range(len(arr)):
            if i!=len(arr)-1:
                for j in range(start,start+5):
                    total+=fatigue(arr[i],j,minerals)
                start+=5
            else:
                end=min(len(minerals),start+5)
                for j in range(start,end):
                    total+=fatigue(arr[i],j,minerals)
        min_val=min(min_val,total)
            
    arr=[]  
    def dfs():
        if len(arr)==pairs:
            return check(0,arr)
        
        for i in range(3):
            if picks[i]>0:
                picks[i]-=1
                arr.append(store[i])
                dfs()
                arr.pop()
                picks[i]+=1
    dfs()
    return min_val