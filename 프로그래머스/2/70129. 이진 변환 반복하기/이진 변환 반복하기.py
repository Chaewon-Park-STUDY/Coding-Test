def solution(s):
    store=[]
    answer=[]
    num_remove_0=0
    num_count=0
    
    
    def convert(n):
        if n==1:
            store.append(n)
            letter=''
            for elem in store[::-1]:
                letter+=str(elem)
            store.clear()  
            return letter
        store.append(n%2)
        n//=2
        return convert(n)
    
    def is_continue(p):
        nonlocal num_remove_0
        nonlocal num_count
        if p=='1':
            return 
        text=''
        num_count+=1
        for elem in p:
            if elem!="0":
                text+=elem
            else:
                num_remove_0+=1
                
        p=text
        p=convert(len(p))
        is_continue(p)
    is_continue(s)
    answer.append(num_count)
    answer.append(num_remove_0)
    return answer
            
  
