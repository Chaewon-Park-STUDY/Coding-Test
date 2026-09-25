def solution(progresses, speeds):
    arr=[]
    answer=[]
    n=len(progresses)
    for i in range(n):
        if (100-progresses[i])%speeds[i]==0:
            arr.append((100-progresses[i])//speeds[i])
        else:
            arr.append((100-progresses[i])//speeds[i]+1)
            
    
    num=1
    for i in range(1,n):
        if all(arr[i]>elem for elem in arr[:i]):
            answer.append(num)
            num=1
        else:
            num+=1
    answer.append(num)
    return answer
    