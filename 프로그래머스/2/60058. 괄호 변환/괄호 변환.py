def solution(p):
    
    def is_correct(a):
        num_first=0
        num_second=0
        for i in range(len(a)):
            if a[i]=="(":
                num_first+=1
            else:
                num_second+=1
            if num_first<num_second:
                return False
        return True
    
    def convert(k):
        letter=k[1:-1]
        new=""
        for elem in letter:
            if elem=="(":
                new+=")"
            else:
                new+="("
        return new
    

    
    def dfs(s):
        if s == "":
            return ""
        num_first=0
        num_second=0
        for i in range(len(s)):
            if s[i]=="(":
                num_first+=1
            else:
                num_second+=1
            if num_first==num_second:
                u=s[:i+1]
                
                if i==len(s)-1:
                    v=""
                else:
                    v=s[i+1:]
                break
        if is_correct(u):
            return u+dfs(v)
        else:
            return "(" + dfs(v) + ")" +convert(u)
        dfs(v)
    return dfs(p)
    
    