import math
a, b = map(int, input().split())

# 최대공약수 구하기
# 주어진 숫자의 약수 중에 최대인 값을 구하는 것
# for i in range(min(a,b), 0, -1):
#   if a % i == 0 and b % i == 0:
#     print(i)
#     break

# 최소공배수 구하기
# 주어진 숫자의 배수중에 최소인 값을 구하는 것
# for i in range(max(a,b), (a*b)+1):
#   if i % a == 0 and i % b == 0:
#     print(i)
#     break

# 라이브러리 이용

print(math.gcd(a, b)) # 최대공약수
print(math.lcm(a, b)) # 최소공배수