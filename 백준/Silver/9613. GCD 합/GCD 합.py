import math
import sys
t = int(input()) # 테스트 수


for _ in range(t):
  n = list(map(int, sys.stdin.readline().split())) # 한줄씩 들어오는 input값을 읽으니까. sys.stdin.readline
  total = 0
  for j in range(1, len(n)):
    for k in range(j+1, len(n)): # 다음 것과 최소공배수 구하기.
      total += math.gcd(n[j], n[k])
  print(total)