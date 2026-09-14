def solution(n, control):
    start=n

    for i in range(len(control)):
            if control[i]=="w":
                start+=1
            elif control[i]=="s":
                start-=1
            elif control[i]=="d":
                start+=10
            else:
                start-=10
    return start
                
                