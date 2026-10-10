def solution(s):
    store=[]
    
    while s:
        is_continue=True
        if s=="":
            return 
        letter=''
        x=s[0]
        x_count=1
        letter+=x
        others_count=0
        for index, elem in enumerate(s[1:], start=1):
            if elem==x:
                x_count+=1
            else:
                others_count+=1
            letter+=elem
            if x_count==others_count:
                s=s[index+1:]
                store.append(letter)
                is_continue=False
                break
        if is_continue!=False:
            store.append(letter)
            break
    

    return len(store)     
                
                
            
            