def solution(phone_number):
    answer = ''
    k=len(phone_number)
    answer+="*"*(k-4)
    answer+=phone_number[-4::]
    return answer