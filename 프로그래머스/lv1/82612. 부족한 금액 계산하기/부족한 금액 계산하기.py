def solution(price, money, count):
    tm = 0
    
    for i in range(1, count+1):
        tm += price * i
    
    if tm > money:
        return int(tm) - int(money)
    else:
        return 0