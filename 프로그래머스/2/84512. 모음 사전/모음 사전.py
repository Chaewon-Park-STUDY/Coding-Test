arr=[]

def solution(word):
    picks=["A","E","I","O","U"]
    
    #start는 점점 감소하는 형태로 
    def dfs(arr,start,num):
        letter=''
        for elem in arr:
            letter+=elem
        if letter==word:
            return num,True
        
        if len(arr)==start:
            if start>0:
                start-=1
                return num,False
        for i in range(5):
            arr.append(picks[i])
            num+=1
            result,found=dfs(arr,start,num)
            num=result
            arr.pop()
            if found:
                return result,True
        return num,False
    num,bool=dfs(arr,5,0)
    return num
    

            
        