def solution(n):
    answer = ''
    for i in range(0, n):
        if i == 0:
            answer += "수"
        elif i == 1:
            answer += '박'
        elif i >= 2 and i % 2 == 0:
            answer += '수'
        elif i >= 2 and i % 2 == 1:
            answer += '박'
    
    return answer