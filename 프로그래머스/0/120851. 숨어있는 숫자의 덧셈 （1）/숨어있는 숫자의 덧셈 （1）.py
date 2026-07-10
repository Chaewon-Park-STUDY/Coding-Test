def solution(my_string):
    answer=0
    arr=list(map(str,list(my_string)))
    for elem in arr:
        if elem.isdigit()==True:
            answer+=int(elem)
            
    return answer