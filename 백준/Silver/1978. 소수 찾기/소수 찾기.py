t = int(input())

nums = list(map(int, input().split()))

소수들 = []

for i in range(t):
  num = nums[i]
  is_prime = True
  if num > 1:
    for j in range(2, num):
      if num % j == 0:
        is_prime = False
    if is_prime:
      소수들.append(num)
    
print(len(소수들))