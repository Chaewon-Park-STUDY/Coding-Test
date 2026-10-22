def solution(s):
    k=len(s)
    answer=0
    def check(letter):
        stack=[]
        for elem in letter:
             if elem in "([{":
                stack.append(elem)
             else:
                if not stack:
                    return False
                if stack[-1] + elem in ["()", "[]", "{}"]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

    if check(s):
        answer+=1
    num=1
    
    while num<k:
        index=s[0]
        s=s[1:]
        s+=index
        if check(s):
            answer+=1
        num+=1
    return answer
        
        