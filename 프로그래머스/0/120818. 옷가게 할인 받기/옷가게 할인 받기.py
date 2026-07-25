def solution(price):
    answer = 0
    if price>=(10**5)*5:
        answer=int(price*0.8)
    elif price>=(10**5)*3:
        answer=int(price*0.9)
    elif price>=(10**5):
        answer=int(price*0.95)
    else:
        answer=price
    return int(answer)