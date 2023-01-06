p = 10 ** 6

prime = [False, False] + [True] * (p - 1)

for i in range(1, int(p) + 1):
    if prime[i]:
        for j in range(2 * i, int(p) + 1, i):
            prime[j] = False
            
m, n = map(int, input().split())

for i in range(m, n + 1):
    if prime[i]:
        print(i)