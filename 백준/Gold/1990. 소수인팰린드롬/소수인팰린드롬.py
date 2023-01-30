a, b = map(int, input().split())

if b > 10 ** 7:
  b = 10 ** 7
  
prime = [False, False] + [True] * (b - 1)

for i in range(2, b + 1):
  if prime[i]:
      j = str(i)
      if j == j[::-1] and i >= a:
        print(i)
      for k in range(2 * i, b + 1, i):
        prime[k] = False
        
print(-1)