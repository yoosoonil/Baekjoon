def solution(s):
    zero = 0
    cnt = 0
    
    # s가 '1'로 다 찰 때까지
    while s != '1':
        if '0' in s:
            zero += s.count('0')
            s = s.replace('0', '')
            
        length = len(s)
        
        # 2진수로 변환
        s = str(format(length,'b')) 
        cnt += 1            
        
        # 이진변환 횟수, 영의 개수
    return [cnt, zero]