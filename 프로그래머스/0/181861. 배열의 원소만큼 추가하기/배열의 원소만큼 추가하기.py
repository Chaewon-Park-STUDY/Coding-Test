def solution(arr):
    answer = []
    for elem in arr:
        for j in range(elem):
            answer.append(elem)
    return answer