def solution(my_string):
    answer = []
    letter=''
    for elem in my_string:
        if elem.isalpha()==True:
            letter+=elem
        else:
            if letter!='':
                answer.append(letter)
            letter=''
    if letter!="":
        answer.append(letter)
    return answer