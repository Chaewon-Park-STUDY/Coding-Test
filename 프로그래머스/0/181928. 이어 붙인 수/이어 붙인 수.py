def solution(num_list):
    odd=''
    even=''
    for elem in num_list:
        if elem%2!=0:
            odd+=str(elem)
        else:
            even+=str(elem)
    return int(odd)+int(even)