def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            p_cnt += 1
        elif s[i] == "y" or s[i] == "Y":
            y_cnt += 1
        
    if p_cnt == y_cnt:
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer