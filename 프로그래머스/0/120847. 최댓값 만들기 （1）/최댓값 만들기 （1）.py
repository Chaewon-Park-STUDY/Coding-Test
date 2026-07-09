def solution(numbers):
    max_num= max(numbers)
    for i in range(len(numbers)):
        if numbers[i]==max(numbers):
            numbers.pop(i)
            break
    answer = max_num*max(numbers)
    return answer