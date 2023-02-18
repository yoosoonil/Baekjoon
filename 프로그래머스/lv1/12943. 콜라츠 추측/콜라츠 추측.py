def solution(num):
    answer = 0
    
    # num이 1이 되는 순간 while문을 멈춤
    while num != 1:
        if answer > 500:
            return -1
        if num % 2 == 0:
            num = num/2
        elif num % 2 == 1:
            num = (num*3) + 1
        answer += 1
    
    return answer