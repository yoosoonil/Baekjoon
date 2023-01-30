import sys

input = sys.stdin.readline


p = 10 ** 6 

prime = [False, False] + [True] * (p - 1)

# 에라토스테네스의 체를 이용한 방식
for i in range(1, int(p ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, p + 1, i):
            prime[j] = False

while True:
    n = int(input())
    # n값이 0 이라면 종료
    if not n:
        break
    
    for i in range(1, n + 1):
        if prime[i] and prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            break