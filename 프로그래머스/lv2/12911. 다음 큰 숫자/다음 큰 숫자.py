def solution(n):
    c = bin(n).count('1')
    # 제한사항으로 1,000,000 이하의 자연수.
    # 그래서 1,000,001 범위까지 돌리는 것.
    for m in range(n+1, 1000001):
        if bin(m).count('1') == c:
            return m