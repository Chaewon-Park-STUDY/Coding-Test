def solution(num_list):
    num=1
    if len(num_list)>=11:
        return sum(num_list)
    elif len(num_list)<=10:
        for elem in num_list:
            num*=elem
        return num