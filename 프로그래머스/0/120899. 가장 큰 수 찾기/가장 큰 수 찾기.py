def solution(array):
    answer = []
    max_value=0
    index=0
    for i in range(len(array)):
        if array[i]>max_value:
            max_value=array[i]
            index=i
    answer.append(max_value)
    answer.append(index)
        
    return answer