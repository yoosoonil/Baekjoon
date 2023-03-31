def solution(n):
    count = 0 # 방법의 수
    for i in range(1, n+1):
        sum = 0 # i부터 시작하는 연속된 자연수들의 합
        for j in range(i, n+1):
            sum += j
            if sum == n:
                count += 1
                break
            elif sum > n:
                break
    return count