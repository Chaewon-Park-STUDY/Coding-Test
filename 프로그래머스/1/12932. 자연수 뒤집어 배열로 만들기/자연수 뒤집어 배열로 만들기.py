def solution(n):
    answer = []
    for elem in str(n)[-1::-1]:
        answer.append(int(elem))
    return answer